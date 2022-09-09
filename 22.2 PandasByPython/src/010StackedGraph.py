import pandas as pd
import matplotlib.pyplot as plt


users = pd.read_excel('./TestExcel/output010.xlsx')
users['Total'] = users.Oct+users.Nov+users.Dec
users.sort_values(by='Total',ascending=False,inplace=True)
print(users)
# 分组柱状图-->叠加柱状图stacked
users.plot.bar(x='Name',y=['Oct','Nov','Dec'],stacked=True)
plt.title('User Behavior',fontsize=24,fontweight='bold')
# 旋转X轴文字45°
ax = plt.gca()
ax.set_xticklabels(users.Name,rotation=45,ha='right')
plt.tight_layout()
# 水平柱状图
users.sort_values(by='Total',ascending=True,inplace=True)
users.plot.barh(x='Name',y=['Oct','Nov','Dec'],stacked=True)
plt.tight_layout()
plt.show()
