import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import linregress

def validate_revenue(series):
    if not 5<series.Revenue<20:
        print(f'{series}值不在范围内')

sales = pd.read_excel('./TestExcel/output018.xlsx',dtype={'Month':str})

# 斜率，截距
slope,intercept,r,p,std_err = linregress(sales.index,sales.Revenue)
# 线性回归方程
exp = sales.index*slope+intercept

# sales.plot.area(y='Revenue')
# 散点图
plt.scatter(x=sales.index,y=sales['Revenue'],color='orange')
plt.plot(sales.index,exp,color='blue')
#plt.bar(sales.index,sales.Revenue)
ax = plt.gca()
ax.set_xticklabels(sales['Month'],rotation=45,ha='right')
plt.title(f'y={slope}*X+{intercept}')
plt.tight_layout()
plt.show()

# 横向验证，传入函数的是series
#sales.apply(validate_revenue,axis=1)
#print(sales.Month.dtype)