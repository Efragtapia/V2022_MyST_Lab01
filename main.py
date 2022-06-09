import data as dt
import pandas as pd 
import functions as fun 


data_ob=dt.ob_data

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









