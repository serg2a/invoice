#!/bin/bash

if [ -n "$1" ]
  then
      pos="$1"
  else
      pos="sasha"
fi

cd ..
#./invoice.sh -web $pos > $pos.html
#scp $pos.html serg2a.tk:/home/serg/html/invoice/$pos.html
scp db/$pos.csv serg2a.tk:/home/serg/html/invoices/invoice/db/$pos.csv
scp conf/$pos.conf serg2a.tk:/home/serg/html/invoices/invoice/conf/$pos.conf
#rm $pos.html
cd -
