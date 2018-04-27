
##  This is the EDA for 2018 KDD CUP

# Checker




```python
import pandas as pd
path='../ml_dataset/2018_kdd_cup_dataset/'
pd.read_csv(path+"beijing_17_18_aq.csv")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>stationId</th>
      <th>utc_time</th>
      <th>PM2.5</th>
      <th>PM10</th>
      <th>NO2</th>
      <th>CO</th>
      <th>O3</th>
      <th>SO2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-01 14:00:00</td>
      <td>453.0</td>
      <td>467.0</td>
      <td>156.0</td>
      <td>7.2</td>
      <td>3.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-01 15:00:00</td>
      <td>417.0</td>
      <td>443.0</td>
      <td>143.0</td>
      <td>6.8</td>
      <td>2.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-01 16:00:00</td>
      <td>395.0</td>
      <td>467.0</td>
      <td>141.0</td>
      <td>6.9</td>
      <td>3.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-01 17:00:00</td>
      <td>420.0</td>
      <td>484.0</td>
      <td>139.0</td>
      <td>7.4</td>
      <td>3.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-01 18:00:00</td>
      <td>453.0</td>
      <td>520.0</td>
      <td>157.0</td>
      <td>7.6</td>
      <td>4.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-01 19:00:00</td>
      <td>429.0</td>
      <td>NaN</td>
      <td>141.0</td>
      <td>6.5</td>
      <td>3.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-01 20:00:00</td>
      <td>211.0</td>
      <td>NaN</td>
      <td>110.0</td>
      <td>3.3</td>
      <td>NaN</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-01 21:00:00</td>
      <td>116.0</td>
      <td>NaN</td>
      <td>87.0</td>
      <td>2.2</td>
      <td>4.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-01 22:00:00</td>
      <td>51.0</td>
      <td>NaN</td>
      <td>58.0</td>
      <td>1.3</td>
      <td>26.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-01 23:00:00</td>
      <td>38.0</td>
      <td>NaN</td>
      <td>55.0</td>
      <td>1.1</td>
      <td>28.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 00:00:00</td>
      <td>21.0</td>
      <td>NaN</td>
      <td>40.0</td>
      <td>0.7</td>
      <td>42.0</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 01:00:00</td>
      <td>16.0</td>
      <td>NaN</td>
      <td>40.0</td>
      <td>0.8</td>
      <td>44.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 02:00:00</td>
      <td>23.0</td>
      <td>NaN</td>
      <td>42.0</td>
      <td>0.7</td>
      <td>45.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 03:00:00</td>
      <td>18.0</td>
      <td>NaN</td>
      <td>30.0</td>
      <td>0.6</td>
      <td>59.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 04:00:00</td>
      <td>58.0</td>
      <td>247.0</td>
      <td>76.0</td>
      <td>2.4</td>
      <td>46.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 05:00:00</td>
      <td>176.0</td>
      <td>NaN</td>
      <td>99.0</td>
      <td>0.3</td>
      <td>42.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 06:00:00</td>
      <td>109.0</td>
      <td>211.0</td>
      <td>86.0</td>
      <td>2.6</td>
      <td>58.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 07:00:00</td>
      <td>267.0</td>
      <td>NaN</td>
      <td>125.0</td>
      <td>4.2</td>
      <td>53.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 08:00:00</td>
      <td>260.0</td>
      <td>NaN</td>
      <td>115.0</td>
      <td>3.9</td>
      <td>56.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 09:00:00</td>
      <td>212.0</td>
      <td>NaN</td>
      <td>112.0</td>
      <td>3.6</td>
      <td>50.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 10:00:00</td>
      <td>183.0</td>
      <td>NaN</td>
      <td>111.0</td>
      <td>0.3</td>
      <td>33.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 11:00:00</td>
      <td>136.0</td>
      <td>NaN</td>
      <td>89.0</td>
      <td>2.3</td>
      <td>41.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 12:00:00</td>
      <td>137.0</td>
      <td>NaN</td>
      <td>89.0</td>
      <td>2.2</td>
      <td>35.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 13:00:00</td>
      <td>125.0</td>
      <td>NaN</td>
      <td>90.0</td>
      <td>2.1</td>
      <td>28.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 14:00:00</td>
      <td>153.0</td>
      <td>NaN</td>
      <td>108.0</td>
      <td>2.5</td>
      <td>13.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 15:00:00</td>
      <td>165.0</td>
      <td>NaN</td>
      <td>126.0</td>
      <td>3.1</td>
      <td>2.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 16:00:00</td>
      <td>225.0</td>
      <td>NaN</td>
      <td>148.0</td>
      <td>4.9</td>
      <td>4.0</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 17:00:00</td>
      <td>275.0</td>
      <td>NaN</td>
      <td>158.0</td>
      <td>6.4</td>
      <td>7.0</td>
      <td>28.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 18:00:00</td>
      <td>293.0</td>
      <td>NaN</td>
      <td>155.0</td>
      <td>6.4</td>
      <td>5.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>aotizhongxin_aq</td>
      <td>2017-01-02 19:00:00</td>
      <td>293.0</td>
      <td>NaN</td>
      <td>153.0</td>
      <td>6.2</td>
      <td>5.0</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>310980</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 10:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310981</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 11:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310982</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 12:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310983</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 13:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310984</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 14:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310985</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 15:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310986</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 16:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310987</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 17:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310988</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 18:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310989</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 19:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310990</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 20:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310991</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 21:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310992</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 22:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310993</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-30 23:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310994</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310995</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 01:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310996</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 02:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310997</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 03:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310998</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 04:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310999</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 05:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>311000</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 06:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>311001</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 07:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>311002</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 08:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>311003</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 09:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>311004</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 10:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>311005</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 11:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>311006</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 12:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>311007</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 13:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>311008</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 14:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>311009</th>
      <td>zhiwuyuan_aq</td>
      <td>2018-01-31 15:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>311010 rows × 8 columns</p>
</div>




```python
beji_aqi_sta=pd.read_csv(path+"Beijing_AirQuality_Stations_en.xlsx")
```


    -------------------------------------------

    UnicodeDecodeErrorTraceback (most recent call last)

    <ipython-input-215-635ed99cc902> in <module>()
    ----> 1 beji_aqi_sta=pd.read_csv(path+"Beijing_AirQuality_Stations_en.xlsx")
    

    ~/.local/lib/python3.5/site-packages/pandas/io/parsers.py in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skipfooter, skip_footer, doublequote, delim_whitespace, as_recarray, compact_ints, use_unsigned, low_memory, buffer_lines, memory_map, float_precision)
        707                     skip_blank_lines=skip_blank_lines)
        708 
    --> 709         return _read(filepath_or_buffer, kwds)
        710 
        711     parser_f.__name__ = name


    ~/.local/lib/python3.5/site-packages/pandas/io/parsers.py in _read(filepath_or_buffer, kwds)
        447 
        448     # Create the parser.
    --> 449     parser = TextFileReader(filepath_or_buffer, **kwds)
        450 
        451     if chunksize or iterator:


    ~/.local/lib/python3.5/site-packages/pandas/io/parsers.py in __init__(self, f, engine, **kwds)
        816             self.options['has_index_names'] = kwds['has_index_names']
        817 
    --> 818         self._make_engine(self.engine)
        819 
        820     def close(self):


    ~/.local/lib/python3.5/site-packages/pandas/io/parsers.py in _make_engine(self, engine)
       1047     def _make_engine(self, engine='c'):
       1048         if engine == 'c':
    -> 1049             self._engine = CParserWrapper(self.f, **self.options)
       1050         else:
       1051             if engine == 'python':


    ~/.local/lib/python3.5/site-packages/pandas/io/parsers.py in __init__(self, src, **kwds)
       1693         kwds['allow_leading_cols'] = self.index_col is not False
       1694 
    -> 1695         self._reader = parsers.TextReader(src, **kwds)
       1696 
       1697         # XXX


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader.__cinit__()


    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._get_header()


    UnicodeDecodeError: 'utf-8' codec can't decode bytes in position 0-1: invalid continuation byte



```python
Lodon_aqi=pd.read_csv(path+"London_historical_aqi_forecast_stations_20180331.csv")
Lodon_aqi
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>MeasurementDateGMT</th>
      <th>station_id</th>
      <th>PM2.5 (ug/m3)</th>
      <th>PM10 (ug/m3)</th>
      <th>NO2 (ug/m3)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2017/1/1 0:00</td>
      <td>CD1</td>
      <td>40.0</td>
      <td>44.4</td>
      <td>36.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2017/1/1 1:00</td>
      <td>CD1</td>
      <td>31.6</td>
      <td>34.4</td>
      <td>46.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2017/1/1 2:00</td>
      <td>CD1</td>
      <td>24.7</td>
      <td>28.1</td>
      <td>38.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2017/1/1 3:00</td>
      <td>CD1</td>
      <td>21.2</td>
      <td>24.5</td>
      <td>32.8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2017/1/1 4:00</td>
      <td>CD1</td>
      <td>24.9</td>
      <td>23.0</td>
      <td>28.1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>2017/1/1 5:00</td>
      <td>CD1</td>
      <td>24.6</td>
      <td>23.9</td>
      <td>29.3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>2017/1/1 6:00</td>
      <td>CD1</td>
      <td>23.9</td>
      <td>22.0</td>
      <td>28.8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>2017/1/1 7:00</td>
      <td>CD1</td>
      <td>22.0</td>
      <td>22.9</td>
      <td>34.6</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>2017/1/1 8:00</td>
      <td>CD1</td>
      <td>19.0</td>
      <td>20.1</td>
      <td>44.6</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>2017/1/1 9:00</td>
      <td>CD1</td>
      <td>19.9</td>
      <td>24.4</td>
      <td>55.3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>2017/1/1 10:00</td>
      <td>CD1</td>
      <td>16.6</td>
      <td>17.5</td>
      <td>46.4</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>2017/1/1 11:00</td>
      <td>CD1</td>
      <td>14.5</td>
      <td>14.6</td>
      <td>42.5</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>2017/1/1 12:00</td>
      <td>CD1</td>
      <td>11.0</td>
      <td>13.9</td>
      <td>44.5</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>2017/1/1 13:00</td>
      <td>CD1</td>
      <td>13.9</td>
      <td>13.4</td>
      <td>53.6</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>2017/1/1 14:00</td>
      <td>CD1</td>
      <td>8.3</td>
      <td>8.6</td>
      <td>61.4</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>2017/1/1 15:00</td>
      <td>CD1</td>
      <td>7.3</td>
      <td>6.1</td>
      <td>57.9</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>2017/1/1 16:00</td>
      <td>CD1</td>
      <td>4.9</td>
      <td>6.1</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>2017/1/1 17:00</td>
      <td>CD1</td>
      <td>4.6</td>
      <td>8.1</td>
      <td>96.5</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>2017/1/1 18:00</td>
      <td>CD1</td>
      <td>8.3</td>
      <td>7.3</td>
      <td>64.2</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
      <td>2017/1/1 19:00</td>
      <td>CD1</td>
      <td>7.3</td>
      <td>8.9</td>
      <td>59.7</td>
    </tr>
    <tr>
      <th>20</th>
      <td>20</td>
      <td>2017/1/1 20:00</td>
      <td>CD1</td>
      <td>7.8</td>
      <td>11.3</td>
      <td>61.3</td>
    </tr>
    <tr>
      <th>21</th>
      <td>21</td>
      <td>2017/1/1 21:00</td>
      <td>CD1</td>
      <td>11.1</td>
      <td>9.8</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>22</td>
      <td>2017/1/1 22:00</td>
      <td>CD1</td>
      <td>7.1</td>
      <td>13.0</td>
      <td>50.9</td>
    </tr>
    <tr>
      <th>23</th>
      <td>23</td>
      <td>2017/1/1 23:00</td>
      <td>CD1</td>
      <td>6.8</td>
      <td>11.4</td>
      <td>40.2</td>
    </tr>
    <tr>
      <th>24</th>
      <td>24</td>
      <td>2017/1/2 0:00</td>
      <td>CD1</td>
      <td>6.2</td>
      <td>7.3</td>
      <td>33.9</td>
    </tr>
    <tr>
      <th>25</th>
      <td>25</td>
      <td>2017/1/2 1:00</td>
      <td>CD1</td>
      <td>9.0</td>
      <td>9.9</td>
      <td>21.7</td>
    </tr>
    <tr>
      <th>26</th>
      <td>26</td>
      <td>2017/1/2 2:00</td>
      <td>CD1</td>
      <td>8.2</td>
      <td>6.4</td>
      <td>19.5</td>
    </tr>
    <tr>
      <th>27</th>
      <td>27</td>
      <td>2017/1/2 3:00</td>
      <td>CD1</td>
      <td>7.0</td>
      <td>9.1</td>
      <td>18.8</td>
    </tr>
    <tr>
      <th>28</th>
      <td>28</td>
      <td>2017/1/2 4:00</td>
      <td>CD1</td>
      <td>6.7</td>
      <td>8.6</td>
      <td>19.7</td>
    </tr>
    <tr>
      <th>29</th>
      <td>29</td>
      <td>2017/1/2 5:00</td>
      <td>CD1</td>
      <td>7.4</td>
      <td>13.3</td>
      <td>27.7</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>141631</th>
      <td>10867</td>
      <td>2018/3/29 19:00</td>
      <td>TH4</td>
      <td>8.5</td>
      <td>16.7</td>
      <td>85.9</td>
    </tr>
    <tr>
      <th>141632</th>
      <td>10868</td>
      <td>2018/3/29 20:00</td>
      <td>TH4</td>
      <td>8.8</td>
      <td>19.4</td>
      <td>89.6</td>
    </tr>
    <tr>
      <th>141633</th>
      <td>10869</td>
      <td>2018/3/29 21:00</td>
      <td>TH4</td>
      <td>8.8</td>
      <td>17.9</td>
      <td>82.4</td>
    </tr>
    <tr>
      <th>141634</th>
      <td>10870</td>
      <td>2018/3/29 22:00</td>
      <td>TH4</td>
      <td>5.0</td>
      <td>14.5</td>
      <td>61.8</td>
    </tr>
    <tr>
      <th>141635</th>
      <td>10871</td>
      <td>2018/3/29 23:00</td>
      <td>TH4</td>
      <td>4.6</td>
      <td>14.2</td>
      <td>67.6</td>
    </tr>
    <tr>
      <th>141636</th>
      <td>10872</td>
      <td>2018/3/30 0:00</td>
      <td>TH4</td>
      <td>4.8</td>
      <td>11.8</td>
      <td>55.4</td>
    </tr>
    <tr>
      <th>141637</th>
      <td>10873</td>
      <td>2018/3/30 1:00</td>
      <td>TH4</td>
      <td>2.0</td>
      <td>11.4</td>
      <td>47.4</td>
    </tr>
    <tr>
      <th>141638</th>
      <td>10874</td>
      <td>2018/3/30 2:00</td>
      <td>TH4</td>
      <td>4.2</td>
      <td>13.5</td>
      <td>51.4</td>
    </tr>
    <tr>
      <th>141639</th>
      <td>10875</td>
      <td>2018/3/30 3:00</td>
      <td>TH4</td>
      <td>3.1</td>
      <td>13.8</td>
      <td>45.8</td>
    </tr>
    <tr>
      <th>141640</th>
      <td>10876</td>
      <td>2018/3/30 4:00</td>
      <td>TH4</td>
      <td>5.0</td>
      <td>12.6</td>
      <td>45.4</td>
    </tr>
    <tr>
      <th>141641</th>
      <td>10877</td>
      <td>2018/3/30 5:00</td>
      <td>TH4</td>
      <td>4.4</td>
      <td>13.1</td>
      <td>45.6</td>
    </tr>
    <tr>
      <th>141642</th>
      <td>10878</td>
      <td>2018/3/30 6:00</td>
      <td>TH4</td>
      <td>8.2</td>
      <td>14.6</td>
      <td>47.4</td>
    </tr>
    <tr>
      <th>141643</th>
      <td>10879</td>
      <td>2018/3/30 7:00</td>
      <td>TH4</td>
      <td>8.2</td>
      <td>18.3</td>
      <td>36.6</td>
    </tr>
    <tr>
      <th>141644</th>
      <td>10880</td>
      <td>2018/3/30 8:00</td>
      <td>TH4</td>
      <td>9.0</td>
      <td>15.6</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>141645</th>
      <td>10881</td>
      <td>2018/3/30 9:00</td>
      <td>TH4</td>
      <td>9.1</td>
      <td>17.7</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>141646</th>
      <td>10882</td>
      <td>2018/3/30 10:00</td>
      <td>TH4</td>
      <td>10.3</td>
      <td>12.7</td>
      <td>35.3</td>
    </tr>
    <tr>
      <th>141647</th>
      <td>10883</td>
      <td>2018/3/30 11:00</td>
      <td>TH4</td>
      <td>12.0</td>
      <td>13.2</td>
      <td>29.4</td>
    </tr>
    <tr>
      <th>141648</th>
      <td>10884</td>
      <td>2018/3/30 12:00</td>
      <td>TH4</td>
      <td>9.1</td>
      <td>13.5</td>
      <td>26.2</td>
    </tr>
    <tr>
      <th>141649</th>
      <td>10885</td>
      <td>2018/3/30 13:00</td>
      <td>TH4</td>
      <td>7.7</td>
      <td>15.0</td>
      <td>35.3</td>
    </tr>
    <tr>
      <th>141650</th>
      <td>10886</td>
      <td>2018/3/30 14:00</td>
      <td>TH4</td>
      <td>7.0</td>
      <td>12.2</td>
      <td>36.6</td>
    </tr>
    <tr>
      <th>141651</th>
      <td>10887</td>
      <td>2018/3/30 15:00</td>
      <td>TH4</td>
      <td>6.4</td>
      <td>11.0</td>
      <td>30.9</td>
    </tr>
    <tr>
      <th>141652</th>
      <td>10888</td>
      <td>2018/3/30 16:00</td>
      <td>TH4</td>
      <td>6.4</td>
      <td>14.0</td>
      <td>39.8</td>
    </tr>
    <tr>
      <th>141653</th>
      <td>10889</td>
      <td>2018/3/30 17:00</td>
      <td>TH4</td>
      <td>14.4</td>
      <td>16.6</td>
      <td>55.2</td>
    </tr>
    <tr>
      <th>141654</th>
      <td>10890</td>
      <td>2018/3/30 18:00</td>
      <td>TH4</td>
      <td>11.2</td>
      <td>18.8</td>
      <td>63.3</td>
    </tr>
    <tr>
      <th>141655</th>
      <td>10891</td>
      <td>2018/3/30 19:00</td>
      <td>TH4</td>
      <td>6.3</td>
      <td>16.1</td>
      <td>67.7</td>
    </tr>
    <tr>
      <th>141656</th>
      <td>10892</td>
      <td>2018/3/30 20:00</td>
      <td>TH4</td>
      <td>3.5</td>
      <td>11.2</td>
      <td>44.3</td>
    </tr>
    <tr>
      <th>141657</th>
      <td>10893</td>
      <td>2018/3/30 21:00</td>
      <td>TH4</td>
      <td>4.7</td>
      <td>12.3</td>
      <td>52.8</td>
    </tr>
    <tr>
      <th>141658</th>
      <td>10894</td>
      <td>2018/3/30 22:00</td>
      <td>TH4</td>
      <td>5.4</td>
      <td>14.0</td>
      <td>54.7</td>
    </tr>
    <tr>
      <th>141659</th>
      <td>10895</td>
      <td>2018/3/30 23:00</td>
      <td>TH4</td>
      <td>8.9</td>
      <td>16.5</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>141660</th>
      <td>10896</td>
      <td>2018/3/31 0:00</td>
      <td>TH4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>141661 rows × 6 columns</p>
