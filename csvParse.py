import csv
from pprint import pprint
def csvParse(fileName):
	with open(fileName, encoding='utf-8') as r_file:
    		# Создаем объект reader, указываем символ-разделитель ","
    		file_reader = csv.reader(r_file, delimiter=",")
    		# Счетчик для подсчета количества строк и вывода заголовков столбцов
    		count = 0
    		# Считывание данных из CSV файла
    		table = []
    		for row in file_reader:
        		line = []
        		for item in row:
            			line.append(int(item))
        		table.append(line)
    		return table
