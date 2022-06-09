import data as dt
import pandas as pd 
import functions as fun 
import functions2 as fun2 
import visualization as vi


data_ob=dt.ob_data
pt_data=dt.pt_data



OBook=fun.f_descriptive_ob(data_ob=data_ob)


metric = pd.DataFrame(OBook['median_ts_ob'])
print(f"Median Time Of Orderbook:{metric}")

metric2 = pd.DataFrame(OBook['Spread'])
print(f"Spread:{metric2}")

metric3 = pd.DataFrame(OBook['Midprice'])
print(f"Midprice:{metric3}")

metric4 = pd.DataFrame(OBook['No_price_levels'])
print(f"No. of price levels:{metric4}")

metric5 = pd.DataFrame(OBook['Bid_Volume'])
print(f"Bid Volume:{metric5}")

metric6 = pd.DataFrame(OBook['Ask_Volume'])
print(f"Ask Volume:{metric6}")

metric7 = pd.DataFrame(OBook['Total_Volume'])
print(f"Total volume:{metric7}")

metric8 = pd.DataFrame(OBook['Imbalance'])
print(f"Imbalance:{metric8}")

metric9 = pd.DataFrame(OBook['W-Midprice'])
print(f"w-Midprice:{metric9}")

metric10 = pd.DataFrame(OBook['V-WAP'])
print(f"V-WAP:{metric10}")

PTrades= fun2.f_publictrades_metrics(pt_data=pt_data)


metricB1 = pd.DataFrame(PTrades['Buy_tt'])
print(f"Buy Trades Count:{metricB1}")

metricB2 = pd.DataFrame(PTrades['Sell_tt'])
print(f"Sell Trades Count:{metricB2}")

metricB3 = pd.DataFrame(PTrades['Total_trade'])
print(f"Total Trade:{metricB3}")

metricB4 = pd.DataFrame(PTrades['Diff'])
print(f"Difference in Trade Count:{metricB4}")

metricB5 = pd.DataFrame(PTrades['OHLC'])
print(f"OHLC:{metricB5}")

plot_3 = vi.plot_lines(data_x=list(data_ob.keys()),
                       data_s1= OBook['bid_size'],
                       data_s2= OBook['ask_size'],
                       data_s3= OBook['total_size'])
plot_3.show()






