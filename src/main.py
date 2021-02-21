# Author : Sergey Alexandrovich Kravchuk
# Email  : spam.reg.box@ya.ru
# License: GPLv3
"""Invoice Clients for generate date base

Create and add invoice, calculate time * multiplay for cost and write.
Generate html,mail and text viewers

example:
    <program name> <key> <name>

"""

import sys
import persone

def main_loop():
    """Select action interactive

        set_name = name db from db/<name>.csv
        operand  = select action from set_setname, run not argv
                   show help info <Persones.__doc__>.

    """

    exit_list = ['y', 'Y', 'yes', 'Yes', 'YES']
    quit = 'No'

    while quit not in exit_list:

        print(persone.Persones.__doc__)
        set_name = input('input name: ')
        operand = input('input operand: ')

        person = persone.Persones(set_name)

        if operand:
            person.action(operand)
        else:
            print('--\n\nUsing: %s <key> <name db>\n\n%s' % \
                 (sys.argv[0], persone.Persones.__doc__))

        quit = input('\n--\n Exit y?: ')

    print('\n\n--\nProgram user exit!\n')

def select_action():
    """Select action fast result. """

    set_name = sys.argv[2]
    operand = sys.argv[1]
    person = persone.Persones(set_name)

    person.action(operand)


def main():

    if len(sys.argv) > 2:
        select_action()
    else:
        main_loop()

if __name__ == "__main__" :
    main()
