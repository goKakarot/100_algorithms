class Animal(object):
    def run(self):
        print('animal is runnning!!')


class Cat(Animal):
    """this is qiaozhi's private class"""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def mew(self):
        print('name is ' + self.__name.title() + ', mew mew mew')

    def its_age(self):
        print(self.__name.title() + ' is ' + str(self.__age) + ' months old')

    def getter_name(self):
        return self.__name

    def setter_name(self, new_name):
        self.__name = new_name
        return self.__name

    def run(self):
        print('cat is running!')
        super().run()

    def __call__(self, *args, **kwargs):
        print('dont try to call the instance')

    def __str__(self):
        return 'direct call of cat'


class Base(object):
    def __init__(self):
        print('Base init')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A init')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B init')

class C(A, B):
    def __init__(self):
        super().__init__()
        print('c init')
c = C()
print(C.__mro__)