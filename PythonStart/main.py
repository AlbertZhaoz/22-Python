import os.path
import re
import threading,time

# lambda 表达式
sum = lambda arg1,arg2: arg1+arg2

print(sum(10,20))

__add = lambda arg1,arg2:arg1+arg2

class Student:
    name = "Albert"
    __age = 14
    sex = '男'

    def __int__(self,*s):
        self.sex = s

    def GetAge(self):
        return self.__age;

class Complex:
    r = 5
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)

print(Student().name)
print(Student().GetAge())

filePath = "C:\\Users\\AlbertZhao\Downloads\\test.txt"
# 可以通过 ptyhon r 进行转义
filePath2 = r"C:\Users\AlbertZhao\Downloads\test.txt"
fileRef = open(filePath,mode='r', buffering=-1, encoding='UTF-8', errors=None, newline=None, closefd=True, opener=None)
lines = fileRef.read()
print(lines)

try:
    result = 10/0
except ZeroDivisionError:
    print("division by zero")
finally:
    print("666")

def loop():
    print("thread is running,name is %s"%threading.currentThread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
    print('thread %s is running...' % threading.current_thread().name)

t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

re_result = re.split(r'[\s\,]+','a,g,  d')
print(re_result)

# __name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性