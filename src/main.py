# Author : Sergey Alexandrovich Kravchuk
# Email  : spam.reg.box@ya.ru
# License: GPLv3
"""Invoice Clients for generate date base

Create and add invoice, calculate time * multiplay for cost and write.
Generate html,mail and text viewers

example:
    <program name> <key> <name>

"""
import os
import sys
import persone
#import threading

#class Loading_prsone(threading.Thread):
#    def __init__(self):
#        threading.Thread.__init__(self)

#    def run(self):
#        loading_persone(self, path)

def loading_persone(path:str="../conf") -> dict:
    name_list = {}
    for name in os.listdir(path):
        name = name.split('.conf')[0]
        print(name)
        name_list[name] = persone.Persones(name)

    return name_list

#th = Loading_persone()
#th.start()
#th.join()

def chek_person(name:str, person:dict) -> bool:
    if name in list(person.keys()):
        return True
    return False

def main_loop(persones:dict):
    """Select action interactive

        set_name = name db from db/<name>.csv
        operand  = select action from set_setname, run not argv
                   show help info <Persones.__doc__>.

    """

    exit_list = ['y', 'Y', 'yes', 'Yes', 'YES', 'q', 'quit']
    quit = 'No'


    while quit not in exit_list:

        print(persone.Persones.__doc__)
        name = input('input name: ')
        operand = input('input operand: ')

        if operand and chek_person(name, persones) :
            persones[name].action(operand)
        else:
            print('--\n\nUsing: %s <key> <name db>\n\n%s' % \
                 (sys.argv[0], persone.Persones.__doc__))

        quit = input('\n--\n Exit y?: ')

    print('\n\n--\nProgram user exit!\n')

def select_action(persones:dict):
    """Select action fast result. """

    name = sys.argv[2]
    operand = sys.argv[1]

    if chek_person(name):
        persones[name].action(operand)
    else:
        print("Person not found!")


def main():

    persones = loading_persone()

    if len(sys.argv) > 2:
        select_action(persones)
    else:
        main_loop(persones)

if __name__ == "__main__" :
    main()