</div>




```python
Lodon_aqi.isnull().sum()
```




    Unnamed: 0                0
    MeasurementDateGMT        0
    station_id                0
    PM2.5 (ug/m3)         18676
    PM10 (ug/m3)          14553
    NO2 (ug/m3)           25445
    dtype: int64




```python
#import xlrd
import csv



import pandas as pd


def xlsx_to_csv_pd():
    data_xls = pd.read_excel(path+'Beijing_AirQuality_Stations_en.xlsx', index_col=0)
    data_xls.to_csv('Beijing_AirQuality_Stations.csv', encoding='utf-8')


if __name__ == '__main__':
    xlsx_to_csv_pd()
    
    
```


```python
len(Lodon_aqi)
```




    141661




```python
import re
re.split('/|:| ',Lodon_aqi['MeasurementDateGMT'][0])

```




    ['2017', '1', '1', '0', '00']




```python
pd.read_csv(path+"London_historical_aqi_other_stations_20180331.csv")
```

    /home/paslab/.local/lib/python3.5/site-packages/IPython/core/interactiveshell.py:2785: DtypeWarning: Columns (0,1) have mixed types. Specify dtype option on import or set low_memory=False.
      interactivity=interactivity, compiler=compiler, result=result)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Station_ID</th>
      <th>MeasurementDateGMT</th>
      <th>PM2.5 (ug/m3)</th>
      <th>PM10 (ug/m3)</th>
      <th>NO2 (ug/m3)</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>LH0</td>
      <td>2017/1/1 0:00</td>
      <td>30.2</td>
      <td>34.6</td>
      <td>15.9</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LH0</td>
      <td>2017/1/1 1:00</td>
      <td>25.4</td>
      <td>29.2</td>
      <td>11.8</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>LH0</td>
      <td>2017/1/1 2:00</td>
      <td>24.7</td>
      <td>28.1</td>
      <td>11.6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>LH0</td>
      <td>2017/1/1 3:00</td>
      <td>23.6</td>
      <td>27.0</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>LH0</td>
      <td>2017/1/1 4:00</td>
      <td>24.2</td>
      <td>27.4</td>
      <td>27.1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>LH0</td>
      <td>2017/1/1 5:00</td>
      <td>22.8</td>
      <td>26.0</td>
      <td>22.9</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LH0</td>
      <td>2017/1/1 6:00</td>
      <td>21.6</td>
      <td>24.8</td>
      <td>26.8</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>LH0</td>
      <td>2017/1/1 7:00</td>
      <td>19.9</td>
      <td>23.1</td>
      <td>39.4</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>LH0</td>
      <td>2017/1/1 8:00</td>
      <td>18.3</td>
      <td>21.3</td>
      <td>41.6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>LH0</td>
      <td>2017/1/1 9:00</td>
      <td>16.3</td>
      <td>19.5</td>
      <td>44.1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>LH0</td>
      <td>2017/1/1 10:00</td>
      <td>13.3</td>
      <td>16.2</td>
      <td>49.1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>LH0</td>
      <td>2017/1/1 11:00</td>
      <td>9.4</td>
      <td>11.6</td>
      <td>45.2</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>LH0</td>
      <td>2017/1/1 12:00</td>
      <td>6.1</td>
      <td>8.5</td>
      <td>41.4</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>LH0</td>
      <td>2017/1/1 13:00</td>
      <td>6.7</td>
      <td>13.4</td>
      <td>53.6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>LH0</td>
      <td>2017/1/1 14:00</td>
      <td>2.1</td>
      <td>4.6</td>
      <td>11.7</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>LH0</td>
      <td>2017/1/1 15:00</td>
      <td>0.9</td>
      <td>2.0</td>
      <td>12.1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>LH0</td>
      <td>2017/1/1 16:00</td>
      <td>1.1</td>
      <td>2.1</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>LH0</td>
      <td>2017/1/1 17:00</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>13.5</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>LH0</td>
      <td>2017/1/1 18:00</td>
      <td>1.5</td>
      <td>2.5</td>
      <td>14.6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>LH0</td>
      <td>2017/1/1 19:00</td>
      <td>2.1</td>
      <td>3.6</td>
      <td>14.7</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>LH0</td>
      <td>2017/1/1 20:00</td>
      <td>2.9</td>
      <td>4.8</td>
      <td>15.5</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>LH0</td>
      <td>2017/1/1 21:00</td>
      <td>4.5</td>
      <td>6.9</td>
      <td>14.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>LH0</td>
      <td>2017/1/1 22:00</td>
      <td>4.9</td>
      <td>7.8</td>
      <td>11.6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>LH0</td>
      <td>2017/1/1 23:00</td>
      <td>5.9</td>
      <td>9.3</td>
      <td>11.8</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>LH0</td>
      <td>2017/1/2 0:00</td>
      <td>5.1</td>
      <td>8.4</td>
      <td>9.6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>LH0</td>
      <td>2017/1/2 1:00</td>
      <td>4.5</td>
      <td>7.7</td>
      <td>6.9</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>LH0</td>
      <td>2017/1/2 2:00</td>
      <td>4.3</td>
      <td>7.7</td>
      <td>7.3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>LH0</td>
      <td>2017/1/2 3:00</td>
      <td>4.9</td>
      <td>8.4</td>
      <td>6.5</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>LH0</td>
      <td>2017/1/2 4:00</td>
      <td>6.7</td>
      <td>10.8</td>
      <td>7.1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>LH0</td>
      <td>2017/1/2 5:00</td>
      <td>7.0</td>
      <td>13.1</td>
      <td>15.3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>141603</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141604</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141605</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141606</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141607</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141608</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141609</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141610</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141611</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141612</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141613</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141614</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141615</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141616</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141617</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141618</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141619</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141620</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141621</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141622</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141623</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141624</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141625</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141626</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141627</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141628</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141629</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141630</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141631</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>141632</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>141633 rows × 7 columns</p>
