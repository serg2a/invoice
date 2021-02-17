# Author : Sergey Alexandrovich Kravchuk
# License: GPLv3

"""Generate settings for file.
new object("name configuration file")
return dict
"""

import os
from all_persone import All_persone

class Configure(All_persone):
    """
    Input configure file name, defaults configure file name
    if file not found using default file
    return dictionary

    example configure file:

    name=Foo
    age=2
    # - comment string

    """


    data_base = {
            'head_list'  : ['date','discribe','time','cost'],
            'table_list' : ['№','Дата','Услуга','Оплата','Цена']
           }
    FOLDER_CONF = "../conf/"

    def __init__(self, filename:str="default") -> dict:
        super().__init__(filename)
        filename = os.path.join(self.FOLDER_CONF, filename + ".conf")

        if os.path.isfile(filename):
            for string in open(filename):
                flag = False
                name = value = ""

                for char in string:
                    if char == "#":
                        break
                    if char == "\n":
                        continue
                    if char == "=":
                        flag = True
                        continue
                    if flag:
                        value += char
                    else:
                        name += char
                        continue
                if name:
                   self.data_base[name]=value

    def __set(self):
        pass

    conf = property(lambda x: x.data_base, __set)

if __name__ == "__main__":
    test = Configure()
    print(f"Name person: {test.name}\n--\n")
    print(test.conf)
