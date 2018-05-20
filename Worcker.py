#!/usr/bin/python
# -*- coding: utf-8 -*-
# Labotskiy Vasiliy

"""
Меняет название файла "Заявка_на_снабжение N 1147483 от 14.05.2018 (1865621053460189965).xls'"
на "'Заявка СТО СТЕБЕНЕВА ' + time + '.xls'"
"""

import os
import datetime

today = datetime.datetime.today()
folder = os.getcwd() + '\\Отчеты\\'
zakaz = 'Заявка_на_снабжение'
file = os.listdir(folder)
time = ""
time = str(today.day) + '.' + str(today.month) + '.' + str(today.year) + ' ' + str(today.hour) + '.' + str(today.minute)

for f in file:
    lis = ''
    s = os.path.basename(f)
    for i in s:
        lis += i
    if not lis.find(zakaz):
        os.rename(folder + f,
                  folder + 'Заявка СТО СТЕБЕНЕВА ' + time + '.xls')
