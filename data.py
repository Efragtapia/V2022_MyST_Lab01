import sys
import os
import pandas as pd
import numpy as np
import pyarrow as pa
 
# Absolute path directory
abs_dir = os.path.abspath('.')
 
# Add project folder to path
sys.path.insert(0, abs_dir)
 
def leer_parquet(file_dir, file_name):
    
    in_data = pa.parquet.read_table(source=abs_dir + file_dir + '/' + file_name)
    dc_data = in_data.to_pydict()
 
    return dc_data
 
dc_ob = leer_parquet(file_dir='/Files/', file_name='ob_okex_daousdt_arrow_lz4.parquet')
 
"""
with open(abs_dir + '/Files/pickle_ob_okex_daousdt' + '.pickle', 'wb') as handle:
    pickle.dump(r_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
 
with open(file_dir + file_name + '.pickle', 'rb') as handle:
    r_data = pickle.load(handle)
"""
 
data_ob = {dc_ob['keys'][i_key]: np.array([dc_ob['bid_volume'][i_key], dc_ob['bid_price'][i_key],
                                           dc_ob['ask_price'][i_key], dc_ob['ask_volume'][i_key]],
                                           dtype=object)
                 for i_key in range(0, len(list(dc_ob['keys'])))[0:4]}
 
(data_ob[list(data_ob.keys())[0]][1][0] + data_ob[list(data_ob.keys())[0]][2][0])*0.5