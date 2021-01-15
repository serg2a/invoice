#!/bin/bash

if [ -n "$1" ]
  then
      pos="$1"
  else
      pos="sasha"
fi

email="sasha"
#email="serg2ak@ya.ru"

echo -n "generate and send html>>> "
./get_serg2a.tk_html.sh $pos
echo -n "send mail to $email: "
cd ..
./invoice.py -mail $pos > mail
mutt $email -s "счет" < mail
echo "ok"
rm mail
cd -
