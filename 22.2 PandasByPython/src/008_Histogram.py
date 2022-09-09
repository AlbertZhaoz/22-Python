import pandas as pd
import matplotlib.pyplot as plt

# 绘图，不要添加index_col='Field'索引列
books = pd.read_excel('./TestExcel/output008.xlsx')
print(books.head(5))
# 按照Number列排序 降序 替换原先的DF
books.sort_values(by='Number', ascending=False, inplace=True)
# 使用pandas绘图：横坐标为Field 纵坐标为Number 颜色橘色 标题xxx
# books.plot.bar(x='Field', y='Number',color='orange',title='InterNationalBooks')
# 使用plt绘图
plt.bar(books.Field, books.Number, color='orange')
# 旋转标签90
plt.xticks(books.Field, rotation=90)
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('InternationalBooks', fontsize=16)
# 紧凑型绘图，能够将横坐标全部显示出来
plt.tight_layout()
plt.show()
