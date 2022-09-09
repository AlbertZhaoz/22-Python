import pandas as pd

# dic = {'x': 100, 'y': 200, 'z': 300}
# s1 = pd.Series(dic)
# 下面这种方式是一样的效果
# index是行号 name是列号 [100,200,300]是行内容
# s1 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')  # 一行数据
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[2, 3, 4], name='C')
# 以Dictionary的形式将Series加入到DataFrame中
df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
# df = df.set_index('A')
# 假如Series index是[2,3,4] 没有的则会填充NaN
print(df.head())
