# Author : Sergey Alexandrovich Kravchuk
# Email  : spam.reg.box@ya.ru
# License: GPLv3

from os import sep
import configs.gensetting as gen_setting
import dbdisp
from viewer import mail, web


FOLDER_CONF = '..' + sep + 'conf' + sep
DEFAULT_CONF = FOLDER_CONF + 'default.conf'
SETTINGS = {
            'head_list'  : ['date','discribe','time','cost'],
            'table_list' : ['№','Дата','Услуга','Оплата','Цена']
           }

class Persones:
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

    def __init__(self, set_update):

        """Initial date base, create list and dict """

        if set_update:
            SETTINGS.update(gen_setting.gen_sett(FOLDER_CONF + set_update +\
                                                 '.conf', DEFAULT_CONF))
        else:
            SETTINGS.update(gen_setting.gen_sett
                           (DEFAULT_CONF, DEFAULT_CONF))

        self.DB = dbdisp.read_invoice(SETTINGS)
        self.DB_DICT = dbdisp.invoice_dict(self.DB, SETTINGS)

    def sum_invoice(self) -> float:
        """Count sum for column dict <invoice['cost']> and return sum"""

        return sum((float(rec['cost'])) for rec in self.DB_DICT)

    def web(self, page=10):
        return web.generate_html(self.DB_DICT, self.sum_invoice(), SETTINGS, \
                                 page)

    def view(self, operand):
        def print_db():

            """View db clients for text table std output """

            print('\n', *SETTINGS['head_list'], sep='\t')
            for line in self.DB:
                print(*line, end='', sep='\t')
            print('\n')

        def print_sum():
            """Print sum all colums in cost for db """

            print(self.sum_invoice(), SETTINGS['money'])

        def print_web():
            """View html for text table"""

            print(web.generate_html(self.DB_DICT,
                  self.sum_invoice(), SETTINGS))

        def print_subject_mail():
            """Create subject for mail, output subject mail"""
            print(SETTINGS['email_s'], self.sum_invoice(), SETTINGS['money'], SETTINGS['corp'])

        def print_mail():
            """View text for email message clients invoice """

            print(mail.generate_text(
                  SETTINGS,self.sum_invoice()))


        if operand == 'p'      : print_db()
        elif operand == 's'    : print_sum()
        elif operand == 'web'  : print_web()
        elif operand == 'mail' : print_mail()
        elif operand == 'smail': print_subject_mail()



    def write(self):
        """
        Write record for SETTINGS['invoice_file'] is input_generator().
        """

        invoice_list = []
        invoice_list.append(dbdisp.input_generator(SETTINGS))
        dbdisp.write_invoice(invoice_list, SETTINGS['invoice_file'])

    def web_write(self, rec:list):
        """Write record for SETTINGS['invoice_file'] is get request"""

        pass

    def dellite_record(self):
        pass

    def update_record(self):
        pass

    def edit_record(self):
        pass


    def read_settings(self):
        pass


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
