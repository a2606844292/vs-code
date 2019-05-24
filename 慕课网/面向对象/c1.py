# 面向对象
# 有意义的面向对象的代码
# 类、对象
# 实例化
# 类最基本的作用:封装
# 模板


class Student():
    name = ''
    age = 0
    # 行为与特征

    def do_homework(self):
        print('homework')


class Printer(Student):
    def print_file(self):
        print('name' + self.name)
        print('age'+str(self.age))


# 方法和函数的区别
# 方法:设计层面 函数:程序运行、过程式的一种称谓
# student = Student()  # 实例化
# student.print_file()
printer = Printer()  # 实例化
printer.print_file()
