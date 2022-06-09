import numpy as np 
import pandas as pd
import data as dt

data_ob=dt.ob_data
pt_data=dt.pt_data

def f_descriptive_ob(data_ob:dict) -> dict:
    
    # -- Median Time of Orderbook update -- #
    ob_ts = list(data_ob.keys()) #Como todo esta en str convertir 
    l_ts = [pd.to_datetime(i_ts) for i_ts in ob_ts]
    # ob_m1 orderbook metric 1
    # En milisegundos ob_m1.total_seconds()*1000
    # Lo cual sería cada cuando cambia en promedio la situación del orderbook
    ob_m1 = np.median([l_ts[n_ts+1] - l_ts[n_ts] for n_ts in range(0, len(l_ts)-1)])# Este nos da la mediana de la diferencias 

    # -- Spread -- #
    # ob_m2 orderbook metric 2
    # Se utiliza mediante el top of the book
    ob_m2 = [data_ob[ob_ts[i]]['ask'][0] - data_ob[ob_ts[i]]['bid'][0] for i in range(0, len(ob_ts))]

    # -- Midprice -- # 
    # ob_3 orderbook metric 3
    ob_m3 = [data_ob[ob_ts[i]]['ask'][0] + data_ob[ob_ts[i]]['bid'][0]*0.5 for i in range(0, len(ob_ts))]

    # -- No. of price levels-- # 
    # ob_4 orderbook metric 4
    # Nos dice los niveles de precios 
    ob_m4 = [data_ob[i_ts].shape[0] for i_ts in ob_ts]

    # -- Bid_Volume, Ask_Volume, Total_Volume-- # 
    # ob_5 orderbook metric 5
    # Esta es la suma de todas las operaciones de bid en cada libro de órdenes
    ob_m5 = [np.round(data_ob[i_ts]['bid_size'].sum(),6) for i_ts in ob_ts]
    ob_m6 = [np.round(data_ob[i_ts]['ask_size'].sum(),6) for i_ts in ob_ts]
    ob_m7 = [np.round(data_ob[i_ts]['bid_size'].sum() + data_ob[i_ts]['ask_size'].sum(),6) for i_ts in ob_ts]
    ob_m8 = [np.round(data_ob[i_ts]['bid_size'].sum(),6) / np.round(data_ob[i_ts]['bid_size']+data_ob[i_ts]['ask_size']).sum() for i_ts in ob_ts]
    ob_m9 = np.multiply(ob_m3,ob_m8)
    
    bid_side = [np.round(data_ob[i_ts]['bid'].sum()*data_ob[i_ts]['bid_size'].sum(),6) for i_ts in ob_ts]
    ask_side = [np.round(data_ob[i_ts]['ask'].sum()*data_ob[i_ts]['ask_size'].sum(),6) for i_ts in ob_ts]
    numerator = np.sum(bid_side + ask_side)
    denominator = [np.round(data_ob[i_ts]['bid_size']+data_ob[i_ts]['ask_size'].sum(),6) for i_ts in ob_ts]
    vwap = numerator/denominator
    
    # -- OHLCV -- #
    ob_m11 = data_ob['price'].resample('60T').ohlc()


    r_data = {'median_ts_ob': ob_m1, 'Spread': ob_m2, 'Midprice': ob_m3, 'No_price_levels': ob_m4, 'Bid_Volume': ob_m5, 'Ask_Volume': ob_m6, 'Total_Volume': ob_m7, 'Imbalance': ob_m8, 'W-Midprice': ob_m9, 'V-WAP': vwap,'OHLC:':ob_m11}

    return r_data



def f_publictrades_metrics(pt_data:dict) -> dict:
    
    pt_data.index = pd.to_datetime(pt_data)['timestamp']
    n = pt_data.groupby('side')['side'].count()
    
    # -- (1) Buy Trade Count -- #
    pt1 = print(f"Buy Trade Count: {n['buy']}")
                
    # -- (2) Sell Trade Count -- #
    pt2 = print(f"Buy Trade Count: {n['sell']}")
                
    # -- (3) Total Trade Count -- #
    total_trades = n.sum()
    pt3 = print(f"Total Trade count: {total_trades} trades")
    
    # -- (4) Difference in Trade Count -- #
    diff = pt1 - pt2
    pt4 = print(f"The difference in Trade count: {diff}")
    
    # Quantity of buy-side sell-side and total trade per period  #
    # n2 = pt_data.groupby('amount')['amount'].count()
    # -- (5) Sell volume -- #
    # pt5 = print(f"Buy Trade Volume: {n['buy']}")
    # -- (6) Buy volume -- #
    # pt6 = print(f"Sell Trade Volume: {n['sell']}")
    # -- (7) Total Volume -- #
    # -- (8) Difference in Volume Buy  Sell -- #
    
    # -- (9) OHLCV: Open High Low Close Volume   Trade Price -- #
    pt9 = pt_data['price'].resample('60T').ohlc()

    
    r_data2 = {'Buy_tt': pt1,'Sell_tt':pt2,'Total_trade':pt3,'Diff':pt4,'OHLC':pt9}

    return r_data2


