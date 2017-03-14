# Игра <<ОЧКО>>

import random

k = [2,3,4,5,6,7,8,9,10,11]
k2 = [11,10,9,8,7,6,5,4,3,2]
i = random.choice(k)
i2 = random.choice(k2)
print('Приветствую вас в игре "ОЧКО"\nВам выпало:',i,'\nДилер:',i2)
exit = 1
while exit == 1:
    if i == 21 and i2 == 21:
            print('Ничья,Продолжаем играть ? (Y/n)')
            d = input()
            if d == 'y' or d == 'Y':
                print('Продолжаем.')
                i = random.choice(k)
                i2 = random.choice(k2)
                print('Ваш счет:',i)
                print('Дилер:',i2)
            else:
                input('Выход из программы,нажмите Enter чтобы выйти...')
                exit = 0
    elif i == 21:
            print('Вы выиграли, набрав 21 очко.')
            print('Хотите начать играть заного? (Y/n)')
            d = input()
            if d == 'y' or d == 'Y':
                print('Продолжаем.')
                i = random.choice(k)
                i2 = random.choice(k2)
                print('Ваш счет:',i)
                print('Дилер:',i2)
            else:
                input('Выход из программы,нажмите Enter чтобы выйти...')
                exit = 0
    elif i2 == 21:
            print('Дилер выиграл,набрав 21 очко !')
            print('Хотите начать играть заного ? (Y/n)')
            d = input()
            if d == 'y' or d == 'Y':
                print('Продолжаем.')
                i = random.choice(k)
                i2 = random.choice(k2)
                print('Ваш счет:',i)
                print('Дилер:',i2)
            else:
                input('Выход из программы,нажмите Enter чтобы выйти...')
                exit = 0
    elif i > 21: 
            print('Вы проиграли, набрав больше 21 очка.')
            print('Хотите начать игру заново? (Y/n)')
            d = input()
            if d == 'y':
                print('Продолжаем.')
                i = random.choice(k)
                i2 = random.choice(k2)
                print('Ваш счет:',i)
                print('Дилер:',i2)
            else:
                input('Выход из программы,нажмите Enter чтобы выйти...')
                exit = 0    
    elif i2 > 21:
            print('У дилера перебор,Вы выиграли :)\nХотите начать игру заного? (Y/n)')
            d = input()
            if d == 'y' or d == 'Y':
                print('Продолжаем.')
                i = random.choice(k)
                i2 = random.choice(k2)
                print('Ваш счет:',i)
                print('Дилер:',i2)
            else:
                input('Выход из программы,нажмите Enter чтобы выйти...')
                exit = 0               
    elif i < 21:
            print('У вас меньше 21 очка, добавить еще одну карту? (Y/n)')
            d = input()
            if d == 'y' or d == 'Y':           
                print('Добавляем карту.')
                i = i + random.choice(k)
                print('Ваш счет:',i)
                print('Дилер:',i2)
            if i2 < 21:
                if i > 21:
                    n = input('Вы проиграли,Хотите начать игру заного ? (Y/n)\n')
                    if n == 'y' or n == 'Y':
                        print('Продолжаем.')
                        i = random.choice(k)
                        i2 = random.choice(k2)
                        print('Ваш счет:',i)
                        print('Дилер:',i2)
                    else:
                        input('Выход из программы,нажмите Enter чтобы выйти...')
                        exit = 0
                if i == 21:
                    print('Вы выиграли, набрав 21 очко.')
                    print('Хотите начать играть заного? (Y/n)')
                    s = input()
                    if s == 'y' or s == 'Y':                        
                        print('Продолжаем.')
                        i = random.choice(k)
                        i2 = random.choice(k2)
                        print('Ваш счет:',i)
                        print('Дилер:',i2)
                    else:
                        input('Выход из программы,нажмите Enter чтобы выйти...')
                        exit = 0
                print('Дилер берет карту ? (Y/n)')
                d2 = input()
                if d2 == 'y' or d2 == 'Y':
                    print('Добавляем карту.')
                    i2 = i2 + random.choice(k2)
                    print('Ваш счет:',i)
                    print('Дилер:',i2)
            else:
                input('Выход из программы,нажмите Enter чтобы выйти...')
                exit = 0
