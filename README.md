Автор   : Сергей Александрович Кравчук
Лицензия: GPLv3
Почта   : spam.reg.box@ya.ru

    Приложение на питоне для создания и ведения базы данных услуг, с расчетом 
времени по минутам. Он считывает данные в виде час начала, минуты начала, час 
окончания и минуты окончания работ. Рассчитывает минуты и умножает на 
множитель установленный в "conf/default.conf"

    Перед началом работы создайте свою конфигурацию на основе "conf/default.conf" 
например "conf/consumer.conf" сначала грузится "db/default.conf" потом обновляется 
на ваш, все поля создавать у себя не обязательно.

    Первый запуск производить с ключом -w для генерация данных

Использование:
    python3 invoice.py "-параметр" "имя конфигурации" без .conf если не указан 
    используется "conf/default.conf"
    
    пример: 
        python3 invoice.py -web duda   # Генерация веб страницы duda

    -web  генерация html
    -mail генерация текста сообщения 
    -p    вывод списком 
    -w    добовление записи
    -s    вывести сумму
    -q    выход
