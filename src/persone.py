# Author : Sergey Alexadrovich Kravchuk
# Email  : spam.reg.box@ya.ru
# License: GPLv3


import dbdisp as db
from all_persone import All_persone
from gensetting import Configure
from viewer import mail, web



class Persones(Configure):
    """Select and request date base invoice

    Select action (write, read or remove string of invoice_file)
    default invoice   : invoice.csv
    default configure : default.conf

    Operand:
        -w write new column <invoice_file>
        -p print for <invoice_file>
        -s print sum all column cost <invoice_file>
        -web print html <invoice_file>
        -mail print text mail <invoice_file>
        -smail print subject email
        -q exit

    Name default = default

    """

    def __init__(self, name):
        super().__init__(name)

        """Initial date base, create list and dict """
        self.SETTINGS = super().conf
        self.data_base = db.Data_gen(self.SETTINGS)
        self.db_list = self.data_base.list()
        self.db_dict = self.data_base.dict()

    def sum_invoice(self) -> float:
        """Count sum for column dict <invoice['cost']> and return sum"""

        return sum((float(rec['cost'])) for rec in self.db_dict)

    def web(self, page=10):
        return web.generate_html(self.db_dict, self.sum_invoice(),
                                 self.SETTINGS, page)

    def view(self, operand):
        def print_db(self):

            """View db clients for text table std output """

            print('\n', *self.SETTINGS['head_list'], sep='\t')
            for line in self.db_list:
                print(*line, end='', sep='\t')
            print('\n')

        def print_sum(self):
            """Print sum all colums in cost for db """

            print(self.sum_invoice(), self.SETTINGS['money'])

        def print_web(self):
            """View html for text table"""

            print(web.generate_html(self.db_dict,
                  self.sum_invoice(), self.SETTINGS))

        def print_subject_mail(self):
            """Create subject for mail, output subject mail"""
            print(self.SETTINGS['email_s'], self.sum_invoice(), 
                  self.SETTINGS['money'], self.SETTINGS['corp'])

        def print_mail(self):
            """View text for email message clients invoice """

            print(mail.generate_text(
                  self.SETTINGS,self.sum_invoice()))


        if operand == 'p'      : print_db(self)
        elif operand == 's'    : print_sum(self)
        elif operand == 'web'  : print_web(self)
        elif operand == 'mail' : print_mail(self)
        elif operand == 'smail': print_subject_mail(self)



    def write(self):
        """
        Write record for SETTINGS['invoice_file'] is input_generator().
        """

        invoice_list = []
        invoice_list.append(self.data_base.input_generator())

        if len(invoice_list) > 0:
            self.data_base.write(invoice_list)


    def select_action(self, operand):
        """Select action form list"""

        if operand == '-p' or operand == 'p': self.view('p')
        elif operand == '-s' or operand == 's': self.view('s')
        elif operand == '-web' or operand == 'web': self.view('web')
        elif operand == '-mail' or operand == 'mail': self.view('mail')
        elif operand == '-smail' or operand == 'smail': self.view('smail')
        elif operand == '-w' or operand == 'w': self.write()
        elif operand == '-q' or operand == 'q' : exit()
        else: print('\nERROR Operand!!!\
                    \nOperand not correct, please switch correct operand!!!')

if __name__ == "__main__":
    test = Persones("braga")
    test.view('p')
