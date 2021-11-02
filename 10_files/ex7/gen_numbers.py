#Данная программа создаёт файл и записывает в неё определённую последовательность случайных чисел 

import random

amount=int(input('Введите длинну последовательности случайных чисел: '))
start = input('Введите начало диапазона выбора случайных чисел (0 по умолчанию): ')
stop = input('Введите конец диапазона выбора случайных чисел (999 по умолчанию): ')
name = input('введите название файла вывода (.txt по умолчанию): ')




#заполняем пустые значения
if start == '':
    start = 0
if stop ==  '':
    stop = 999

start = int(start)
stop = int(stop)

#убираем пользовательское расширение
if not '.' in name:
    name+='.txt'

file_numbers = open(name, "w", encoding='utf-8')

#записываем столбик/строку рандомных чисел
#делаем первую итерацию отдельно, чтобы потом нормально переносить строку
random_number = random.randrange(start, stop+1,1)
file_numbers.write(str(random_number))

for _ in range(amount-1):
    file_numbers.write(' ') #'\n'-столбик, ' ' - строка
    random_number = random.randrange(start, stop+1,1)
    file_numbers.write(str(random_number))
    
print(f'в файл "{name}" было записано {amount} случайных чисел в диапазоне от {start} до {stop}.')
print('Завершение работы.')

file_numbers.close()