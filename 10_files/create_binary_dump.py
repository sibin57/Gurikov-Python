import pickle
automobiles = []

print('Вас приветствует программа сохранения списка автомобилей!')
print('(чтобы выйти, напишите "выход", или не пишите модель)')


while True:
    model=input('\nвведите производителя и модель: ')
    if model == '' or model == 'выход':
        break
    year = int(input('введите год выпуска: '))
    color = input('введите цвет автомобиля: ')
    coment = input('дополнительные примечания?:')

    print('\nПроверьте, всё ли верно:\n')
    print('модель:', model)
    print('год выпуска:', year)
    print('цвет:', color)
    print('примечания:', coment)
    promt =input('Всё верно?(да/НЕТ): ')
    if promt.lower() == 'да' or promt.lower() == 'д' or promt.lower() == 'yes' or promt.lower() == 'y':
        print('автомобиль внесён в список')
        automobiles.append([model, year, color, coment])
    else:
        print('введите инфорамцию с начала\n')

#    if coment == '' or coment in 'нетуотсутствуют':
#        auto=[model, year, color]
#    else:
#        auto=[model, year, color, coment] 

file = open("auto.dat","wb")
pickle.dump(automobiles, file)
file.close()
print('файл "auto.dat" создан, вся информация сохранена. Предыдушее содержимое файла удалено')