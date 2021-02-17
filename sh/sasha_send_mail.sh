#!/bin/bash

if [ -n "$1" ]
  then
      pos="$1"
  else
      pos="sasha"
fi

email="sasha" # abook using record email address 
#email="serg2ak@ya.ru" # copy duble

echo -n "send mail to $email: "
cd ..
./invoice.sh -mail $pos > mail
subject="$(./invoice.sh smail $pos)"
mutt $email -s "$subject" < mail
echo "ok"
rm mail
cd -
