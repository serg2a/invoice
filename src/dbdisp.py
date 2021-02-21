# Author : Sergei Alexandrovich Kravchuk
# License: GPLv3
# Email  : spam.reg.box@ya.ru

import os
import sys
import datetime
import gentime


class Data_gen:
    """Manipulation db(db name.csv)

    Read and write for db, create list db_invoice
    """
    def __init__(self, settings):
        self.invoice_list = []
        self.invoice_dict = []
        self.settings = settings
        self.file = self.settings['invoice_file']
        self.head = self.settings['head_list']
        self.sep = self.settings['sep']

        self.read()

    def read(self):
        """Read of invoice from file *.csv for list invoice_list. """

        if os.path.isfile(self.file):
            for string in open(self.file):
                self.invoice_list.append(string.split(self.sep))
            for rec in self.invoice_list:
                self.invoice_dict.append(dict(zip(self.head,rec)))

    def list(self):
        return self.invoice_list

    def dict(self):
        return self.invoice_dict


    def write(self, invoice_list):
        """Add write of invoice for list invoice_list. """
        if os.path.isfile(self.file):
            with open(self.file, "a") as fd:
                fd.writelines(invoice_list.pop())


    def input_generator(self) -> list:
        """Input and check date, description, ... in order """

        tmp = []
        multipler = float(self.settings['multipler'])

        for head_list in self.head:

            if head_list == 'date':
                tmp.append(datetime.datetime.today().
                           strftime('%Y/%m/%d') + self.sep)

            elif head_list == 'time':
                ok = input('calculate for time y/n?:')
                if ok == 'y' or ok == 'Y':
                    times = gentime.gen(input('example 12:12-13:30 time:\n'))
                    if times:
                        tmp.append(times + self.sep)
                    else:
                        print('Fall: Not correct input')
                        return 0;
                else:
                    tmp.append('0' + self.sep)

            elif head_list == 'cost':
                if tmp[2] != '0' + self.sep : # time 
                    print('time_cost')
                    tmp.append(str(float(tmp[2].replace(self.sep, ""))*multipler) + self.sep)
                else:
                    print('cost')
                    tmp.append(str(input(head_list + ": ") + self.sep))

            else:
                tmp.append(str(input(head_list + ": ") + self.sep))

        tmp.append("\r\n")

        return tmp