</div>



Geograhy





```python
pd.read_csv(path+"London_grid_weather_station.csv")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>london_grid_000</th>
      <th>50.5</th>
      <th>-2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>london_grid_001</td>
      <td>50.6</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>london_grid_002</td>
      <td>50.7</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>london_grid_003</td>
      <td>50.8</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>london_grid_004</td>
      <td>50.9</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>london_grid_005</td>
      <td>51.0</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>london_grid_006</td>
      <td>51.1</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>london_grid_007</td>
      <td>51.2</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>london_grid_008</td>
      <td>51.3</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>london_grid_009</td>
      <td>51.4</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>london_grid_010</td>
      <td>51.5</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>london_grid_011</td>
      <td>51.6</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>london_grid_012</td>
      <td>51.7</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>london_grid_013</td>
      <td>51.8</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>london_grid_014</td>
      <td>51.9</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>london_grid_015</td>
      <td>52.0</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>london_grid_016</td>
      <td>52.1</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>london_grid_017</td>
      <td>52.2</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>london_grid_018</td>
      <td>52.3</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>london_grid_019</td>
      <td>52.4</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>london_grid_020</td>
      <td>52.5</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>london_grid_021</td>
      <td>50.5</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <th>21</th>
      <td>london_grid_022</td>
      <td>50.6</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <th>22</th>
      <td>london_grid_023</td>
      <td>50.7</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <th>23</th>
      <td>london_grid_024</td>
      <td>50.8</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <th>24</th>
      <td>london_grid_025</td>
      <td>50.9</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <th>25</th>
      <td>london_grid_026</td>
      <td>51.0</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <th>26</th>
      <td>london_grid_027</td>
      <td>51.1</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <th>27</th>
      <td>london_grid_028</td>
      <td>51.2</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <th>28</th>
      <td>london_grid_029</td>
      <td>51.3</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <th>29</th>
      <td>london_grid_030</td>
      <td>51.4</td>
      <td>-1.9</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>830</th>
      <td>london_grid_831</td>
      <td>51.7</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>831</th>
      <td>london_grid_832</td>
      <td>51.8</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>832</th>
      <td>london_grid_833</td>
      <td>51.9</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>833</th>
      <td>london_grid_834</td>
      <td>52.0</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>834</th>
      <td>london_grid_835</td>
      <td>52.1</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>835</th>
      <td>london_grid_836</td>
      <td>52.2</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>836</th>
      <td>london_grid_837</td>
      <td>52.3</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>837</th>
      <td>london_grid_838</td>
      <td>52.4</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>838</th>
      <td>london_grid_839</td>
      <td>52.5</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>839</th>
      <td>london_grid_840</td>
      <td>50.5</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>840</th>
      <td>london_grid_841</td>
      <td>50.6</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>841</th>
      <td>london_grid_842</td>
      <td>50.7</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>842</th>
      <td>london_grid_843</td>
      <td>50.8</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>843</th>
      <td>london_grid_844</td>
      <td>50.9</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>844</th>
      <td>london_grid_845</td>
      <td>51.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>845</th>
      <td>london_grid_846</td>
      <td>51.1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>846</th>
      <td>london_grid_847</td>
      <td>51.2</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>847</th>
      <td>london_grid_848</td>
      <td>51.3</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>848</th>
      <td>london_grid_849</td>
      <td>51.4</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>849</th>
      <td>london_grid_850</td>
      <td>51.5</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>850</th>
      <td>london_grid_851</td>
      <td>51.6</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>851</th>
      <td>london_grid_852</td>
      <td>51.7</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>852</th>
      <td>london_grid_853</td>
      <td>51.8</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>853</th>
      <td>london_grid_854</td>
      <td>51.9</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>854</th>
      <td>london_grid_855</td>
      <td>52.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>855</th>
      <td>london_grid_856</td>
      <td>52.1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>856</th>
      <td>london_grid_857</td>
      <td>52.2</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>857</th>
      <td>london_grid_858</td>
      <td>52.3</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>858</th>
      <td>london_grid_859</td>
      <td>52.4</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>859</th>
      <td>london_grid_860</td>
      <td>52.5</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
<p>860 rows × 3 columns</p>
</div>




```python
pd.read_csv(path+"Beijing_grid_weather_station.csv")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>beijing_grid_000</th>
      <th>39</th>
      <th>115</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>beijing_grid_001</td>
      <td>39.1</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>beijing_grid_002</td>
      <td>39.2</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>beijing_grid_003</td>
      <td>39.3</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>beijing_grid_004</td>
      <td>39.4</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>beijing_grid_005</td>
      <td>39.5</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>beijing_grid_006</td>
      <td>39.6</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>beijing_grid_007</td>
      <td>39.7</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>beijing_grid_008</td>
      <td>39.8</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>beijing_grid_009</td>
      <td>39.9</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>beijing_grid_010</td>
      <td>40.0</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>beijing_grid_011</td>
      <td>40.1</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>beijing_grid_012</td>
      <td>40.2</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>beijing_grid_013</td>
      <td>40.3</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>beijing_grid_014</td>
      <td>40.4</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>beijing_grid_015</td>
      <td>40.5</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>beijing_grid_016</td>
      <td>40.6</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>beijing_grid_017</td>
      <td>40.7</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>beijing_grid_018</td>
      <td>40.8</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>beijing_grid_019</td>
      <td>40.9</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>beijing_grid_020</td>
      <td>41.0</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>beijing_grid_021</td>
      <td>39.0</td>
      <td>115.1</td>
    </tr>
    <tr>
      <th>21</th>
      <td>beijing_grid_022</td>
      <td>39.1</td>
      <td>115.1</td>
    </tr>
    <tr>
      <th>22</th>
      <td>beijing_grid_023</td>
      <td>39.2</td>
      <td>115.1</td>
    </tr>
    <tr>
      <th>23</th>
      <td>beijing_grid_024</td>
      <td>39.3</td>
      <td>115.1</td>
    </tr>
    <tr>
      <th>24</th>
      <td>beijing_grid_025</td>
      <td>39.4</td>
      <td>115.1</td>
    </tr>
    <tr>
      <th>25</th>
      <td>beijing_grid_026</td>
      <td>39.5</td>
      <td>115.1</td>
    </tr>
    <tr>
      <th>26</th>
      <td>beijing_grid_027</td>
      <td>39.6</td>
      <td>115.1</td>
    </tr>
    <tr>
      <th>27</th>
      <td>beijing_grid_028</td>
      <td>39.7</td>
      <td>115.1</td>
    </tr>
    <tr>
      <th>28</th>
      <td>beijing_grid_029</td>
      <td>39.8</td>
      <td>115.1</td>
    </tr>
    <tr>
      <th>29</th>
      <td>beijing_grid_030</td>
      <td>39.9</td>
      <td>115.1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>620</th>
      <td>beijing_grid_621</td>
      <td>40.2</td>
      <td>117.9</td>
    </tr>
    <tr>
      <th>621</th>
      <td>beijing_grid_622</td>
      <td>40.3</td>
      <td>117.9</td>
    </tr>
    <tr>
      <th>622</th>
      <td>beijing_grid_623</td>
      <td>40.4</td>
      <td>117.9</td>
    </tr>
    <tr>
      <th>623</th>
      <td>beijing_grid_624</td>
      <td>40.5</td>
      <td>117.9</td>
    </tr>
    <tr>
      <th>624</th>
      <td>beijing_grid_625</td>
      <td>40.6</td>
      <td>117.9</td>
    </tr>
    <tr>
      <th>625</th>
      <td>beijing_grid_626</td>
      <td>40.7</td>
      <td>117.9</td>
    </tr>
    <tr>
      <th>626</th>
      <td>beijing_grid_627</td>
      <td>40.8</td>
      <td>117.9</td>
    </tr>
    <tr>
      <th>627</th>
      <td>beijing_grid_628</td>
      <td>40.9</td>
      <td>117.9</td>
    </tr>
    <tr>
      <th>628</th>
      <td>beijing_grid_629</td>
      <td>41.0</td>
      <td>117.9</td>
    </tr>
    <tr>
      <th>629</th>
      <td>beijing_grid_630</td>
      <td>39.0</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>630</th>
      <td>beijing_grid_631</td>
      <td>39.1</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>631</th>
      <td>beijing_grid_632</td>
      <td>39.2</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>632</th>
      <td>beijing_grid_633</td>
      <td>39.3</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>633</th>
      <td>beijing_grid_634</td>
      <td>39.4</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>634</th>
      <td>beijing_grid_635</td>
      <td>39.5</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>635</th>
      <td>beijing_grid_636</td>
      <td>39.6</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>636</th>
      <td>beijing_grid_637</td>
      <td>39.7</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>637</th>
      <td>beijing_grid_638</td>
      <td>39.8</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>638</th>
      <td>beijing_grid_639</td>
      <td>39.9</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>639</th>
      <td>beijing_grid_640</td>
      <td>40.0</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>640</th>
      <td>beijing_grid_641</td>
      <td>40.1</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>641</th>
      <td>beijing_grid_642</td>
      <td>40.2</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>642</th>
      <td>beijing_grid_643</td>
      <td>40.3</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>643</th>
      <td>beijing_grid_644</td>
      <td>40.4</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>644</th>
      <td>beijing_grid_645</td>
      <td>40.5</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>645</th>
      <td>beijing_grid_646</td>
      <td>40.6</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>646</th>
      <td>beijing_grid_647</td>
      <td>40.7</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>647</th>
      <td>beijing_grid_648</td>
      <td>40.8</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>648</th>
      <td>beijing_grid_649</td>
      <td>40.9</td>
      <td>118.0</td>
    </tr>
    <tr>
      <th>649</th>
      <td>beijing_grid_650</td>
      <td>41.0</td>
      <td>118.0</td>
    </tr>
  </tbody>
</table>
<p>650 rows × 3 columns</p>
</div>



## From here is the geographic EDA 

