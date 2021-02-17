# Author : Sergey Alexandrovich Kravchuk
# Email  : spam.reg.box@ya.ru
# License: GPLv3

class All_persone:
    def __init__(self, name):
        self.__name = name

    def __set(self, name):
        if name:
            self.__name = name

    name = property(lambda x: x.__name, __set)
