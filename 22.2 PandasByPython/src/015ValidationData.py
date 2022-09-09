import pandas as pd

def validate_score(x):
    """[校验函数]  
      
    Args:
        x ([object]): [学生信息]
    """    
    try:
        assert 0<=x.Score<=100
    except: 
        print(f'#{x.ID}\tStudent {x.Name} has an invalid score {x.Score}')
    #第二种写法
    #if not 0<=x.Score<=100:
        #print(f'#{x.ID}\tStudent {x.Name} has an invalid score {x.Score}')

students = pd.read_excel('./TestExcel/output015.xlsx')
# axis默认为0,从上到下  1,从左到右进行校验
students.apply(validate_score,axis=1)
# print(students)