### The station in Beijin


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```


```python
beijingAqCsv = pd.read_csv('../ml_dataset/2018_kdd_cup_dataset/beijing_17_18_aq.csv')
air_station_beij = beijingAqCsv.groupby("stationId", sort=False) 
```


```python
air_station_beij.groups
```




    {'aotizhongxin_aq': Int64Index([   0,    1,    2,    3,    4,    5,    6,    7,    8,    9,
                 ...
                 8876, 8877, 8878, 8879, 8880, 8881, 8882, 8883, 8884, 8885],
                dtype='int64', length=8886),
     'badaling_aq': Int64Index([ 8886,  8887,  8888,  8889,  8890,  8891,  8892,  8893,  8894,
                  8895,
                 ...
                 17762, 17763, 17764, 17765, 17766, 17767, 17768, 17769, 17770,
                 17771],
                dtype='int64', length=8886),
     'beibuxinqu_aq': Int64Index([17772, 17773, 17774, 17775, 17776, 17777, 17778, 17779, 17780,
                 17781,
                 ...
                 26648, 26649, 26650, 26651, 26652, 26653, 26654, 26655, 26656,
                 26657],
                dtype='int64', length=8886),
     'daxing_aq': Int64Index([26658, 26659, 26660, 26661, 26662, 26663, 26664, 26665, 26666,
                 26667,
                 ...
                 35534, 35535, 35536, 35537, 35538, 35539, 35540, 35541, 35542,
                 35543],
                dtype='int64', length=8886),
     'dingling_aq': Int64Index([35544, 35545, 35546, 35547, 35548, 35549, 35550, 35551, 35552,
                 35553,
                 ...
                 44420, 44421, 44422, 44423, 44424, 44425, 44426, 44427, 44428,
                 44429],
                dtype='int64', length=8886),
     'donggaocun_aq': Int64Index([44430, 44431, 44432, 44433, 44434, 44435, 44436, 44437, 44438,
                 44439,
                 ...
                 53306, 53307, 53308, 53309, 53310, 53311, 53312, 53313, 53314,
                 53315],
                dtype='int64', length=8886),
     'dongsi_aq': Int64Index([53316, 53317, 53318, 53319, 53320, 53321, 53322, 53323, 53324,
                 53325,
                 ...
                 62192, 62193, 62194, 62195, 62196, 62197, 62198, 62199, 62200,
                 62201],
                dtype='int64', length=8886),
     'dongsihuan_aq': Int64Index([62202, 62203, 62204, 62205, 62206, 62207, 62208, 62209, 62210,
                 62211,
                 ...
                 71078, 71079, 71080, 71081, 71082, 71083, 71084, 71085, 71086,
                 71087],
                dtype='int64', length=8886),
     'fangshan_aq': Int64Index([71088, 71089, 71090, 71091, 71092, 71093, 71094, 71095, 71096,
                 71097,
                 ...
                 79964, 79965, 79966, 79967, 79968, 79969, 79970, 79971, 79972,
                 79973],
                dtype='int64', length=8886),
     'fengtaihuayuan_aq': Int64Index([79974, 79975, 79976, 79977, 79978, 79979, 79980, 79981, 79982,
                 79983,
                 ...
                 88850, 88851, 88852, 88853, 88854, 88855, 88856, 88857, 88858,
                 88859],
                dtype='int64', length=8886),
     'guanyuan_aq': Int64Index([88860, 88861, 88862, 88863, 88864, 88865, 88866, 88867, 88868,
                 88869,
                 ...
                 97736, 97737, 97738, 97739, 97740, 97741, 97742, 97743, 97744,
                 97745],
                dtype='int64', length=8886),
     'gucheng_aq': Int64Index([ 97746,  97747,  97748,  97749,  97750,  97751,  97752,  97753,
                  97754,  97755,
                 ...
                 106622, 106623, 106624, 106625, 106626, 106627, 106628, 106629,
                 106630, 106631],
                dtype='int64', length=8886),
     'huairou_aq': Int64Index([106632, 106633, 106634, 106635, 106636, 106637, 106638, 106639,
                 106640, 106641,
                 ...
                 115508, 115509, 115510, 115511, 115512, 115513, 115514, 115515,
                 115516, 115517],
                dtype='int64', length=8886),
     'liulihe_aq': Int64Index([115518, 115519, 115520, 115521, 115522, 115523, 115524, 115525,
                 115526, 115527,
                 ...
                 124394, 124395, 124396, 124397, 124398, 124399, 124400, 124401,
                 124402, 124403],
                dtype='int64', length=8886),
     'mentougou_aq': Int64Index([124404, 124405, 124406, 124407, 124408, 124409, 124410, 124411,
                 124412, 124413,
                 ...
                 133280, 133281, 133282, 133283, 133284, 133285, 133286, 133287,
                 133288, 133289],
                dtype='int64', length=8886),
     'miyun_aq': Int64Index([133290, 133291, 133292, 133293, 133294, 133295, 133296, 133297,
                 133298, 133299,
                 ...
                 142166, 142167, 142168, 142169, 142170, 142171, 142172, 142173,
                 142174, 142175],
                dtype='int64', length=8886),
     'miyunshuiku_aq': Int64Index([142176, 142177, 142178, 142179, 142180, 142181, 142182, 142183,
                 142184, 142185,
                 ...
                 151052, 151053, 151054, 151055, 151056, 151057, 151058, 151059,
                 151060, 151061],
                dtype='int64', length=8886),
     'nansanhuan_aq': Int64Index([151062, 151063, 151064, 151065, 151066, 151067, 151068, 151069,
                 151070, 151071,
                 ...
                 159938, 159939, 159940, 159941, 159942, 159943, 159944, 159945,
                 159946, 159947],
                dtype='int64', length=8886),
     'nongzhanguan_aq': Int64Index([159948, 159949, 159950, 159951, 159952, 159953, 159954, 159955,
                 159956, 159957,
                 ...
                 168824, 168825, 168826, 168827, 168828, 168829, 168830, 168831,
                 168832, 168833],
                dtype='int64', length=8886),
     'pingchang_aq': Int64Index([168834, 168835, 168836, 168837, 168838, 168839, 168840, 168841,
                 168842, 168843,
                 ...
                 177710, 177711, 177712, 177713, 177714, 177715, 177716, 177717,
                 177718, 177719],
                dtype='int64', length=8886),
     'pinggu_aq': Int64Index([177720, 177721, 177722, 177723, 177724, 177725, 177726, 177727,
                 177728, 177729,
                 ...
                 186596, 186597, 186598, 186599, 186600, 186601, 186602, 186603,
                 186604, 186605],
                dtype='int64', length=8886),
     'qianmen_aq': Int64Index([186606, 186607, 186608, 186609, 186610, 186611, 186612, 186613,
                 186614, 186615,
                 ...
                 195482, 195483, 195484, 195485, 195486, 195487, 195488, 195489,
                 195490, 195491],
                dtype='int64', length=8886),
     'shunyi_aq': Int64Index([195492, 195493, 195494, 195495, 195496, 195497, 195498, 195499,
                 195500, 195501,
                 ...
                 204368, 204369, 204370, 204371, 204372, 204373, 204374, 204375,
                 204376, 204377],
                dtype='int64', length=8886),
     'tiantan_aq': Int64Index([204378, 204379, 204380, 204381, 204382, 204383, 204384, 204385,
                 204386, 204387,
                 ...
                 213254, 213255, 213256, 213257, 213258, 213259, 213260, 213261,
                 213262, 213263],
                dtype='int64', length=8886),
     'tongzhou_aq': Int64Index([213264, 213265, 213266, 213267, 213268, 213269, 213270, 213271,
                 213272, 213273,
                 ...
                 222140, 222141, 222142, 222143, 222144, 222145, 222146, 222147,
                 222148, 222149],
                dtype='int64', length=8886),
     'wanliu_aq': Int64Index([222150, 222151, 222152, 222153, 222154, 222155, 222156, 222157,
                 222158, 222159,
                 ...
                 231026, 231027, 231028, 231029, 231030, 231031, 231032, 231033,
                 231034, 231035],
                dtype='int64', length=8886),
     'wanshouxigong_aq': Int64Index([231036, 231037, 231038, 231039, 231040, 231041, 231042, 231043,
                 231044, 231045,
                 ...
                 239912, 239913, 239914, 239915, 239916, 239917, 239918, 239919,
                 239920, 239921],
                dtype='int64', length=8886),
     'xizhimenbei_aq': Int64Index([239922, 239923, 239924, 239925, 239926, 239927, 239928, 239929,
                 239930, 239931,
                 ...
                 248798, 248799, 248800, 248801, 248802, 248803, 248804, 248805,
                 248806, 248807],
                dtype='int64', length=8886),
     'yanqin_aq': Int64Index([248808, 248809, 248810, 248811, 248812, 248813, 248814, 248815,
                 248816, 248817,
                 ...
                 257684, 257685, 257686, 257687, 257688, 257689, 257690, 257691,
                 257692, 257693],
                dtype='int64', length=8886),
     'yizhuang_aq': Int64Index([257694, 257695, 257696, 257697, 257698, 257699, 257700, 257701,
                 257702, 257703,
                 ...
                 266570, 266571, 266572, 266573, 266574, 266575, 266576, 266577,
                 266578, 266579],
                dtype='int64', length=8886),
     'yongdingmennei_aq': Int64Index([266580, 266581, 266582, 266583, 266584, 266585, 266586, 266587,
                 266588, 266589,
                 ...
                 275456, 275457, 275458, 275459, 275460, 275461, 275462, 275463,
                 275464, 275465],
                dtype='int64', length=8886),
     'yongledian_aq': Int64Index([275466, 275467, 275468, 275469, 275470, 275471, 275472, 275473,
                 275474, 275475,
                 ...
                 284342, 284343, 284344, 284345, 284346, 284347, 284348, 284349,
                 284350, 284351],
                dtype='int64', length=8886),
     'yufa_aq': Int64Index([284352, 284353, 284354, 284355, 284356, 284357, 284358, 284359,
                 284360, 284361,
                 ...
                 293228, 293229, 293230, 293231, 293232, 293233, 293234, 293235,
                 293236, 293237],
                dtype='int64', length=8886),
     'yungang_aq': Int64Index([293238, 293239, 293240, 293241, 293242, 293243, 293244, 293245,
                 293246, 293247,
                 ...
                 302114, 302115, 302116, 302117, 302118, 302119, 302120, 302121,
                 302122, 302123],
                dtype='int64', length=8886),
     'zhiwuyuan_aq': Int64Index([302124, 302125, 302126, 302127, 302128, 302129, 302130, 302131,
                 302132, 302133,
                 ...
                 311000, 311001, 311002, 311003, 311004, 311005, 311006, 311007,
                 311008, 311009],
                dtype='int64', length=8886)}




```python
beijingAqCsv_sta = pd.read_csv('Beijing_AirQuality_Stations.csv')
```


```python
beijingAqCsv_sta
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Pollutant Species</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>type</td>
      <td>Unit</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PM2.5</td>
      <td>µg/m3 (microgram/cubic meter)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PM10</td>
      <td>µg/m3 (microgram/cubic meter)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>SO2</td>
      <td>µg/m3 (microgram/cubic meter)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NO2</td>
      <td>µg/m3 (microgram/cubic meter)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>O3</td>
      <td>µg/m3 (microgram/cubic meter)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>CO</td>
      <td>µg/m3 (microgram/cubic meter)</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Stations at Beijing</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Station ID</td>
      <td>longitude</td>
      <td>latitude</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Urban Stations</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>dongsi_aq</td>
      <td>116.417</td>
      <td>39.929</td>
    </tr>
    <tr>
      <th>12</th>
      <td>tiantan_aq</td>
      <td>116.407</td>
      <td>39.886</td>
    </tr>
    <tr>
      <th>13</th>
      <td>guanyuan_aq</td>
      <td>116.339</td>
      <td>39.929</td>
    </tr>
    <tr>
      <th>14</th>
      <td>wanshouxigong_aq</td>
      <td>116.352</td>
      <td>39.878</td>
    </tr>
    <tr>
      <th>15</th>
      <td>aotizhongxin_aq</td>
      <td>116.397</td>
      <td>39.982</td>
    </tr>
    <tr>
      <th>16</th>
      <td>nongzhanguan_aq</td>
      <td>116.461</td>
      <td>39.937</td>
    </tr>
    <tr>
      <th>17</th>
      <td>wanliu_aq</td>
      <td>116.287</td>
      <td>39.987</td>
    </tr>
    <tr>
      <th>18</th>
      <td>beibuxinqu_aq</td>
      <td>116.174</td>
      <td>40.09</td>
    </tr>
    <tr>
      <th>19</th>
      <td>zhiwuyuan_aq</td>
      <td>116.207</td>
      <td>40.002</td>
    </tr>
    <tr>
      <th>20</th>
      <td>fengtaihuayuan_aq</td>
      <td>116.279</td>
      <td>39.863</td>
    </tr>
    <tr>
      <th>21</th>
      <td>yungang_aq</td>
      <td>116.146</td>
      <td>39.824</td>
    </tr>
    <tr>
      <th>22</th>
      <td>gucheng_aq</td>
      <td>116.184</td>
      <td>39.914</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Suburban Stations</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>fangshan_aq</td>
      <td>116.136</td>
      <td>39.742</td>
    </tr>
    <tr>
      <th>26</th>
      <td>daxing_aq</td>
      <td>116.404</td>
      <td>39.718</td>
    </tr>
    <tr>
      <th>27</th>
      <td>yizhuang_aq</td>
      <td>116.506</td>
      <td>39.795</td>
    </tr>
    <tr>
      <th>28</th>
      <td>tongzhou_aq</td>
      <td>116.663</td>
      <td>39.886</td>
    </tr>
    <tr>
      <th>29</th>
      <td>shunyi_aq</td>
      <td>116.655</td>
      <td>40.127</td>
    </tr>
    <tr>
      <th>30</th>
      <td>pingchang_aq</td>
      <td>116.23</td>
      <td>40.217</td>
    </tr>
    <tr>
      <th>31</th>
      <td>mentougou_aq</td>
      <td>116.106</td>
      <td>39.937</td>
    </tr>
    <tr>
      <th>32</th>
      <td>pinggu_aq</td>
      <td>117.1</td>
      <td>40.143</td>
    </tr>
    <tr>
      <th>33</th>
      <td>huairou_aq</td>
      <td>116.628</td>
      <td>40.328</td>
    </tr>
    <tr>
      <th>34</th>
      <td>miyun_aq</td>
      <td>116.832</td>
      <td>40.37</td>
    </tr>
    <tr>
      <th>35</th>
      <td>yanqin_aq</td>
      <td>115.972</td>
      <td>40.453</td>
    </tr>
    <tr>
      <th>36</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Other Stations</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38</th>
      <td>dingling_aq</td>
      <td>116.22</td>
      <td>40.292</td>
    </tr>
    <tr>
      <th>39</th>
      <td>badaling_aq</td>
      <td>115.988</td>
      <td>40.365</td>
    </tr>
    <tr>
      <th>40</th>
      <td>miyunshuiku_aq</td>
      <td>116.911</td>
      <td>40.499</td>
    </tr>
    <tr>
      <th>41</th>
      <td>donggaocun_aq</td>
      <td>117.12</td>
      <td>40.1</td>
    </tr>
    <tr>
      <th>42</th>
      <td>yongledian_aq</td>
      <td>116.783</td>
      <td>39.712</td>
    </tr>
    <tr>
      <th>43</th>
      <td>yufa_aq</td>
      <td>116.3</td>
      <td>39.52</td>
    </tr>
    <tr>
      <th>44</th>
      <td>liulihe_aq</td>
      <td>116</td>
      <td>39.58</td>
    </tr>
    <tr>
      <th>45</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Stations Near Traffic</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>47</th>
      <td>qianmen_aq</td>
      <td>116.395</td>
      <td>39.899</td>
    </tr>
    <tr>
      <th>48</th>
      <td>yongdingmennei_aq</td>
      <td>116.394</td>
      <td>39.876</td>
    </tr>
    <tr>
      <th>49</th>
      <td>xizhimenbei_aq</td>
      <td>116.349</td>
      <td>39.954</td>
    </tr>
    <tr>
      <th>50</th>
      <td>nansanhuan_aq</td>
      <td>116.368</td>
      <td>39.856</td>
    </tr>
    <tr>
      <th>51</th>
      <td>dongsihuan_aq</td>
      <td>116.483</td>
      <td>39.939</td>
    </tr>
  </tbody>
