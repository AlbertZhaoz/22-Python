import pandas as pd
import matplotlib.pyplot as plt

books = pd.read_excel('./TestExcel/output009.xlsx')
print(books)
books.sort_values(by=2021, inplace=True, ascending=False)
books.plot.bar(x='Field', y=[2020, 2021],color=['orange','blue'])
plt.title('National Books', fontsize=16, fontweight='bold')
plt.xlabel('Field', fontweight='bold')
plt.ylabel('Number', fontweight='bold')
# 自定义X轴样式:斜45° 文字最末端-对齐
ax = plt.gca()
ax.set_xticklabels(books.Field, rotation=45, ha='right')
# 将图片左边和底部固定
figures = plt.gcf()
figures.subplots_adjust(left=0.2,bottom=0.42)
# plt.tight_layout()
plt.show()
