
class Student():  # 类方法
    name = ''  # 类变量
    age = 0
    sum = 0

    def __init__(self, name, age):  # self代表的是实例
        self.name = name  # 对实例变量进行赋值
        self.age = age
        self.__score = 0  # 加__变成私有变量
        # print('student')
        # print(self.name)
        self.__class__.sum += 1
        print('当前班级学生总数为:'+str(self.__class__.sum))

    def marking(self, score):
        self.__score = score
        if score < 0:
            return '分数不能为负数'
        print(self.name+'本次考试分数为:'+str(self.__score))

    # 行为与特征
    # 类方法
    def do_homework(self):
        self.do_engilsig_homework()  # 内部调用方法
        print('do homework now')
        # self.__class__.sum += 1
        # print('当前班级学生总数为:'+str(self.__class__.sum))

    def do_engilsig_homework(self):
        print()

    # 类方法 #装饰器
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    # 静态方法
    @staticmethod
    def add(x, y):
        print(Student.sum)
        print('This is a static method')


Student1 = Student('xiaobai', 18)
Student2 = Student('xiaohei', 18)
resule = Student1.marking(-1)  # 调用marking的方法
print(resule)


# Student1.do_homework()
# 不建议使用这种方法修改值
Student1.__score = -1  # python通过.为新增变量,所以不会报错
print(Student1.__score)
# print(Student1.__dict__)  # 与students进行对比检测
print(Student2._Student__score)  # 访问私有变量

# r = Student1.score
# 公开的public私有的private
# print(Student1.score)


# 静态方法调用
# Student1.add(1, 2)
# Student.add(1, 2)
# 类方法的调用
# Student1.plus_sum()
# Student1.do_homework() #调用其它实例方法
# 实例方法调用
# Student2 = Student('xiaohei', 18)
# Student1.plus_sum()
# Student3 = Student('xiaoming', 18)
# Student1.plus_sum()


# print(Student1.name)
# print(Student.sum)
# print(Student1.__dict__)
# print(Student.__dict__)
