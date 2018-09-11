
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import os
import chardet


def find_in_file(what, where):
    where = where.lower()
    return what in where


def find_in_files(what, files):
    pool = []
    for file in files:
        try:
            with open(file, 'rb') as f:
                data = f.read()
                result = chardet.detect(data)
                if find_in_file(what, data.decode(result['encoding'])):
                    pool.append(file)
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
    return pool


def print_files(files, str):
    print('Всего найдено {} ф., содержащих строку {}:'.format(len(files), str))
    for file in files:
        print(file)


migrations = 'Migrations'
migrations_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), migrations)

files = [f for f in os.listdir(migrations_dir) if f.endswith('.sql')]
files = list(map(lambda f: os.path.join(migrations_dir, f), files))
main_list = files

while True:
    str_to_find = input('Введите строку для поиска: ').lower()
    if not str_to_find:
        break
    files = find_in_files(str_to_find, files)
    print_files(files, str_to_find)
    if not files:
        files = main_list





