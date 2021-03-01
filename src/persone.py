# Author : Sergey Alexadrovich Kravchuk
# Email  : spam.reg.box@ya.ru
# License: GPLv3


from .dbdisp import Data_gen
from .all_persone import All_persone
from .gensetting import Configure
from .viewer import mail, web



class Persones(Configure):
    """Select and request date base invoice

    Select action (write, read or remove string of invoice_file)
    default invoice   : invoice.csv
    default configure : default.conf

    Operand:
        -w write new record
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
        self.db = Data_gen(self.conf)

    def sum_invoice(self) -> float:
        """Count sum for column dict <invoice['cost']> and return sum"""

        return sum((float(rec['cost'])) for rec in self.db.dict)


    def web(self, page=10):
        return web.generate_html(self.db.dict, self.sum_invoice(),
                                 self.conf, page)

    def print_db(self):
        """View db clients for text table std output """

        self.db.join()
        print('\n', *self.conf['head_list'], sep='\t')
        for line in self.db.list:
            print(*line, end='', sep='\t')
        print('\n')


    def print_sum(self):
        """Print sum all colums in cost for db """

        print(self.sum_invoice(), self.conf['money'])


    def print_web(self):
        """View html for text table"""

        print(web.generate_html(self.db.dict,
              self.sum_invoice(), self.conf))


    def print_subject_mail(self):
        """Create subject for mail, output subject mail"""
        print(self.conf['email_s'], self.sum_invoice(), 
              self.conf['money'], self.conf['corp'])


    def print_mail(self):
        """View text for email message clients invoice """

        print(mail.generate_text(
              self.conf,self.sum_invoice()))


    def write(self):
        """
        Write record for conf['invoice_file'] is input_generator().
        """

        invoice_list = []
        invoice_list.append(self.db.input_generator())

        if len(invoice_list) > 0:
            self.db.write(invoice_list)


    def action(self, operand):
        """Select action form list"""

        if operand == '-p' or operand == 'p': self.print_db()
        elif operand == '-s' or operand == 's': self.print_sum()
        elif operand == '-web' or operand == 'web': self.print_web()
        elif operand == '-mail' or operand == 'mail': self.print_mail()
        elif operand == '-smail' or operand == 'smail': self.print_subject_mail()
        elif operand == '-w' or operand == 'w': self.write()
        elif operand == '-q' or operand == 'q' : exit()
        else:
            print('\nERROR Operand!!!\
                    \nOperand not correct, please switch correct operand!!!')
            exit(1)

#
# test
#
if __name__ == "__main__":
    test = Persones("braga")
    test.action('p')
    test.action('s')
    test.action('mail')
    test.action('web')
