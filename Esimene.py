print("Tere! Olen sinu uus sõber - Python!")#Teksti sisestamine ekraanile
nimi=input ("Mis on sinu nimi?")#teksti sisestamiseks
if nimi.isalpha()==True:
    print (f"{nimi}, oi kui ilus nimi")#Tekstiväljund
else:
    print("See ei ole nimi")#kontroll
i=int(input("Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))#teksti sisestamiseks
if i==1:
    pikk=""
    while type(pikk) !=float:
            try:
                pikk=float(input("Sisestage oma pikus =>"))#arvi sisestamiseks
            except:
                    TypeError#kontroll
    mass=""
    while type(mass) !=float:
            try:
                mass=float(input("Sisestage oma mass =>"))#arvi sisestamiseks
            except:
                    TypeError#kontroll
    if (pikk>20 and pikk<270) and (mass>1 and mass<495):#piiranguid
            indeks=mass/(0.01*pikk)**2
            print('Sinu indeks on',round(indeks,1),"кг/м²")#Tekstiväljund
            if indeks<16:
                print(f"Tervisele ohtlik alakaal")#Tekstiväljund
            elif indeks>16 and indeks<19:
                print (f"Alakaal")#Tekstiväljund
            elif indeks>19 and indeks<25:
                print(f"Normaalkaal")#Tekstiväljund
            elif indeks>25 and indeks<30:
                print(f"Ülekaal")#Tekstiväljund
            elif indeks>30 and indeks<35:
                print(f"Rasvumine")#Tekstiväljund
            elif indeks>35 and indeks<40:
                print(f"Tugev rasvumine")#Tekstiväljund
            elif indeks>40:
                print(f"Tugev rasvumine")#Tekstiväljund
    else:
        print("kahjuks, sa oled suri")#andmed ei sobi
else:
    print("See on kasulik info!")#info ei sobi
print()

import random
ver = 0
print(input(f'Добро пожаловать в игру камень/ножницы/бумага эта игра на смерть,если вы проиграете компьютеру,то вы умираете.У вас есть одна попытка выиграть компьютер.Удачи!Вы готовы?'))
print('1 - камень')
print('2 - ножницы')
print('3 - бумага')
while (ver == 0):
        player = int(input("Выбери что-то из указаного выше =>"))
        if (player == 1 or player == 2 or player == 3):
            ver = 1    
if player == 1:
        print("Вы выбрали камень.")  
if player == 2:
        print("Вы выбрали ножницы.") 
if player == 3:
        print("Вы выбрали бумагу.")  
computer = random.randint(1, 3)
if computer == 1:
        print("Компьютер выбрал камень.") 
if computer == 2:
        print("Компьютер выбрал ножницы.")
if computer == 3:
        print("Компьютер выбрал бумагу.")
if player == computer:# определяем победителя
        win = 0
if player == 1 and computer == 2:
        win = 1 
if player == 1 and computer == 3:
        win = 2 
if player == 2 and computer == 1:
        win = 2  
if player == 2 and computer == 3:
        win = 1 
if player == 3 and computer == 1:
        win = 1
if player == 3 and computer == 2:
        win = 2
if win == 0:
        print("Ничья!")
if win == 1:
        print("Победил игрок!")
if win == 2:
        print("Победил компьютер!")