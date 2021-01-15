#!/bin/bash

DEFAULT_MAIL="you_email@you.dom"

if [ -n "$1" ]
  then
      pos="$1"
  else
      pos="$DEFAULT_MAIL"
fi

email="$DEFAULT_MAIL"

echo -n "send mail to $email: "
cd ..
./invoice.sh -mail $pos > mail
subject="$(./invoice.sh smail $pos)"
mutt $email -s "$subject" < mail
echo "ok"
rm mail
cd -
