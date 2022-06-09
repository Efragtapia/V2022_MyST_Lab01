import numpy as np 
import pandas as pd
import data as dt



pt_data=dt.pt_data



def f_publictrades_metrics(pt_data=pt_data):
    
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