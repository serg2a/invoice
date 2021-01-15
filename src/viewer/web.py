# Author   : Sergei Alexandrovich Kravchuk
# Copyright: GPLv3
# Email    : spam.reg.box@ya.ru
"""Generate_web viewer of html """

import decimal

def generate_html(db:list, summ:float, sett:dict, \
                  page:int=0, page_count:int=10):
    """
   db = A0[B0[,,,,]] 
   title =  A0[name1,name3,name3]
   sum function summ
    """

    html = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta http-equiv="Cache-Control" content="no-cache">
    <title>Счет - %s </title>
    <link rel="stylesheet" href="/style/tab.css">    
    <link rel="stylesheet" href="/style/invoice.css">
  </head>
  <body>
""" % sett['corp']

    def color_digit(digit):
        """Color digit up and down for zero. """
        return 'red' if digit > 0 else 'green'

    def human_digit(digit):
        """Return string human ridable digiting. """
        return '{0:,}'.format(decimal.Decimal(digit)).replace(',', ' ')


    def select_page(pages:list, page:int)->str:
        """List for page select """
        html = '</br><dev class=page> Страница: '

        for p in range(len(pages)):
            if p == page:
                html += '%d' % (p)
            else:
                html += '<a href="?p=%d">%d</a>' % (p, p)

        return html + '</dev></br>'


    def page_counter(db, page_count):
        """Create page list

           return list[(0, page_count), (page_count, page_count + page_count)]
        """

        page = 0
        pages = []

        while len(db) > page:
            page_next = page + page_count
            pages.append((page, page_next))
            page += page_next

        return pages


    money = sett['money']
    titles = sett['table_list']

    html += '<h2>Счет: %s </br>' % sett['corp']
    html += 'Итог: <b style="color:%s">%s %s</b></h2>' % (color_digit
             (summ), human_digit(str(summ)), money)
    html += '<u>Множитель времени: %d </u>' % float(sett['multipler'])
    html += '<table border="0">\n<tr>\n'

    for title in titles:
        html += '<th>%s</th>' % title
    html += '</tr>'

    color = '1'

    db.reverse()

    pages = page_counter(db, page_count)
    start, stop = pages[page]
    num_line = start

    for line in db[start:stop]:
        num_line += 1
        color = '1' if color == '2' else '2'
        html += '<tr class="color%s">' % color
        html += '<td>%s</td>' % num_line
        for record in line:
            if record == 'cost':
                html += '<td align="right"><b style="color:%s">%s %s</b></td>'\
                         % (color_digit(float(line[record])),
                            human_digit(line[record]), money)
            elif record == 'time':
                if line[record] == "0": 
                    html += '<td>Сдельно</td>'
                else:
                    html += '<td>%d:%d</td>' % (int(line[record])//60,
                          int(line[record])%60)
            else:
                html += '<td>%s</td>' % line[record]
        html += '</tr>'

    html += '</table>'

    html += select_page(pages, page)

    html += '</br><a href="%s">Загрузить счет в csv</a>' % \
             sett['invoice_file']
    html += '<p style="font-size:14px;color:#666"><a href="/COPYING_RU.pdf">'
    html += '<img src="/pic/gplv3-or-later.png" alt="GPLv3"></a> </br>&copy;'
    html += '2020 Sergey Kravchuk'
    html += '<a href="/invoice-0.9.tar.bz2">invoice-0.9.tar.bz2</a></p>'
    html += '</body>\n</html>'

    return html
