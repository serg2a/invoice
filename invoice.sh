#!/bin/bash
#
#--------------------------------------------------------------------------
#This file is part of invoice.
#
#    invoice is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License.
#
#    invoice is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with invoice.  If not, see <https://www.gnu.org/licenses/>.
#
#--------------------------------------------------------------------------
#
# Author: Sergey Alexandrovich Kravchuk
# License: GPLv3
# Email: spam.reg.box@ya.ru

FOLDERS='src'

cd $FOLDERS
python3 main.py $1 $2
cd ..
