#Данная программа читает последовательность целых чисел из файла,
#и формирует из неё список удвоенных нечётных чисел.
#После полученный список сортируется и записывается в файл

print('Вас приветсвует программа обработки последовательности чисел')
input_file_name = input('Введите название файла ввода, находящегося в дирректории запуска (.txt по умолчанию): ').lstrip()
output_file_name = input('Введите желаемое название файла вывода (.txt по умолчанию): ').lstrip()

#добавляем txt к названию без расширения
if not '.' in input_file_name:
    input_file_name+='.txt' 
if not '.' in output_file_name:
    output_file_name+='.txt' 


input_file = open(input_file_name,'r', encoding='utf-8')
input_numbers=[int(num) for num in input_file.readline().split()]
input_file.close()

output_numbers = [str(num*2) for num in input_numbers if num%2]
output_file = open(output_file_name, 'w', encoding='utf-8')
output_file.write(' '.join(output_numbers))
output_file.close()

print(f'удвоенные чётные числа из файла "{input_file_name}" записаны в файл "{output_file_name}".')
print('Завершение работы.')
#input = file.readline()