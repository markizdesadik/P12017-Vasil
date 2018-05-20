import re
import os
import datetime

today = datetime.datetime.today()

folder = os.getcwd() + '\Отчеты\\'
file_list = os.listdir(folder + '\\')
dogovor = 'Договор_поставки'
antiword = os.getcwd() + '\\antiword\\'
text_in_doc = []
client = 'Покупатель: '
num_dogovor = ''
client = ''
data = ''
pokypka = 'Покупатель: '
num = 'Договор поставки '

for file_in in file_list:
    if not file_in.find(dogovor):
        if os.path.exists(folder + 'replaced_file.doc'):
            os.remove(folder + 'replaced_file.doc')
        os.rename(folder + file_in, folder + 'replaced_file.doc')

        os.system(
            'E://Pyexe/antiword/antiword.exe -m cp1251 ' + folder + 'replaced_file.doc > ' + folder + 'new_file.txt')
        with open(folder + 'new_file.txt', 'r') as file:
            for row in file:
                text_in_doc.append(row)

        for stroka in text_in_doc:
            if client:
                continue
            else:
                if pokypka in stroka:
                    client = (
                        stroka[len(pokypka):].replace(' ', '').replace('|', '').replace('\n', '').replace('"', ''))
                    print(client)

            fuu = re.search(r'\d\d\d\d.[г]', stroka)
            print(fuu)
            if fuu:
                data = (stroka.replace(' ', '').replace('г.', '_').replace('|', '').replace('\n', ''))

            if num_dogovor:
                continue
            else:
                if num in stroka:
                    num_dogovor = (
                        stroka[len(num) + 1:].replace(' ', '').replace('/', '_').replace('|', '').replace('\n',
                                                                                                          '').replace(
                            '№', 'N'))
                    print(num_dogovor)

        rename_file = 'договор {} {} от {}{}.doc'.format(client, num_dogovor, data, today.microsecond)
        os.rename(folder + 'replaced_file.doc', folder + rename_file)
