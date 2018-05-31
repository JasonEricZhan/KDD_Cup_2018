from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input,Dropout,Activation,GRU,Conv1D,CuDNNGRU
from keras.layers import SpatialDropout1D,MaxPool1D,RepeatVector,MaxPooling1D
from keras.layers import Bidirectional,BatchNormalization,concatenate,TimeDistributed
from keras.models import Model
from keras import initializers, regularizers, constraints, optimizers, layers
from keras.optimizers import Adam,SGD,Nadam
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers.core import Layer  
from keras import initializers, regularizers, constraints  
from keras import backend as K


def dot_product(x, kernel):
    """
    Wrapper for dot product operation, in order to be compatible with both
    Theano and Tensorflow
    Args:
        x (): input
        kernel (): weights
    Returns:
    """
    if K.backend() == 'tensorflow':
        return K.squeeze(K.dot(x, K.expand_dims(kernel)), axis=-1)
    else:
        return K.dot(x, kernel)
    
#better for detect time series' order
class AttentionWithContext(Layer):
    """
        Attention operation, with a context/query vector, for temporal data.
        Supports Masking.
        Follows the work of Yang et al. [https://www.cs.cmu.edu/~diyiy/docs/naacl16.pdf]
        "Hierarchical Attention Networks for Document Classification"
        by using a context vector to assist the attention
        # Input shape
            3D tensor with shape: `(samples, steps, features)`.
        # Output shape
            2D tensor with shape: `(samples, features)`.
        :param kwargs:
        Just put it on top of an RNN Layer (GRU/LSTM/SimpleRNN) with return_sequences=True.
        The dimensions are inferred based on the output shape of the RNN.
        Example:
            model.add(LSTM(64, return_sequences=True))
            model.add(AttentionWithContext())
        """

    def __init__(self, init='glorot_uniform', kernel_regularizer=None, bias_regularizer=None, kernel_constraint=None, bias_constraint=None,  **kwargs):
        self.supports_masking = True
        self.init = initializers.get(init)
        self.kernel_initializer = initializers.get('glorot_uniform')

        self.kernel_regularizer = regularizers.get(kernel_regularizer)
        self.bias_regularizer = regularizers.get(bias_regularizer)

        self.kernel_constraint = constraints.get(kernel_constraint)
        self.bias_constraint = constraints.get(bias_constraint)

        super(AttentionWithContext, self).__init__(**kwargs)

    def build(self, input_shape):
        self.kernel = self.add_weight((input_shape[-1], 1),
                                 initializer=self.kernel_initializer,
                                 name='{}_W'.format(self.name),
                                 regularizer=self.kernel_regularizer,
                                 constraint=self.kernel_constraint)
        self.b = self.add_weight((input_shape[1],),
                                 initializer='zero',
                                 name='{}_b'.format(self.name),
                                 regularizer=self.bias_regularizer,
                                 constraint=self.bias_constraint)

        self.u = self.add_weight((input_shape[1],),
                                 initializer=self.kernel_initializer,
                                 name='{}_u'.format(self.name),
                                 regularizer=self.kernel_regularizer,
                                 constraint=self.kernel_constraint)
        self.built = True

    def compute_mask(self, input, mask):
        return None

    def call(self, x, mask=None):
        # (x, 40, 300) x (300, 1)
        multData =  K.dot(x, self.kernel) # (x, 40, 1)
        multData = K.squeeze(multData, -1) # (x, 40)
        multData = multData + self.b # (x, 40) + (40,)

        multData = K.tanh(multData) # (x, 40)

        multData = multData * self.u # (x, 40) * (40, 1) => (x, 1)
        multData = K.exp(multData) # (X, 1)

        # apply mask after the exp. will be re-normalized next
        if mask is not None:
            mask = K.cast(mask, K.floatx()) #(x, 40)
            multData = mask*multData #(x, 40) * (x, 40, )

        # in some cases especially in the early stages of training the sum may be almost zero
        # and this results in NaN's. A workaround is to add a very small positive number ε to the sum.
        # a /= K.cast(K.sum(a, axis=1, keepdims=True), K.floatx())
        multData /= K.cast(K.sum(multData, axis=1, keepdims=True) + K.epsilon(), K.floatx())
        multData = K.expand_dims(multData)
        weighted_input = x * multData
        return K.sum(weighted_input, axis=1)


    def compute_output_shape(self, input_shape):
        return (input_shape[0], input_shape[-1],)
        
