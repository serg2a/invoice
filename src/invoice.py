import sys
import os
import persone

class Invoice():

    def __init__(self, path:str="../conf") -> dict:
        self.path = path
        self.person = {}
        self.loading_persone()


    def loading_persone(self):
        for name in os.listdir(self.path):
            name = name.split('.conf')[0]
            self.person[name] = persone.Persones(name)

    def chek_person(self, name:str) -> bool:
        if name in list(self.person.keys()):
            return True
        return False


    def run(self):
        """Select action interactive

            set_name = name db from db/<name>.csv
            operand  = select action from set_setname, run not argv
                       show help info <Persones.__doc__>.

        """

        exit_list = ['y', 'Y', 'yes', 'Yes', 'YES', 'q', 'quit', '']
        quit = 'No'


        while quit not in exit_list:

            print(persone.Persones.__doc__)
            name = input('input name: ')
            operand = input('input operand: ')

            if operand and self.chek_person(name) :
                self.person[name].action(operand)
            else:
                print('--\n\nUsing: %s <key> <name db>\n\n%s' % \
                     (sys.argv[0], persone.Persones.__doc__))

            quit = input('\n--\n Exit y?: ')

        print('\n\n--\nProgram user exit!\n')

    def action(self):
        """Select action fast result. """

        name = sys.argv[2]
        operand = sys.argv[1]

        if self.chek_person(name):
            self.person[name].action(operand)
        else:
            print("Person not found!")
