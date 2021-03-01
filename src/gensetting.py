# Author : Sergey Alexandrovich Kravchuk
# License: GPLv3

"""Generate settings for file.
new object("name configuration file")
return dict
"""

import os
import sys
from .all_persone import All_persone

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


    def __init__(self, name:str="default"):
        super().__init__(name)

        self.data_base = data_gen(self.name)

    def __set(self):
        pass


    conf = property(lambda x: x.data_base, __set)

#
# functions
#
def data_gen(filename):
    data_base = {
            'head_list'  : ['date','discribe','time','cost'],
            'table_list' : ['№','Дата','Услуга','Оплата','Цена']
           }
    FOLDER_CONF = "conf/"
    filename = os.path.join(FOLDER_CONF, filename + ".conf")

    if os.path.isfile(filename):
        for string in open(filename):
            name = string.split('=',1)[0].strip()
            value = string.split('=',1)[-1].split('#')[0].strip()

            if len(name) > 0:
              data_base[name]=value
    else:
        print("File not found!!!\n", file=sys.stderr)
        exit(1)


    return data_base

#
# test
#
if __name__ == "__main__":
    test = Configure()
    print(f"Name person: {test.name}\n--\n")
    print(test.conf)