from keras import backend as K

def smape_loss_keras(true, predicted):
    """
    Differentiable SMAPE loss
    :param true: Truth values
    :param predicted: Predicted values
    :return: 6 columns' mean smape_loss
    """
    epsilon=1e-8
    nominater=K.abs(predicted-true)
    summ = true+predicted+epsilon
    smape = nominater / summ * 2.0
    s1=smape[:,0]
    s1=K.mean(s1)
    s2=smape[:,1]
    s2=K.mean(s2)
    s3=smape[:,2]
    s3=K.mean(s3)
    s4=smape[:,3]
    s4=K.mean(s4)
    s5=smape[:,4]
    s5=K.mean(s5)
    s6=smape[:,5]
    s6=K.mean(s6)
    return (s1+s2+s3+s4+s5+s6)/6
    
#for beijin
def weather_model(MAX_time_step=_Eric_created_,grid_station_num=100,feature_num=20):
     sub_input = Input(shape=(grid_station_num,feature_num), dtype='float32')
     l_Con_sub = Conv1D(filters=128, kernel_size=8, strides=1, padding='same',activation='elu')(sub_input)
     l_Con_sub = Conv1D(filters=64, kernel_size=3, strides=1, padding='same',activation='elu')(l_Con_sub)

     l_att = AttentionWithContext()(l_Con_sub)

     subextractor = Model(sub_input, l_att )
    
     review_input = Input(shape=(MAX_time_step,grid_station_num,feature_num), dtype='float32',name='aux_input')
     review_encoder = TimeDistributed(subextractor)(review_input)
     #review_encoder = Conv1D(filters=32, kernel_size=8, strides=1, padding='same',activation='elu')(review_encoder)
     return review_input,review_encoder


def mapping_extractor(aqi_station_num=35,grid_station_num=100,MAX_time_step=_Eric_created_,embed_activation='linear'):
     AQI_dist_input = Input(shape=(aqi_station_num,), dtype='float32',name='AQI_dist_input')
     AQI_dist_1D=RepeatVector(MAX_time_step)(AQI_dist_input)
     AQI_dist_1D=TimeDistributed(Dense(30,activation=embed_activation))(AQI_dist_1D)
     AQI_dist_1D=TimeDistributed(Dense(25,activation=embed_activation))(AQI_dist_1D)
     AQI_dist_1D= Conv1D(filters=24, kernel_size=8, strides=1, padding='same',activation='elu')(AQI_dist_1D)
     AQI_dist_1D= Conv1D(filters=16, kernel_size=3, strides=1, padding='same',activation='elu')(AQI_dist_1D)
     AQI_dist_1D=MaxPooling1D(2,padding='same',strides=1)(AQI_dist_1D)

     Grid_dist_input = Input(shape=(grid_station_num,), dtype='float32',name='Grid_dist_input')
     Grid_dist_1D=RepeatVector(MAX_time_step)(Grid_dist_input)
     Grid_dist_1D=TimeDistributed(Dense(450,activation=embed_activation))(Grid_dist_1D)
     Grid_dist_1D=TimeDistributed(Dense(300,activation=embed_activation))(Grid_dist_1D)
     Grid_dist_1D= Conv1D(filters=256, kernel_size=8, strides=1, padding='same',activation='elu')(Grid_dist_1D)
     Grid_dist_1D= Conv1D(filters=100, kernel_size=3, strides=1, padding='same',activation='elu')(Grid_dist_1D)
     Grid_dist_1D=MaxPooling1D(2,padding='same',strides=1)(Grid_dist_1D)
     return AQI_dist_input,Grid_dist_input,AQI_dist_1D,Grid_dist_1D

def pollution_extractor(MAX_time_step=_Eric_created_,feature_num=15):
     pollution_input = Input(shape=(MAX_time_step,feature_num), dtype='float32',name='main_input')
     l_Con_main = Conv1D(filters=64, kernel_size=8, strides=1, padding='same',activation='elu')(pollution_input)
     l_Con_main = Conv1D(filters=32, kernel_size=3, strides=1, padding='same',activation='elu')(l_Con_main)
     l_Con_main=MaxPooling1D(2,padding='same',strides=1)(l_Con_main)
     return  pollution_input,l_Con_main







