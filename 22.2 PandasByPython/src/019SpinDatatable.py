import pandas as pd

# 显示最大列
pd.options.display.max_columns = 999
videos = pd.read_excel('./TestExcel/output016.xlsx',index_col='Month')
# 旋转表格，要将index_col设置为旋转坐标列Month，不然就会以默认index来作为列名
videos = videos.transpose()
print(videos)