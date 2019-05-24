class Animal:
    def heshui(self):
        print('动物正在喝水')


class Cat(Animal):
    def heshui(self):
        super().heshui()


cat = Cat()
cat.heshui()
