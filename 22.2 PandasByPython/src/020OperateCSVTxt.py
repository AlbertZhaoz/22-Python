import pandas as pd

students1 = pd.read_csv('./TestOtherFiles/Students.csv')
print(students1)

students2 = pd.read_csv('./TestOtherFiles/Students.txt',sep='|')
print(students2)