</table>
</div>




```python
import folium
```


```python
list(air_station_beij.groups.keys())
```




    ['gucheng_aq',
     'mentougou_aq',
     'yizhuang_aq',
     'nongzhanguan_aq',
     'qianmen_aq',
     'tiantan_aq',
     'aotizhongxin_aq',
     'dingling_aq',
     'liulihe_aq',
     'fengtaihuayuan_aq',
     'yungang_aq',
     'yanqin_aq',
     'daxing_aq',
     'donggaocun_aq',
     'dongsi_aq',
     'miyunshuiku_aq',
     'huairou_aq',
     'pingchang_aq',
     'yufa_aq',
     'pinggu_aq',
     'guanyuan_aq',
     'dongsihuan_aq',
     'beibuxinqu_aq',
     'wanliu_aq',
     'miyun_aq',
     'badaling_aq',
     'nansanhuan_aq',
     'shunyi_aq',
     'fangshan_aq',
     'tongzhou_aq',
     'wanshouxigong_aq',
     'xizhimenbei_aq',
     'yongledian_aq',
     'zhiwuyuan_aq',
     'yongdingmennei_aq']




```python
location_beji={}
```


```python
for i in range(0,len(beijingAqCsv_sta)):
    temp=beijingAqCsv_sta.iloc[i,:]
    if temp['Pollutant Species'] in list(air_station_beij.groups.keys()):
       location_beji[temp['Pollutant Species']]=temp.values[1:].astype(float).tolist()[::-1]
```


```python
location_beji
```




    {'aotizhongxin_aq': [39.982, 116.397],
     'badaling_aq': [40.365, 115.988],
     'beibuxinqu_aq': [40.09, 116.174],
     'daxing_aq': [39.718, 116.404],
     'dingling_aq': [40.292, 116.22],
     'donggaocun_aq': [40.1, 117.12],
     'dongsi_aq': [39.929, 116.417],
     'dongsihuan_aq': [39.939, 116.483],
     'fangshan_aq': [39.742, 116.136],
     'fengtaihuayuan_aq': [39.863, 116.279],
     'guanyuan_aq': [39.929, 116.339],
     'gucheng_aq': [39.914, 116.184],
     'huairou_aq': [40.328, 116.628],
     'liulihe_aq': [39.58, 116.0],
     'mentougou_aq': [39.937, 116.106],
     'miyun_aq': [40.37, 116.832],
     'miyunshuiku_aq': [40.499, 116.911],
     'nansanhuan_aq': [39.856, 116.368],
     'nongzhanguan_aq': [39.937, 116.461],
     'pingchang_aq': [40.217, 116.23],
     'pinggu_aq': [40.143, 117.1],
     'qianmen_aq': [39.899, 116.395],
     'shunyi_aq': [40.127, 116.655],
     'tiantan_aq': [39.886, 116.407],
     'tongzhou_aq': [39.886, 116.663],
     'wanliu_aq': [39.987, 116.287],
     'wanshouxigong_aq': [39.878, 116.352],
     'xizhimenbei_aq': [39.954, 116.349],
     'yanqin_aq': [40.453, 115.972],
     'yizhuang_aq': [39.795, 116.506],
     'yongdingmennei_aq': [39.876, 116.394],
     'yongledian_aq': [39.712, 116.783],
     'yufa_aq': [39.52, 116.3],
     'yungang_aq': [39.824, 116.146],
     'zhiwuyuan_aq': [40.002, 116.207]}




```python
#del temp
temp=beijingAqCsv_sta.loc[beijingAqCsv_sta['Pollutant Species']==list(air_station_beij.groups.keys())[0]].iloc[:,1:].values[0]

```


```python
temp=temp.astype(float).tolist()
```


```python
temp=temp[::-1]
```


```python
map_1 = folium.Map(location=temp, zoom_start=9)
```


