
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

import glob
import os.path

def get_searching_result(list_of_files, string):
		search_result = []
		for file in list_of_files:
				with open(file) as f:
						data = f.read()
						if string in data:
								search_result.append(file)
		return search_result

def print_searching_result(list_of_files):
		for file in list_of_files:
				print('{}'.format(file))
		print('Всего: {}'.format(len(list_of_files)))

def search(files):
		search_string = str(input('Введите строку для поиска (для выхода введите q):'))
		if search_string != 'q':
				print_searching_result(get_searching_result(files, search_string))
				temp_files = []
				for file in get_searching_result(files, search_string):
						temp_files.append(file)
				return search(temp_files)
		else:
				print('Работа программы завершена')

migrations = 'Migrations'
files = glob.glob(os.path.join(migrations, "*.sql"))
print(os.path.join(migrations, "*.sql"))
print(files)

