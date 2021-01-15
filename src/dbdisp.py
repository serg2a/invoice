# Author : Sergei Alexandrovich Kravchuk
# License: GPLv3
# Email  : spam.reg.box@ya.ru
"""Manipulation db(db name.csv) 

Read and write for db, create list db_invoice
"""
import datetime

def read_invoice(settings)->list:
    """Read of invoice from file *.csv for list invoice_list. """

    tmp_list = []
    invoice_list = []
    new_line = ''
    sep = settings['sep']

    try:
        with open(settings['invoice_file'], 'r') as invoice_file:
            for line in invoice_file:
                for char in line:
                    new_line += char
                    if char == sep:
                       tmp_list.append(new_line.replace(sep, ""))
                       new_line = ''
                invoice_list.append(tmp_list)
                tmp_list = []
    except FileNotFoundError:
        print('\n    File Not Found %s !!!\n\n' % settings['invoice_file'])

    return invoice_list


def invoice_dict(invoice_list:list, settings):
    """Generate invoice dict is invoice list. """
    invoice_dict = []
    for record in invoice_list:
        invoice_dict.append(dict(zip(settings['head_list'], record)))

    return invoice_dict


def write_invoice(invoice_list:list, invoice_file):
    """Add write of invoice for list invoice_list. """

    with open(invoice_file, 'a') as invoice_table:
        for line in invoice_list:
            invoice_table.writelines(line)

    return True


def input_time(times:str='') -> int:
    """Calculate time for input start/time

    return count minute (h*60+m)-(h*60+m)
    example: 22:11-22:12
    return: 1

    input 25 for exit!!!

    return time for minute
    --
    test:

    >>> input_time('13:00-14:00')
    60
    >>> input_time('13:30-14:30')
    60
    >>> input_time('15:30-16:00')
    30
    >>> input_time('25:55-26:55')
    Fall: start time!!!
    0
    >>> input_time('18:30-16:30')
    Fall: Start time < stop time!!!
    0

    """


    if times == '':
        print('input time, example 13:30-15:12\n')
        times = input('time: ')

    times = times.split('-')
    start = times[0].split(':')
    stop = times[1].split(':')

    start_hour = int(start[0])
    start_min = int(start[1])
    stop_hour = int(stop[0])
    stop_min = int(stop[1])


    if start_hour > 24 or start_hour < 0\
            or stop_min > 60 or stop_min < 0:
        print('Fall: start time!!!')
        return 0

    if stop_hour > 24 or stop_hour < 0\
            or stop_min > 60 or stop_min < 0:
        print('Fall: stop time!!!')
        return 0

    if start_hour > stop_hour:
        print('Fall: Start time < stop time!!!')
        return 0

    return ((stop_hour * 60 + stop_min) - (start_hour * 60 + start_min))


def input_generator(settings:dict) -> list:
    """Input and check date, description, ... in order """

    tmp = []
    sep = settings['sep']
    multipler = float(settings['multipler'])

    for head_list in settings['head_list']:

        if head_list == 'date':
            tmp.append(datetime.datetime.today().
                       strftime('%Y/%m/%d') + sep)

        elif head_list == 'time':
            ok = input('calculate for time y/n?:')
            if ok == 'y' or ok == 'Y':
                times = str(input_time())
                if times != 0:
                    tmp.append(times + sep)
                    print(tmp[-1])
                else:
                    print('Fall: Not correct input')
            else:
                tmp.append('0' + sep)

        elif head_list == 'cost':
            if tmp[2] != '0' + sep : # time 
                print('time_cost')
                tmp.append(str(float(tmp[2].replace(sep, ""))*multipler) + sep)
            else:
                print('cost')
                tmp.append(str(input(head_list + ": ") + sep))

        else:
            tmp.append(str(input(head_list + ": ") + sep))

    tmp.append("\r\n")

    return tmp

if __name__ == "__main__":
    import doctest
    doctest.testmod()