```python
for key in location_beji:
    folium.Marker(location=location[key]).add_to(map_1)
map_1
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIgLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC5taW4uY3NzIiAvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiIC8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIgLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuY3NzIiAvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2dpdC5jb20vcHl0aG9uLXZpc3VhbGl6YXRpb24vZm9saXVtL21hc3Rlci9mb2xpdW0vdGVtcGxhdGVzL2xlYWZsZXQuYXdlc29tZS5yb3RhdGUuY3NzIiAvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfYTVkMmMxZjI0ZGZkNDIwMjhlZjYyNDk1YWM1OTgwMGIgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYiA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYicsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbMzkuOTE0LDExNi4xODRdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogOSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1heEJvdW5kczogYm91bmRzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF5ZXJzOiBbXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTsKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfY2M5ZmMzZWVhYmVjNDI0OTlhZDI1Zjk5YWVmZGUyNDEgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgICAgICAgICB7CiAgImF0dHJpYnV0aW9uIjogbnVsbCwKICAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsCiAgIm1heFpvb20iOiAxOCwKICAibWluWm9vbSI6IDEsCiAgIm5vV3JhcCI6IGZhbHNlLAogICJzdWJkb21haW5zIjogImFiYyIKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTVkMmMxZjI0ZGZkNDIwMjhlZjYyNDk1YWM1OTgwMGIpOwogICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzg2YWJmMDY2OTE5ODRjNjhhNGYzNDg3NWEwODA3NjQyID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuOTU0LDExNi4zNDldLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzU2ZjRjNDk0YjFhYTQ2YWM4OGM2MTRhZTI5OTZiYTQ2ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuOTg3LDExNi4yODddLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2Y2YmM5YjNiMzU2NDRjNmI5ZWI4ODkzYmZlNmE0Y2RlID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuNzk1LDExNi41MDZdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2E2ZmMzNmZjNjcyNzQyMDZhZGRiZmQ5NjNhOTFkNTI5ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuOTM3LDExNi40NjFdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzU3Mzk1NjkzNTliNTRiMGQ5MThjM2VhNTY1YTZhYTUyID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuNTIsMTE2LjNdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2UzYzc2Y2IyY2U3NTRmNDc5ZDUyNGFjZmZjMmU2Yzc3ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuMSwxMTcuMTJdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2YzOGZlNWJmOTdhMzQ3ZDNiYTI4MTljYzZlZjE2ZTdmID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuODg2LDExNi40MDddLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzYxMDE4NzUwNzhlMjRlZThiYTBhOWQ4OTk0ZmQ4ODMzID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuMDAyLDExNi4yMDddLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzJkNTdmZTg1MTdkZTQ0MDhiNTU0NjA5ODdhZWVjY2Q5ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuOTgyLDExNi4zOTddLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzUwZjhmYWRiZTFlMTQzOTk4YzNkYmUxNGViNjY3Y2U2ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuMjkyLDExNi4yMl0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfZTUyNjIwNTgwMWMyNDdlNmFmOGUyNjcxMGYyZmM2ZTIgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS41OCwxMTYuMF0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfNGEwOWU0MGJmNGE0NGUzMGEwNTIzN2Y4ODgxYzc3NjYgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS44NjMsMTE2LjI3OV0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfYThhNGFkZWNkZWViNDhiY2JjMTQ0NmE4ZjVlMmIxYTMgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS44MjQsMTE2LjE0Nl0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfNWQwNGNlMzQwOWU2NGM1ZTlmODg1ZmIyMzk5ZTUwNmEgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC40NTMsMTE1Ljk3Ml0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfNWE1ZmFmYTkwYjg3NGQzYTkxNWJlOTI4ZmY4OTE2ODQgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS43MTgsMTE2LjQwNF0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfZjkyYmIzOTdhNjZhNDI1YTk2OWIxYjExNzJkY2Y0MGIgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS45MjksMTE2LjQxN10sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfYmUyZmM5NzJjNWZmNGRlM2JhOTkwYzQ0OTVjOGRiMDYgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS45MzcsMTE2LjEwNl0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfYmEwYzgzMDg1Y2Q2NDQ0NmI3OWY4NTAxZTI5ZmM3NGIgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC4zMjgsMTE2LjYyOF0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfNDdlMjViZWNlMGY1NDk0M2I3MTU2N2M5ODE2Y2YyZDUgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS44NTYsMTE2LjM2OF0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfMjI1NzBhYWI0ZDhlNDNlZmFlM2VkNmFiMmY4NDdhOGYgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC4yMTcsMTE2LjIzXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfYTVkMmMxZjI0ZGZkNDIwMjhlZjYyNDk1YWM1OTgwMGIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9lMzgwMmY4MzlmMTc0NTQ0YThkN2I4MjA1YWU4NjMyOSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjE0MywxMTcuMV0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfYjMwMzRkYzY0MDk1NGEyY2JkNWYyMmNkMzU4NDA3MjMgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS45MjksMTE2LjMzOV0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfMWMwYWYwMjlkN2E1NDcwMTkzNjc2MTBkNjE0YzQ1MDYgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS45MzksMTE2LjQ4M10sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwX2E1ZDJjMWYyNGRmZDQyMDI4ZWY2MjQ5NWFjNTk4MDBiKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfYzQyNzNlZjRmMDFhNDFmMWEyMmEyOGE5YmM4ODAyNWIgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC4wOSwxMTYuMTc0XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfYTVkMmMxZjI0ZGZkNDIwMjhlZjYyNDk1YWM1OTgwMGIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl8xN2EyMzlmYjM3M2Q0Njk0OTI2ZTMyYTVkNGU2ZjRlZCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzM5Ljg4NiwxMTYuNjYzXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfYTVkMmMxZjI0ZGZkNDIwMjhlZjYyNDk1YWM1OTgwMGIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl83ZTZkMjg0ZTI2Mzg0NTM0OTA0ODMwMDExM2YyYTg5NiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjM2NSwxMTUuOTg4XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfYTVkMmMxZjI0ZGZkNDIwMjhlZjYyNDk1YWM1OTgwMGIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl8wMjZjYTU2ZGRjYTE0NDJmYTliNjRkZDRkZjU0ODBkNCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjEyNywxMTYuNjU1XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfYTVkMmMxZjI0ZGZkNDIwMjhlZjYyNDk1YWM1OTgwMGIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl82Mjg2YWRlOTZkYzM0NmVkODFlMjdhOWVkNWNkNDk1MiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzM5Ljg3OCwxMTYuMzUyXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfYTVkMmMxZjI0ZGZkNDIwMjhlZjYyNDk1YWM1OTgwMGIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl8zY2Y1YzYyODAxOTg0YzA5YjIyMTQ0MGViOTY4NmNjMiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjQ5OSwxMTYuOTExXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfYTVkMmMxZjI0ZGZkNDIwMjhlZjYyNDk1YWM1OTgwMGIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl80ZDJhNDRiNGJiYWI0YTM1OTI1YjA4NTIyNTBlMzBjMCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjM3LDExNi44MzJdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzgyNWEzYmE4ZmMxMjQxYTJhZGUyZjZhY2Q3ZWExZTQ5ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuNzQyLDExNi4xMzZdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2U5MjJlMWZjYjExNDRlMTE5ZDhiNGVhOTBiNWE5NTMzID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuNzEyLDExNi43ODNdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2IyYTk4NzM5NzM4ZjRkZjBiYjc0YjJmMWE3NjgxNTY5ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuODk5LDExNi4zOTVdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2E1MjhkMGJjMGQ4ZjQwNzc4Nzg0MzhiOWMyOWU2OGU4ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuOTE0LDExNi4xODRdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2FjOTU4MmQwMjU5ZjQxY2ZhNTAwNzFkZTI4MTUwOTM2ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuODc2LDExNi4zOTRdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF9hNWQyYzFmMjRkZmQ0MjAyOGVmNjI0OTVhYzU5ODAwYik7CiAgICAgICAgICAgIAo8L3NjcmlwdD4=" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
temp=beijingAqCsv_sta.loc[beijingAqCsv_sta['Pollutant Species']==list(air_station_beij.groups.keys())[0]].iloc[:,1:].values[0]
temp=temp.astype(float).tolist()
temp=temp[::-1]
map_1 = folium.Map(location=temp, zoom_start=9,tiles='Stamen Terrain')
for key in location:
    folium.Marker(location=location[key]).add_to(map_1)
map_1
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIgLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC5taW4uY3NzIiAvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiIC8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIgLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuY3NzIiAvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2dpdC5jb20vcHl0aG9uLXZpc3VhbGl6YXRpb24vZm9saXVtL21hc3Rlci9mb2xpdW0vdGVtcGxhdGVzL2xlYWZsZXQuYXdlc29tZS5yb3RhdGUuY3NzIiAvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfOTUyNTY2YzQ3NDVlNGZmNzg3MDIzY2NkYzk2NTM4ZDIgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMiA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMicsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbMzkuOTE0LDExNi4xODRdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogOSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1heEJvdW5kczogYm91bmRzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF5ZXJzOiBbXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTsKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfMGNmM2QyMmZiYTJkNDRmYTk0NzA2ZjRjZDlkNmQ0ODkgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3N0YW1lbi10aWxlcy17c30uYS5zc2wuZmFzdGx5Lm5ldC90ZXJyYWluL3t6fS97eH0ve3l9LmpwZycsCiAgICAgICAgICAgICAgICB7CiAgImF0dHJpYnV0aW9uIjogbnVsbCwKICAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsCiAgIm1heFpvb20iOiAxOCwKICAibWluWm9vbSI6IDEsCiAgIm5vV3JhcCI6IGZhbHNlLAogICJzdWJkb21haW5zIjogImFiYyIKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTUyNTY2YzQ3NDVlNGZmNzg3MDIzY2NkYzk2NTM4ZDIpOwogICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzVhNTI4ZWIxYmFkYzQ0M2ViOGMyYTA4OTIyN2M3ZDIwID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuOTU0LDExNi4zNDldLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2NhMjk4YTY3MWQzZDQ2ZDZiMWQxZDQ2YjdlZGZlY2Y0ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuOTg3LDExNi4yODddLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzFkNTk1MWU4YjVkYjQ1OGFhYzE3ZDBmMGI2ZjdhNTk4ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuNzk1LDExNi41MDZdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzlmN2VmZjVmYjM3ZjRlOWE5YjcyNTFjZTllZmExMmFhID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuOTM3LDExNi40NjFdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2UwYzYyYTJmZWM1NjQyZmU4NmYzZWRiMTlhNzAzNGYzID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuNTIsMTE2LjNdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2I4YjE0MTU1ZTg2ZDQ3ZGE4ZGUxMGIyN2ZiYjkzN2FiID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuMSwxMTcuMTJdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzg3OGVmZjgyMzA1NjQ0OWY5NDVkYjcwMjk3NGQwYzZkID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuODg2LDExNi40MDddLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2JjNmE0MGIyYmI2YTQyOTA4NDBjNWUxNDEzN2UxMzA3ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuMDAyLDExNi4yMDddLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzFmYWMwZGI5ZmVmZjRkYmM4MGFmYjJjZDE4YjlhNjUwID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuOTgyLDExNi4zOTddLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzg2NTA3MGNhYzFhMjQ0OTU4YmYwZjJiNTE3NmJlYjAzID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuMjkyLDExNi4yMl0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfODFlYjU4YmZkOTIxNGRjZTgwOTgzZWU4MmM1ZDM1NTQgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS41OCwxMTYuMF0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfM2FlNjJhODZjMzZkNGY1MTgxMmNmN2M5MDllMDllZTcgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS44NjMsMTE2LjI3OV0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfZDU5ZWNiNTM5NTEyNDY4NmE0M2ViZDk3NTc3NTNmNDIgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS44MjQsMTE2LjE0Nl0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfNTMyZmVkYjc1ZDA4NGRmZTllMTk4ZWZlMjI0YzYxMTMgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC40NTMsMTE1Ljk3Ml0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfNDlkYzUwNDhiYmIwNDY0NGI2OTVlM2IzMzFjYWI2MzcgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS43MTgsMTE2LjQwNF0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfODQwZmIzYWEzNjUzNGVjZmJhNjA5Y2JkNzk0YTE5ZjYgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS45MjksMTE2LjQxN10sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfNmUzNzhkODE3ZTc3NDAyZWE0OWEzOTkwMWQ5MzgyNmUgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS45MzcsMTE2LjEwNl0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfZGRkOWY4ZGY5NGFiNDgxYzkxM2ZlM2Y4ZDQ0MzQ3Y2MgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC4zMjgsMTE2LjYyOF0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfZTIyMzc5OTRjZjUzNGRmMjhlMmVhM2UyMGQ3MWEwMWQgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS44NTYsMTE2LjM2OF0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfZjRjODZjZTZmZGE1NDkxZThhOThiZjYzNmQ0NTE0MmYgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC4yMTcsMTE2LjIzXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfOTUyNTY2YzQ3NDVlNGZmNzg3MDIzY2NkYzk2NTM4ZDIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9iZTYxOTFjOWQ2NWQ0YWU1ODkyOGJjMjA3MDJjMTNhOCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjE0MywxMTcuMV0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfMGUyMzI2OGQ3YWFmNDAxODk4MmU4YTJmZDM2YzFhZTggPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS45MjksMTE2LjMzOV0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfZmRhM2M0ODIwMGJjNGNlZmI4NTU3MGM2MzFlNzhlODkgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszOS45MzksMTE2LjQ4M10sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzk1MjU2NmM0NzQ1ZTRmZjc4NzAyM2NjZGM5NjUzOGQyKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfYjAyODc5ZDkzNGI3NDNmYTlhY2ZhODRjOGEwOGRkMzggPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC4wOSwxMTYuMTc0XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfOTUyNTY2YzQ3NDVlNGZmNzg3MDIzY2NkYzk2NTM4ZDIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9iYjlkMGY1ZGEzODI0NjE0ODMzNTBjNDc2ZTBiYTAxMCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzM5Ljg4NiwxMTYuNjYzXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfOTUyNTY2YzQ3NDVlNGZmNzg3MDIzY2NkYzk2NTM4ZDIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl82MDRiYzRkMzEyNWI0YTkxYmNjNzE3MmI4NmRmM2U0ZCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjM2NSwxMTUuOTg4XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfOTUyNTY2YzQ3NDVlNGZmNzg3MDIzY2NkYzk2NTM4ZDIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9jZmVhZDQwYTQwYzQ0MTlkYWI5YTcyMDg0ZDIxNjkzZCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjEyNywxMTYuNjU1XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfOTUyNTY2YzQ3NDVlNGZmNzg3MDIzY2NkYzk2NTM4ZDIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl82NTc0MTcwOTBhMzA0NGI5YTFjMGNmNWMxZTY5ZTc2MyA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzM5Ljg3OCwxMTYuMzUyXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfOTUyNTY2YzQ3NDVlNGZmNzg3MDIzY2NkYzk2NTM4ZDIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl82YTc0ZDczMTZkMDA0ZDYyYjExZjdiY2RiZjYwMjc3OSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjQ5OSwxMTYuOTExXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfOTUyNTY2YzQ3NDVlNGZmNzg3MDIzY2NkYzk2NTM4ZDIpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl84MDE3MGE5ZjAxNDM0MWIxOGJlZmNlNmUzYTEzYmU0NiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjM3LDExNi44MzJdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzZiNmViOGI0ODg4ZDQ2MTk4YmQyOTM2NDZmMzBkMzU5ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuNzQyLDExNi4xMzZdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2ZhZmYxNDA3Y2E5MzQxZmU5NmJjZmI4Y2QyODFjOTI2ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuNzEyLDExNi43ODNdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzMwZGIwY2M1YzkxZDRkYTlhMTdlMDNkMWJlMTE1NWY4ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuODk5LDExNi4zOTVdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzcwY2M2MzA1MTAwMDQ0OThhNzc2NDA3MzIwMTViM2M1ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuOTE0LDExNi4xODRdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzQ4YWMzMWZhMDQ2ZjQ0OTlhNWVlYjQzODZiOTQwOTY5ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzkuODc2LDExNi4zOTRdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF85NTI1NjZjNDc0NWU0ZmY3ODcwMjNjY2RjOTY1MzhkMik7CiAgICAgICAgICAgIAo8L3NjcmlwdD4=" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



### The station in London


```python
LondonAqCsv_sta = pd.read_csv(path+'London_AirQuality_Stations.csv')
```


```python
LondonAqCsv_sta
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>api_data</th>
      <th>need_prediction</th>
      <th>historical_data</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>SiteType</th>
      <th>SiteName</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BX9</td>
      <td>True</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.465983</td>
      <td>0.184877</td>
      <td>Suburban</td>
      <td>Bexley - Slade Green FDMS</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BX1</td>
      <td>True</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.465983</td>
      <td>0.184877</td>
      <td>Suburban</td>
      <td>Bexley - Slade Green</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BL0</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.522287</td>
      <td>-0.125848</td>
      <td>Urban Background</td>
      <td>Camden - Bloomsbury</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CD9</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.527707</td>
      <td>-0.129053</td>
      <td>Roadside</td>
      <td>Camden - Euston Road</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CD1</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.544219</td>
      <td>-0.175284</td>
      <td>Kerbside</td>
      <td>Camden - Swiss Cottage</td>
    </tr>
    <tr>
      <th>5</th>
      <td>CT2</td>
      <td>True</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.514525</td>
      <td>-0.104516</td>
      <td>Kerbside</td>
      <td>City of London - Farringdon Street</td>
    </tr>
    <tr>
      <th>6</th>
      <td>CT3</td>
      <td>True</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.513847</td>
      <td>-0.077766</td>
      <td>Urban Background</td>
      <td>City of London - Sir John Cass School</td>
    </tr>
    <tr>
      <th>7</th>
      <td>CR8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.410039</td>
      <td>-0.127523</td>
      <td>Urban Background</td>
      <td>Croydon - Norbury Manor</td>
    </tr>
    <tr>
      <th>8</th>
      <td>GN0</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.490532</td>
      <td>0.074003</td>
      <td>Roadside</td>
      <td>Greenwich - A206 Burrage Grove</td>
    </tr>
    <tr>
      <th>9</th>
      <td>GR4</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.452580</td>
      <td>0.070766</td>
      <td>Suburban</td>
      <td>Greenwich - Eltham</td>
    </tr>
    <tr>
      <th>10</th>
      <td>GN3</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.486957</td>
      <td>0.095111</td>
      <td>Roadside</td>
      <td>Greenwich - Plumstead High Street</td>
    </tr>
    <tr>
      <th>11</th>
      <td>GR9</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.456357</td>
      <td>0.040725</td>
      <td>Roadside</td>
      <td>Greenwich - Westhorne Avenue</td>
    </tr>
    <tr>
      <th>12</th>
      <td>GB0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.456300</td>
      <td>0.085606</td>
      <td>Roadside</td>
      <td>Greenwich and Bexley - Falconwood FDMS</td>
    </tr>
    <tr>
      <th>13</th>
      <td>HR1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.617327</td>
      <td>-0.298775</td>
      <td>Urban Background</td>
      <td>Harrow - Stanmore</td>
    </tr>
    <tr>
      <th>14</th>
      <td>HV1</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.520787</td>
      <td>0.205461</td>
      <td>Roadside</td>
      <td>Havering - Rainham</td>
    </tr>
    <tr>
      <th>15</th>
      <td>LH0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.488780</td>
      <td>-0.441627</td>
      <td>Urban Background</td>
      <td>Hillingdon - Harlington</td>
    </tr>
    <tr>
      <th>16</th>
      <td>KC1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.521047</td>
      <td>-0.213492</td>
      <td>Urban Background</td>
      <td>Kensington and Chelsea - North Ken</td>
    </tr>
    <tr>
      <th>17</th>
      <td>KF1</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.521047</td>
      <td>-0.213492</td>
      <td>Urban Background</td>
      <td>Kensington and Chelsea - North Ken FIDAS</td>
    </tr>
    <tr>
      <th>18</th>
      <td>LW2</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.474954</td>
      <td>-0.039641</td>
      <td>Roadside</td>
      <td>Lewisham - New Cross</td>
    </tr>
    <tr>
      <th>19</th>
      <td>RB7</td>
      <td>True</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.569484</td>
      <td>0.082907</td>
      <td>Urban Background</td>
      <td>Redbridge - Ley Street</td>
    </tr>
    <tr>
      <th>20</th>
      <td>TD5</td>
      <td>True</td>
      <td>NaN</td>
      <td>True</td>
      <td>51.425256</td>
      <td>-0.345608</td>
      <td>Suburban</td>
      <td>Richmond Upon Thames - Bushy Park</td>
    </tr>
    <tr>
      <th>21</th>
      <td>ST5</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.389287</td>
      <td>-0.141662</td>
      <td>Industrial</td>
      <td>Sutton - Beddington Lane north</td>
    </tr>
    <tr>
      <th>22</th>
      <td>TH4</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.515046</td>
      <td>-0.008418</td>
      <td>Roadside</td>
      <td>Tower Hamlets - Blackwall</td>
    </tr>
    <tr>
      <th>23</th>
      <td>MY7</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>51.522540</td>
      <td>-0.154590</td>
      <td>Kerbside</td>
      <td>Westminster - Marylebone Road FDMS</td>
    </tr>
  </tbody>
