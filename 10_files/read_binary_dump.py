import pickle

print('Вас приветствует программа сохранения списка автомобилей!')
print('сейчас будет выведено всё содержимое файла "auto.dat"\n')
file = open("auto.dat","rb")
automobiles = pickle.load(file)

i=1
for auto in automobiles:
    print('Автомобиль номер',i)
    print("модель:", auto[0])
    print("год выпуска:", auto[1])
    print("цвет авто:", auto[2])
    print("примечания:", auto[3])
    print()
    i+=1

print('КОНЕЦ СПИСКА')
file.close()
