# 继承
from c6 import Human


class Student(Human):
    name = 'xiaohao'
    age = 0
    # sum = 0

    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)
        # Human.__init__(self, name, age)  # 调用父类的构造函数,进行初始化
        # self.__score = 0
        # self.__class__.sum += 1

    def do_homework(self):
        super(Student, self).do_homework()  # 调用父类普通的实例方法
        print('homework')


Student1 = Student('xiaoxue', 'xiaobai', 18)
Student1.do_homework()
# Student.do_homework(Student1) #调用类的实例方法,多此一举操作
# print(Student1.sum)
# print(Student.sum)
# print(Student1.name)
# print(Student1.age)
# Student1.get_name()
