import pickle
avto1=["Волга","Белый","1970"]
avto2=["Жигули", "Красный", "1980"]
avto3=["Победа","Зеленый", "1950"]
marka=input("\nВведите марку автомобиля ")
color=input("\nВведите цвет автомобиля ")
god=input("\nВведите год автомобиля ")
avto4=[marka,color,god]
zap=open("avto.dat","wb")
pickle.dump(avto1,zap) #консервация данных
pickle.dump(avto2,zap)
pickle.dump(avto3,zap)
pickle.dump(avto4,zap)
zap.close()
#--------------------------------
zap=open("avto.dat","rb+")
avto1=pickle.load(zap) #расконсервация данных
avto2=pickle.load(zap)
avto3=pickle.load(zap)
avto4=pickle.load(zap)
print(avto1)
print(avto2)
print(avto3)
print(avto4)
zap.close()