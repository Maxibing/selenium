#coding=utf-8

class ClassA(object):

    string1 = '这是一个字符串'

    def function(self):
        print('这是一个实例')
        print(self)

    @classmethod
    def classfunc(cls):
        print('这是一个类方法')
        print(cls)

    @staticmethod
    def staticfunc():
        print('这是一个静态方法')

test = ClassA() #初始化一个classA的对象，test是类classA的实例对象
test.function() #对象调用实例对象

test.staticfunc()   #对象调用静态方法

test.classfunc()    #对象调用类方法

print(test.string1) #对象调用类变量

ClassA.function(test)  # 类调用实例方法，需要带参数，这里的test是一个对象参数
ClassA.function(ClassA) # 类调用实例方法，需要带参数，这里的ClassA是一个类参数
ClassA.staticfunc() # 类调用静态方法
ClassA.classfunc()  # 类调用类方法