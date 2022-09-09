import pandas as pd

house_price = pd.read_excel('./TestExcel/output013.xlsx')

# DataFrame.sum()
# axis 1横轴 0纵轴 sum求和 mean求平均
temp_total = house_price[['bedrooms','bathrooms']].sum(axis=1)
temp_average = house_price[['bedrooms','bathrooms']].mean(axis=1)
house_price['TotalRooms'] = temp_total
house_price['AverageRooms'] = temp_average
# house_price['AverageRooms'] .astype(int)
# 追加列方向的累加
col_sum = house_price[['ID','price','bedrooms','bathrooms','sqft_living','sqft_basement']].sum()
col_sum['TotalRooms'] = 'Summary'
# 将自动按照col_sum的列名来进行追加
house_price = house_price.append(col_sum,ignore_index=True)

print(house_price)
