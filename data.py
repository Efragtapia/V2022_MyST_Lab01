import sys
import os
import pandas as pd
import numpy as np
import pyarrow as pa
import json 
 
pt_data = pd.read_csv('btcusdt_binance.csv')


# Opening JSON object as a dictionary
f = open('orderbooks_05jul21.json')

# Return JSON object as a dictionary 
orderbooks_data = json.load(f)
ob_data = orderbooks_data['bitfinex']

# Drop None keys (con compresión de diccionarios)
ob_data = {i_keys: i_value for i_keys, i_value in ob_data.items() if i_value is not None}

# Convert to DataFrame and rearange colums
ob_data = {i_ob: pd.DataFrame(ob_data[i_ob])[['bid_size', 'bid', 'ask', 'ask_size']]
                if ob_data[i_ob] is not None else None for i_ob in list(ob_data.keys())}