</table>
</div>




```python
location_Lodon={}
for i in range(0,len(LondonAqCsv_sta)):
    temp_name=LondonAqCsv_sta['Unnamed: 0'].iloc[i]
    temp_Latitude=LondonAqCsv_sta['Latitude'].iloc[i]
    temp_Longitude=LondonAqCsv_sta['Longitude'].iloc[i]
    location_Lodon[temp_name]=[temp_Latitude,temp_Longitude]
```


```python
location_Lodon
```




    {'BL0': [51.522287, -0.12584800000000002],
     'BX1': [51.46598327, 0.184877127],
     'BX9': [51.46598327, 0.184877127],
     'CD1': [51.544219, -0.175284],
     'CD9': [51.52770662, -0.129053205],
     'CR8': [51.410039000000005, -0.127523],
     'CT2': [51.51452534, -0.104515626],
     'CT3': [51.51384718, -0.077765682],
     'GB0': [51.4563, 0.08560599999999999],
     'GN0': [51.490532, 0.074003],
     'GN3': [51.486957000000004, 0.095111],
     'GR4': [51.45258, 0.070766],
     'GR9': [51.456357000000004, 0.040725],
     'HR1': [51.617327, -0.298775],
     'HV1': [51.52078746, 0.20546070600000002],
     'KC1': [51.52104675, -0.21349214],
     'KF1': [51.52104675, -0.21349214],
     'LH0': [51.48878, -0.44162700000000005],
     'LW2': [51.474954, -0.039641],
     'MY7': [51.52254, -0.15459],
     'RB7': [51.56948433, 0.082907475],
     'ST5': [51.3892869, -0.141661525],
     'TD5': [51.42525604, -0.345608291],
     'TH4': [51.51504617, -0.008418493]}




```python
#del temp
col_list=['Latitude','Longitude']
temp_pd=LondonAqCsv_sta[col_list]

```


```python
temp_pd.iloc[0].values.tolist()
```




    [51.46598327, 0.184877127]




```python
map_2 = folium.Map(location=temp_pd.iloc[0].values.tolist(), zoom_start=9)
```


```python
for key in location_Lodon:
    folium.Marker(location=location_Lodon[key]).add_to(map_2)
map_2
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIgLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC5taW4uY3NzIiAvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiIC8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIgLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuY3NzIiAvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2dpdC5jb20vcHl0aG9uLXZpc3VhbGl6YXRpb24vZm9saXVtL21hc3Rlci9mb2xpdW0vdGVtcGxhdGVzL2xlYWZsZXQuYXdlc29tZS5yb3RhdGUuY3NzIiAvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTAgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzBjNWM4MWIyNjVmNDRkMWRiMDFjNjljOTdiOWQyZTUwIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF8wYzVjODFiMjY1ZjQ0ZDFkYjAxYzY5Yzk3YjlkMmU1MCA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF8wYzVjODFiMjY1ZjQ0ZDFkYjAxYzY5Yzk3YjlkMmU1MCcsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNTEuNDY1OTgzMjcsMC4xODQ4NzcxMjddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogOSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1heEJvdW5kczogYm91bmRzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF5ZXJzOiBbXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTsKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfMWE0YzYyMDZhMmU1NDFkOGI0MzllMjIwYjJhZjJhY2YgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3tzfS50aWxlLm9wZW5zdHJlZXRtYXAub3JnL3t6fS97eH0ve3l9LnBuZycsCiAgICAgICAgICAgICAgICB7CiAgImF0dHJpYnV0aW9uIjogbnVsbCwKICAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsCiAgIm1heFpvb20iOiAxOCwKICAibWluWm9vbSI6IDEsCiAgIm5vV3JhcCI6IGZhbHNlLAogICJzdWJkb21haW5zIjogImFiYyIKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzY5YjE1MzU0NTc2NTQ1Y2FiNzMwY2YxNmRhYTc1MTA0ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNDg2OTU3MDAwMDAwMDA0LDAuMDk1MTExXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9iY2ZkYmY4NTc1N2Q0ODIwYjdjMTRhYmI2MDJmNzk1MCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUyMjI4NywtMC4xMjU4NDgwMDAwMDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzBjNWM4MWIyNjVmNDRkMWRiMDFjNjljOTdiOWQyZTUwKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfYjRiYjc4ZWMyNjNkNDY1Y2FiOTVlYzI4NDgwMWNhNDkgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS40MTAwMzkwMDAwMDAwMDUsLTAuMTI3NTIzXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl8xNjUzYmNmOTk1YzQ0ZWU1YTIzODlhNGQxODQ5ZDEwNyA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUyMTA0Njc1LC0wLjIxMzQ5MjE0XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl83MWU1ZWExNjA4NTk0MjdlODJkNWYzYjYwNmUzYjI1MSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjM4OTI4NjksLTAuMTQxNjYxNTI1XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl83N2I5Mjk1MDcyNmI0ZTFlYTY4NWUwNjI4ZmZmMTJkMCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUxNTA0NjE3LC0wLjAwODQxODQ5M10sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzBjNWM4MWIyNjVmNDRkMWRiMDFjNjljOTdiOWQyZTUwKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfZmQyNTQ1ZTdhOTMyNDczNWJkM2ZkN2FmNWJjY2VhYTggPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS40NjU5ODMyNywwLjE4NDg3NzEyN10sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzBjNWM4MWIyNjVmNDRkMWRiMDFjNjljOTdiOWQyZTUwKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfN2ZiYzI5ZTE2YmFhNGI0MTllMjE5OTIwYWZhOTM3ZGEgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS40NjU5ODMyNywwLjE4NDg3NzEyN10sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzBjNWM4MWIyNjVmNDRkMWRiMDFjNjljOTdiOWQyZTUwKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfMjkxYzViNWFhMWZjNGI4Mjk3NTZlMmJjNTA2M2I5YzggPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS40NTYzNTcwMDAwMDAwMDQsMC4wNDA3MjVdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF8wYzVjODFiMjY1ZjQ0ZDFkYjAxYzY5Yzk3YjlkMmU1MCk7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzU2ODgyMTZmN2ZhNDQ5MjU4ZTg1N2QxM2Q0NDU5Y2M0ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNTIxMDQ2NzUsLTAuMjEzNDkyMTRdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF8wYzVjODFiMjY1ZjQ0ZDFkYjAxYzY5Yzk3YjlkMmU1MCk7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzYxMjAxOWI5OWQzNTRjZGE5NWViZDYyYWU5NmQ2ZjVhID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNDc0OTU0LC0wLjAzOTY0MV0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzBjNWM4MWIyNjVmNDRkMWRiMDFjNjljOTdiOWQyZTUwKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfMDY3ODRjMTFhMmMwNDBhNWFlOTE3ZjAxM2NjNDA3YzMgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS41MjA3ODc0NiwwLjIwNTQ2MDcwNjAwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl8wNWIxNTQwOGU0MzY0MDkyYThlZjc2ZDFhMzk5YjgwNyA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjYxNzMyNywtMC4yOTg3NzVdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF8wYzVjODFiMjY1ZjQ0ZDFkYjAxYzY5Yzk3YjlkMmU1MCk7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2YzMTc1M2RhZDkyMTRlMWI4ZWQyNjBkNjAxMWMxNzZhID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNDI1MjU2MDQsLTAuMzQ1NjA4MjkxXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9mMTY3OTY2OTljNmQ0MTU1YjJiNGZhYjJmNDM3MWUxZSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjQ1MjU4LDAuMDcwNzY2XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9jNjYxYTgxODYzNTk0NzU2OThkYTQzMWVjZjI5NzE4NSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjU2OTQ4NDMzLDAuMDgyOTA3NDc1XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9jZjJmNzI3N2NlOTE0ZGYyOGI0MzM5OWYzZTVhYzQ3OSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUyMjU0LC0wLjE1NDU5XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9jNzE4NTM0MDM1Zjk0M2E2YjBhM2I2NTAyNDY5YTNmZiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUxNDUyNTM0LC0wLjEwNDUxNTYyNl0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzBjNWM4MWIyNjVmNDRkMWRiMDFjNjljOTdiOWQyZTUwKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfOTYyNDhhODc2OTJkNGI3MGE2NzQ2ZjY2NWFkNTEwYzkgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS41Mjc3MDY2MiwtMC4xMjkwNTMyMDVdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF8wYzVjODFiMjY1ZjQ0ZDFkYjAxYzY5Yzk3YjlkMmU1MCk7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzM4MTg5NmMyMDM3ZjQ5OGFiOGQyMTA5YWNhZGQ2MzRlID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNDkwNTMyLDAuMDc0MDAzXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9hMjNlMGM4ZDMzN2E0YTU1OWU1ZmRjNjg3NzgzY2RhZSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjQ4ODc4LC0wLjQ0MTYyNzAwMDAwMDAwMDA1XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfMGM1YzgxYjI2NWY0NGQxZGIwMWM2OWM5N2I5ZDJlNTApOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl8zODQ0MTkyNTVmYTc0ZDFlYjc3YTNjMjZmMDA1NDkyYSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUxMzg0NzE4LC0wLjA3Nzc2NTY4Ml0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzBjNWM4MWIyNjVmNDRkMWRiMDFjNjljOTdiOWQyZTUwKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfOTM4N2I2MjMwZjY2NDFlNDk4ODAzYjdlODliMTNlN2YgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS40NTYzLDAuMDg1NjA1OTk5OTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF8wYzVjODFiMjY1ZjQ0ZDFkYjAxYzY5Yzk3YjlkMmU1MCk7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2ZmOGI4YzRjNGJkMTRiZjI4Y2YyYjYwZTMyMTRkYzg4ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNTQ0MjE5LC0wLjE3NTI4NF0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzBjNWM4MWIyNjVmNDRkMWRiMDFjNjljOTdiOWQyZTUwKTsKICAgICAgICAgICAgCjwvc2NyaXB0Pg==" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
map_2 = folium.Map(location=temp_pd.iloc[0].values.tolist(), zoom_start=9,tiles='Stamen Terrain')
```


