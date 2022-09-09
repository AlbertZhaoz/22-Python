import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./TestExcel/output011.xlsx',index_col='From')
print(students)
# 绘制饼图,默认情况下以index_col作为图例显示饼图
# 排序以顺时针形式呈现，并将开始位置设置为-250
# students['2017'].sort_values().plot.pie(startangle=-250)
# 第二种方式counterclock=False顺时针方式呈现
students['2017'].plot.pie(counterclock=False)
plt.title('Source of International Students')
plt.ylabel('2017',fontweight='bold')
plt.show()