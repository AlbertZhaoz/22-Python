import pandas as pd
import matplotlib.pyplot as plt 

# 显示所有列
pd.options.display.max_columns =777
homes = pd.read_excel('./TestExcel/output013.xlsx')
# print(homes.head())
# 散点图scatter
#homes.plot.scatter(x='sqft_living',y='price')
# 直方图hist 分布区间bins
# homes.sqft_living.plot.hist(bins=100)
# plt.xticks(range(0,max(homes.sqft_living),5000),fontsize=8,rotation=90)
# 密度图kde
homes.sqft_living.plot.kde()
plt.xticks(range(0,max(homes.sqft_living),5000),fontsize=8,rotation=90)
plt.show()
# 数据相关性分析 column row relation
print(homes.corr())