```python
for key in location_Lodon:
    folium.Marker(location=location_Lodon[key]).add_to(map_2)
map_2
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIgLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC5taW4uY3NzIiAvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiIC8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIgLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuY3NzIiAvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2dpdC5jb20vcHl0aG9uLXZpc3VhbGl6YXRpb24vZm9saXVtL21hc3Rlci9mb2xpdW0vdGVtcGxhdGVzL2xlYWZsZXQuYXdlc29tZS5yb3RhdGUuY3NzIiAvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzRhZWJlYmMzYzdjNTRmNjg4N2MyYzViZjI1NDExYTFhIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF80YWViZWJjM2M3YzU0ZjY4ODdjMmM1YmYyNTQxMWExYSA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF80YWViZWJjM2M3YzU0ZjY4ODdjMmM1YmYyNTQxMWExYScsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNTEuNDY1OTgzMjcsMC4xODQ4NzcxMjddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogOSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1heEJvdW5kczogYm91bmRzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF5ZXJzOiBbXSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdvcmxkQ29weUp1bXA6IGZhbHNlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY3JzOiBMLkNSUy5FUFNHMzg1NwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTsKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHRpbGVfbGF5ZXJfY2EyMTA2NDE3NGUzNGEwYjllNjRmYzk0NzcxNDRlNWEgPSBMLnRpbGVMYXllcigKICAgICAgICAgICAgICAgICdodHRwczovL3N0YW1lbi10aWxlcy17c30uYS5zc2wuZmFzdGx5Lm5ldC90ZXJyYWluL3t6fS97eH0ve3l9LmpwZycsCiAgICAgICAgICAgICAgICB7CiAgImF0dHJpYnV0aW9uIjogbnVsbCwKICAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsCiAgIm1heFpvb20iOiAxOCwKICAibWluWm9vbSI6IDEsCiAgIm5vV3JhcCI6IGZhbHNlLAogICJzdWJkb21haW5zIjogImFiYyIKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzAwOGU2ODUyOTZjMjRmMzhiZjQ1MzRjMDhlNDFhN2QzID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNDg2OTU3MDAwMDAwMDA0LDAuMDk1MTExXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl83MjZmNzgyYTA5NTc0ZTk2YTNhY2VlZjBmMmJhMTIwNiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUyMjI4NywtMC4xMjU4NDgwMDAwMDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzRhZWJlYmMzYzdjNTRmNjg4N2MyYzViZjI1NDExYTFhKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfYmEyODJkOGQ4MjY3NDY1N2FiZWI1YmMzY2QxZjE3MjMgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS40MTAwMzkwMDAwMDAwMDUsLTAuMTI3NTIzXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9iMTU2MzIxYzgxM2Y0ODNkOTJjNTIwNGIwN2Y4NDhkMSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUyMTA0Njc1LC0wLjIxMzQ5MjE0XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9iODViMGRiZTNhODk0OWU5YTM1ZTYzNDc3NTc5ZTljZCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjM4OTI4NjksLTAuMTQxNjYxNTI1XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl8yM2VlODFiY2MyMDM0MzUwYTUwNWUzNWU3NDZhZjFkOCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUxNTA0NjE3LC0wLjAwODQxODQ5M10sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzRhZWJlYmMzYzdjNTRmNjg4N2MyYzViZjI1NDExYTFhKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfMGY4ZWM3YzgwNTNkNDBiODliMzZlNTEzOWVmMmNmMTcgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS40NjU5ODMyNywwLjE4NDg3NzEyN10sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzRhZWJlYmMzYzdjNTRmNjg4N2MyYzViZjI1NDExYTFhKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfNGJlMGJjNTU3N2Q5NDQ5NGJjNmQxZmQyMzcwMmQzYWYgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS40NjU5ODMyNywwLjE4NDg3NzEyN10sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzRhZWJlYmMzYzdjNTRmNjg4N2MyYzViZjI1NDExYTFhKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfYTY0NTEzNGU1YTg0NDljNWI3YzZjNzRiZTMyNTZiMTEgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS40NTYzNTcwMDAwMDAwMDQsMC4wNDA3MjVdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF80YWViZWJjM2M3YzU0ZjY4ODdjMmM1YmYyNTQxMWExYSk7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzdkNjY0ZTA5MGZjODRmZTZiYmViNzVjMzdiY2E2ODg5ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNTIxMDQ2NzUsLTAuMjEzNDkyMTRdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF80YWViZWJjM2M3YzU0ZjY4ODdjMmM1YmYyNTQxMWExYSk7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyX2EwODlhYmI4OTA0YjQyZWI5NDlhZWVmZmJiNGQzMzA4ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNDc0OTU0LC0wLjAzOTY0MV0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzRhZWJlYmMzYzdjNTRmNjg4N2MyYzViZjI1NDExYTFhKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfZDMyY2Y2MTFiNjAwNDViM2E1OWMyZTc0N2MyNDc3ODMgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS41MjA3ODc0NiwwLjIwNTQ2MDcwNjAwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl85YzFkNWVhNGUyNzI0NmMzYjRkYjJjMjA0MjczN2U5MiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjYxNzMyNywtMC4yOTg3NzVdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF80YWViZWJjM2M3YzU0ZjY4ODdjMmM1YmYyNTQxMWExYSk7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzk2NWZlZjk4NTJhNDQ1OWRhZTZjMGUxNjk5YzNlNzk5ID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNDI1MjU2MDQsLTAuMzQ1NjA4MjkxXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9iMjQ0NDgzZDIyNjc0YzIwYjQ1ZmEyMjM3OGNhYjhiZiA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjQ1MjU4LDAuMDcwNzY2XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9kNTVjZjg0MzU4MmQ0NWUyODE1NDJiNGJkN2MxZmRlYyA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjU2OTQ4NDMzLDAuMDgyOTA3NDc1XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl9kNTZhMGNlMTA5OTY0NGZhOTczMWY3MjE0NDA0ZGVmMCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUyMjU0LC0wLjE1NDU5XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl8wMGIzOTMwMzQ0OTA0Y2FlYWYyZjkzNzU3NTc1MzYxMCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUxNDUyNTM0LC0wLjEwNDUxNTYyNl0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzRhZWJlYmMzYzdjNTRmNjg4N2MyYzViZjI1NDExYTFhKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfZjlhMGViMzEzZjkxNGIxM2EzYzM3NmJiOWU4Nzk2ZDcgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS41Mjc3MDY2MiwtMC4xMjkwNTMyMDVdLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF80YWViZWJjM2M3YzU0ZjY4ODdjMmM1YmYyNTQxMWExYSk7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzEyZjM0YjhjZWZhMTQ4NzY4OTljN2ZlYWMyMjZkYWNlID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNDkwNTMyLDAuMDc0MDAzXSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl83NzgyZGYzMDYzZmQ0OWYwOGI4ZmNiMTkxNGM1NmYwMSA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjQ4ODc4LC0wLjQ0MTYyNzAwMDAwMDAwMDA1XSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBpY29uOiBuZXcgTC5JY29uLkRlZmF1bHQoKQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIC5hZGRUbyhtYXBfNGFlYmViYzNjN2M1NGY2ODg3YzJjNWJmMjU0MTFhMWEpOwogICAgICAgICAgICAKICAgIAoKICAgICAgICAgICAgdmFyIG1hcmtlcl8yZGNjYjhkMDJmMDQ0ZTdiYjJhMDYzYTMxMTU2MGZkMCA9IEwubWFya2VyKAogICAgICAgICAgICAgICAgWzUxLjUxMzg0NzE4LC0wLjA3Nzc2NTY4Ml0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzRhZWJlYmMzYzdjNTRmNjg4N2MyYzViZjI1NDExYTFhKTsKICAgICAgICAgICAgCiAgICAKCiAgICAgICAgICAgIHZhciBtYXJrZXJfM2YyZDkxMTcwYmJiNDhiZThiZDVhN2I1ODI1YjUzMjYgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFs1MS40NTYzLDAuMDg1NjA1OTk5OTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgIGljb246IG5ldyBMLkljb24uRGVmYXVsdCgpCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgLmFkZFRvKG1hcF80YWViZWJjM2M3YzU0ZjY4ODdjMmM1YmYyNTQxMWExYSk7CiAgICAgICAgICAgIAogICAgCgogICAgICAgICAgICB2YXIgbWFya2VyXzhiNjgzYjI3ODQzZDQyZjhiODMyZGY4NDJhZGU5MmEwID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbNTEuNTQ0MjE5LC0wLjE3NTI4NF0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgaWNvbjogbmV3IEwuSWNvbi5EZWZhdWx0KCkKICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAuYWRkVG8obWFwXzRhZWJlYmMzYzdjNTRmNjg4N2MyYzViZjI1NDExYTFhKTsKICAgICAgICAgICAgCjwvc2NyaXB0Pg==" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>


