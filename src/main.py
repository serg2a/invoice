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
from invoice import Invoice


def main():

    persones = Invoice()

    if len(sys.argv) > 2:
        persones.action()
    else:
        persones.run()


if __name__ == "__main__" :
    main()
