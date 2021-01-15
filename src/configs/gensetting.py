# Author : Sergey Alexandrovich Kravchuk
# License: GPLv3
"""Generate settings for file.

If file not found then using default configure

"""

import os

def gen_sett(filename:str, def_conf) -> dict:
    """Function generate dictionary from file

    input configure file name, defaults configure file name
    if file not found using default file
    return dictionary

    example configure file:
      name=Foo
      age=2

    # - comment string

    """

    if os.path.isfile(filename):
        with open(filename, 'r') as conf_file:
            const_dict = {}

            for line in conf_file:
                flag = 0
                name = value = ""

                for char in line:
                    if char == "#":
                        break
                    if char == "\n":
                        continue
                    if char == "=":
                        flag = 1
                        continue
                    if flag == 0:
                        name += char
                        continue
                    if flag == 1:
                        value += char

                if name != "":
                    const_dict[name]=value

        return const_dict

    elif os.path.isfile(def_conf):
        print('\nFor this name configure file  NOT FOUND!!!\
              \nUsing %s' % def_conf)
        return gen_sett(def_conf, def_conf)

    else:
        print('\n\n\nFATAL ERROR!!! Default configure file not found: %s' %\
              def_conf)
        return False


if __name__ == "__main__":
    print('input test')
