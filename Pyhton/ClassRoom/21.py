# Игра <<Двадцать одно>>

import random

k = [2,3,4,5,6,7,8,9,10,11]
k2 = [11,10,9,8,2,3,4,5,6,7]
i = random.choice(k) #Игрок
i2 = random.choice(k2) #Дилер
print('Добро пожаловать в игру "Двадцать одно" !!!\nЦель игры набрать в сумме 21 очко.\nДавайте начнем.\n\nВам выпало:',i,'\nДилер:',i2)
exit = 1
while exit == 1:
    #Проверка на ничью.
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
                break
    #Проверка на 21 у Игрока.
    elif i == 21:
            print('Вы выиграли, набрав 21 очко.')
            print('Хотите начать играть заново? (Y/n)')
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
                break
    #Проверка на 21 у Дилера.
    elif i2 == 21:
            print('Дилер выиграл,набрав 21 очко !')
            print('Хотите начать играть заново ? (Y/n)')
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
                break
    #Проверка на число больше 21 у Игрока.
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
                break
    #Проверка на число больше 21 у Дилера.
    elif i2 > 21:
            print('У дилера перебор,Вы выиграли :)\nХотите начать игру заново? (Y/n)')
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
                break
    #Проверка на меньшее число у Дилера и Игрока.
    elif i < 21:
            print('\nУ вас меньше 21 очка, добавить еще одну карту? (Y/n)')
            d = input()
            if d == 'y' or d == 'Y':
                print('Добавляем карту.')
                i = i + random.choice(k)
                print('Ваш счет:',i)
            if i2 < 21:
                if i > 21:
                    n = input('\nВы проиграли :(\nХотите начать игру заново ? (Y/n)\n')
                    if n == 'y' or n == 'Y':
                        print('Продолжаем.')
                        i = random.choice(k)
                        i2 = random.choice(k2)
                        print('Ваш счет:',i)
                        print('Дилер:',i2)
                    else:
                        input('Выход из программы,нажмите Enter чтобы выйти...')
                        exit = 0
                        break
                if i == 21:
                    print('Вы выиграли, набрав 21 очко.')
                    print('Хотите начать играть заново? (Y/n)')
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
                        break
                print('Дилер берет карту ? (Y/n)')
                d2 = input()
                if d2 == 'y' or d2 == 'Y':
                    print('Добавляем карту.')
                    i2 = i2 + random.choice(k2)
                    print('Дилер:',i2)
                #Проверка на отмену карты у Дилера и Игрока.
                if d == 'n' and d2 == 'n':
                    print('Ваш счет:',i)
                    print('Дилер:',i2)
                    if i < 21 and i < i2:
                        print('\nДилер выиграл !')
                        input("Заходите к нам снова :)\n\nНажмите Enter,чтобы выйти...")
                        break
                    if i2 < 21 and i2 < i:
                        print('\nВы выиграли !')
                        input("Заходите к нам снова :)\n\nНажмите Enter,чтобы выйти...")
                        break
                    if i == i2:
                        print('\nНичья !')
                        input("Заходите к нам снова :)\n\nНажмите Enter,чтобы выйти...")
                        break
