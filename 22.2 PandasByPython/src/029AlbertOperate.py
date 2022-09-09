import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

# 设置最大显示行数为777
pd.options.display.max_columns = 777

# 读取Excel
students_one = pd.read_excel('./TestExcel/AlbertData.xlsx',sheet_name='Sheet1',index_col='Index')
students_two = pd.read_excel('./TestExcel/AlbertData.xlsx',sheet_name='Sheet2',index_col='Index')
#print(students_one.tail())
#print(students_two.head())


df = pd.DataFrame({
    'Factor': ['Growth', 'Value'],
    'Weight': [0.10, 0.20],
    'Variance': [0.15, 0.35]
})

#print(df)

# 拼接两张sheet表
students_total = students_one.append(students_two).reset_index(drop=True)
#print(students_total.tail())

missing_date = students_total

# 排序并绘制柱状图
# students_total.sort_values(by=['MoneyLast','MoneyCur'],inplace=True,ascending=False)
#print(students_total.head())
temp = students_total[:20]
temp.plot.bar(x='Name',y=['MoneyLast','MoneyCur'])
ax = plt.gca()
ax.set_xticklabels(temp.Name,rotation=45,ha='right')
#plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.title("National Students' Money")


# 叠加柱状图
# students_total.sort_values(by=['MoneyLast','MoneyCur'],inplace=True,ascending=False)
#print(students_total.head())
temp.plot.bar(x='Name',y=['MoneyLast','MoneyCur'],stacked=True)
ax = plt.gca()
ax.set_xticklabels(temp.Name,rotation=45,ha='right')
#plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.title("National Students' Money")

# 水平叠加柱图
temp.plot.barh(x='Name',y=['MoneyLast','MoneyCur'],stacked=True)
#plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.title("National Students' Money")

# 环形图
plt.figure(figsize=[9,7]) # 防止颜色超出
temp = students_total[:8]
temp.set_index('Country',inplace=True)
temp['MoneyLast'].plot.pie(wedgeprops = {'width' : 0.4})
plt.title("MoneyLast")
plt.tight_layout()

# 折线图
temp = students_total[:20]
temp.set_index('Country',inplace=True)
temp.plot(y='MoneyLast')
plt.xticks(range(0,len(temp.index)),temp.index)
ax = plt.gca()
ax.set_xticklabels(temp.index,rotation=45,ha='right')
plt.title("MoneyLast")
plt.tight_layout()

# 叠加区域图
temp = students_total[:20]
temp.set_index('Country',inplace=True)
temp.plot.area(y=['MoneyLast','MoneyCur'])
plt.xticks(range(0,len(temp.index)),temp.index)
ax = plt.gca()
ax.set_xticklabels(temp.index,rotation=45,ha='right')
plt.title("MoneyLast")
plt.tight_layout()

# 散点图
#students_total.plot.scatter(x='Country',y='MoneyLast')

# 密度图
students_total.set_index('Country',inplace=True)
students_total['MoneyLast'].plot.hist(bins=100)
plt.xticks(range(0,max(students_total.MoneyLast.astype(int)),50),fontsize=8,rotation=90)
plt.title('MiDu')

# 数据相关性
print(students_total.corr())

plt.show()

# 手动追加一行
stu = pd.Series({'Name':'法外狂徒张三','Age':22,'Phone':13323263588,'Country':'China'})
students_total=students_total.append(stu,ignore_index=True)
print(students_total.tail())

# 更改3999行王瑜为JoJo
students_total['Name'].at[3999] = 'JoJo'
print(students_total.tail())

# 切片技术在中间插入一行
part1 = students_total[:4]
part2 = students_total[4:]
stu = pd.Series({'Name':'法外狂徒张三','Age':22,'Phone':13323263588,'Country':'China'})
students_total = part1.append(stu,ignore_index = True).append(part2).reset_index(drop=True)
print(students_total.head())

# 删除第0,2,3行和5-8行
students_total.drop(index=[0,2,3],inplace=True)
students_total.drop(index=range(5,8),inplace=True)
print(students_total.head())

# 重新铺一下index
students_total.reset_index(drop=True,inplace=True)
print(students_total.head())