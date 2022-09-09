import pandas as pd
import matplotlib.pyplot as plt

weeks = pd.read_excel('./TestExcel/output012.xlsx',index_col='Week')
print(weeks)
print(weeks.columns)
# 折线图
weeks.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'])
plt.title('Sales Weekly Trend',fontsize=16,fontweight='bold')
plt.ylabel('Total',fontsize=12,fontweight='bold')
plt.xticks(weeks.index)
# 叠加区域图
weeks.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'])
plt.title('Sales Weekly Trend',fontsize=16,fontweight='bold')
plt.ylabel('Total',fontsize=12,fontweight='bold')
plt.xticks(weeks.index)
plt.show()
