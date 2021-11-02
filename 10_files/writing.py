zap=open("avto.txt", "w", encoding='utf-8') #Открываем файл на запись
for i in range(1,3):
    marka=input("\nВведите марку автомобиля ")
    zap.write(marka)
    zap.write("\n") #Перевод курсора на следующую строку
    god=input("\nВведите год выпуска ")
    zap.write(god)
    zap.write("\n")
    color=input("\nВведите цвет машины ")
    zap.write(color)
    zap.write("\n")
zap.close() #Закрываем файл