import pandas as pd
import numpy as np

def cal_bike_complex_clothing(b,c):
    return b**2+c*np.pi

sales = pd.read_excel('./TestExcel/output012.xlsx')
sales['complex'] = sales.apply(lambda row:cal_bike_complex_clothing(row['Bikes'],row['Clothing']),axis=1)

#将列名大写
sales.rename(columns={'complex':'Complex'},inplace=True)
sales.drop(columns={'Components'},inplace=True)
print(sales)