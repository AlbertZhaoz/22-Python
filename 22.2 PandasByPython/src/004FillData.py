import pandas as pd
from datetime import date, timedelta


# 实现月份累加算法,d是初始时间，md是累加的月份
def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


# 跳过空行16行，选取E:H列 指定ID列的数据类型为int(先转为string类型，直接转int类型不行)
books = pd.read_excel('./TestExcel/output004.xlsx', skiprows=16, usecols="E:H",
                      dtype={'ID': str, 'InStore': str, 'Date': str})
startTime = date(2021, 12, 25)
for i in books.index:
    books['ID'].at[i] = i + 1
    print(type(books['ID']))  # 此种写法books['ID']是pandas.core.series.Series对象
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'NO'  # 在Python中if else可以组成表达式用
    # books['Date'].at[i] = startTime + timedelta(days=i)  # 天数依次累加
    # books['Date'].at[i] = date(startTime.year+i,startTime.month,startTime.day)  # 年份依次累加
    books['Date'].at[i] = add_month(startTime, i)  # 月份依次累加
# print(books['ID'])

books.to_excel('./TestExcel/output004Test.xlsx')
print(books)
