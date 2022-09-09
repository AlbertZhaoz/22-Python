import pandas as pd
from faker import Faker
import random as rd

fake = Faker()
# fake = Faker('zh-CN')

# 要输入到DF中的数据字典
dic = {}

# 姓名
list_name = []
# 随机手机号
list_phone_number = []
# 随机国家
list_country = []
# 随机邮件
list_email = []
# 随机车牌号
list_car_number = []
# 随机年份，格式2022-02-22
list_date = []
# 随机字符串，长度在min-max之间
list_str =[]
# 随机年龄
list_age = []
# 随机金额
list_money_last = []
list_money_current = []
# 索引
list_index = []
for i in range(0,2000):
    list_index.append(i)
    list_name.append(fake.name())
    list_phone_number.append(fake.phone_number())
    list_country.append(fake.country())
    list_email.append(fake.email())
    list_car_number.append(fake.license_plate())
    list_date.append(fake.date_time(tzinfo=None, end_datetime=None))
    list_str.append(fake.pystr(min_chars=0, max_chars=8))
    list_age.append(rd.randint(15,65))
    list_money_last.append(rd.random()*9999)
    list_money_current.append(rd.random()*10000)

dic['Index'] = list_index
dic['Name'] = list_name
dic['Age'] = list_age
dic['Phone'] = list_phone_number
dic['Country'] = list_country
dic['Email'] = list_email
dic['CarNumber'] = list_car_number
dic['Date'] = list_date
dic['Note'] = list_str
dic['MoneyLast'] = list_money_last
dic['MoneyCur'] = list_money_current

df = pd.DataFrame(dic)
print(df.columns)
writer = pd.ExcelWriter('./TestExcel/AlbertData.xlsx',mode='a',engine='openpyxl')
df.to_excel(writer,sheet_name="Sheet2")
writer.save()
writer.close()

