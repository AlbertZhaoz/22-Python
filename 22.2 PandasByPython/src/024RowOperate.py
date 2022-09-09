import pandas as pd


students1 = pd.read_excel('F:/Repo/albertpython/TestExcel/output011.xlsx',sheet_name='Sheet1')
students2 = pd.read_excel('F:/Repo/albertpython/TestExcel/output011.xlsx',sheet_name='Sheet2')

# 两个Sheet合并为一个,重置index_col drop=True放弃原来的
student_total = students1.append(students2).reset_index(drop=True)

# 追加手动创建的一行
stu = pd.Series({'Rank':100,'From':'USA','2016':90,'2017':100})
student_total=student_total.append(stu,ignore_index=True)

# 更改其中一行的值
student_total['From'].at[13] = 'Mexico3'
student_total.at[12,'From'] = 'Japan3'

# 插入一行 切片技术
stu = pd.Series({'Rank':101,'From':'USB','2016':90,'2017':100})
# 左闭右开
part1 = student_total[:10]
part2 = student_total[10:]
student_total = part1.append(stu,ignore_index=True).append(part2).reset_index(drop=True)

# 删除数据行
# student_total.drop(index=[0,1,2],inplace=True)
# student_total.drop(index=range(4,6),inplace=True)

for i in range(5,8):
    student_total['From'].at[i] =''

missing_data = student_total.loc[student_total['From']=='']
student_total.drop(index=missing_data.index,inplace=True) #切片的方式传入
student_total.reset_index(drop=True) # 重新铺一下index
print(student_total)


