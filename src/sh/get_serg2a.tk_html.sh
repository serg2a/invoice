#!/bin/bash

if [ -n "$1" ]
  then
      pos="$1"
  else
      pos="sasha"
fi

cd ..
./invoice.sh -web $pos > $pos.html
scp $pos.html serg2a.tk:/home/serg/html/invoice/$pos.html
scp db/$pos.csv serg2a.tk:/home/serg/html/invoice/db/$pos.csv
rm $pos.html
cd -