MAX_time_step=48
def main_model_att(ts=MAX_time_step,last_drop_out_rate=0.1,skip_connected=False,multi_length_cnn=False
                   adding_another_drop_out=False):
     s0 = Input(shape=(128,), name='hidden_state')
     s=s0
    
     last= Input(shape=(128,), name='last_state') #feed autocorrelation and the last element in the last sequence (t-1)
     last=Dense(512,activation='selu')(last)
     last=Dense(256,activation='selu')(last)
     last=Dense(128,activation='selu')(last)
     last=RepeatVector(MAX_time_step)(last)
        
     review_input,review_encoder=weather_model(aqi_station_num=35,MAX_time_step=ts,grid_station_num=100,feature_num=20)
     AQI_dist_input,Grid_dist_input,AQI_dist_1D,Grid_dist_1D=mapping_extractor(MAX_time_step=ts)
     pollution_input,l_Con_main=pollution_extractor(MAX_time_step=ts)
    
     #review_encoder=TimeDistributed(Dense(64))(review_encoder)

     comb=concatenate([review_encoder,l_Con_main,AQI_dist_1D,Grid_dist_1D,last])
    
     if multi_length_cnn:
        long_time= Conv1D(filters=200, kernel_size=16, strides=1, padding='same',activation='elu')(comb)
        mid_time= Conv1D(filters=200, kernel_size=8, strides=1, padding='same',activation='elu')(comb)
        short_time= Conv1D(filters=200, kernel_size=3, strides=1, padding='same',activation='elu')(comb)
        comb=concatenate([long_time,mid_time,short_time])
        comb= Conv1D(filters=256, kernel_size=8, strides=1, padding='same',activation='elu')(comb)
        comb= Conv1D(filters=128, kernel_size=3, strides=1, padding='same',activation='elu')(comb)
        comb=MaxPooling1D(2,padding='same',strides=1)(comb)
     else:
        if skip_connected:
            skipconnect=comb
        comb= Conv1D(filters=200, kernel_size=12, strides=1, padding='same',activation='elu')(comb)
        comb= Conv1D(filters=200, kernel_size=6, strides=1, padding='same',activation='elu')(comb)
        comb= Conv1D(filters=128, kernel_size=3, strides=1, padding='same',activation='elu')(comb)
     #comb= Conv1D(filters=64, kernel_size=3, strides=1, padding='same',activation='elu')(comb)
        comb=MaxPooling1D(2,padding='same',strides=1)(comb)
        if skip_connected:
            comb=concatenate([comb,skipconnect])
     comb=BatchNormalization()(comb)

     comb_gru  = Bidirectional(CuDNNGRU(128,return_sequences=True))(comb)
     #comb_gru  = Bidirectional(CuDNNGRU(128,return_sequences=True))(comb_gru)

     outputs = []
     for t in range(MAX_time_step):
          if  t is  0:
             comb= AttentionWithContext()(comb_gru)
             repeator = RepeatVector(MAX_time_step)(comb)
             s1=repeator
             s2,_= CuDNNGRU(128,return_state=True)(s1,initial_state=[s])  #feed zero or other special information
             output=s2   
             prev=s2
             if adding_another_drop_out:
               output=Dropout(last_drop_out_rate)(output)
             output=Dense(64,activation='relu')(output)
             output=Dropout(last_drop_out_rate)(output)
             output=Dense(6,activation='relu')(output)
             prev=RepeatVector(MAX_time_step)(prev)
          else:
             comb=concatenate([comb_gru ,prev])
             comb= AttentionWithContext()(comb_gru)
             repeator = RepeatVector(MAX_time_step)(comb)
             s1=repeator
             s2,_= CuDNNGRU(128,return_state=True)(s1,initial_state=[s2])
             output=s2  
             prev=s2
             if adding_another_drop_out:
               output=Dropout(last_drop_out_rate)(output)
             output=Dense(64,activation='relu')(output)
             output=Dropout(last_drop_out_rate)(output)
             output=Dense(6,activation='relu')(output)
             prev=RepeatVector(MAX_time_step)(prev)
        
          outputs.append(output)
     model = Model([review_input,pollution_input,AQI_dist_input,Grid_dist_input,s0], outputs)
     print(model.summary())
     return model


model=main_model_att()
    
    
model.compile(optimizer = Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.003), loss=smape_loss_keras, 
              metrics=['mae'])
