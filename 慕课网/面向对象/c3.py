
class Student():
    name = 'xiaohao'  # 全局变量，类变量
    age = 0

    # 概念:类变量、实例变量

    def __init__(self, name, age):
        # 构造函数
        # 初始化对象的属性
        self.name = name  # 局部变量  #实例变量定义的方式
        self.age = age
        # print('student')
        # 不能返回retun

    # 行为与特征
    def do_homework(self):
        print('homework')


Student1 = Student('xiaobai', 18)  # 默认调用__init__函数，需要传入参数
Student2 = Student('xiaohei', 18)
print(Student1.name, Student1.age)
print(Student2.name)
print(Student.name)
# Student1.__init__()  # 很少去使用该方法调用
