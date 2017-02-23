# Игра <<Кости>> V2.0

print("\t\tДобро пожаловать в игру \"Кости\"!")
print('\n')

import random

print('Как будем играть?')
print('1 - Один игрок.')
print('2 - Играем с компьютером.')
print('3 - Играем с другом.')
user = int(input('\nСделайте Ваш выбор: '))

#Один игрок
if user == 1:
    print("Выбран режим игры 'Одиночка'!")
    name0 = input('Игрок, введите Ваше имя: ')
    balance = int(input('Введите баланс: '))
    print("\nCделайте ставку! Размер - от 2 до 12\n")
    while True:
        ## Делаем ставку
        St = int(input(name0 + ',Введите вашу ставку: '))
        #Проверка на ставку
        if St < 2 or St > 12:
            print('Не верная ставка,попробуйте снова !\n')
            continue
        
        # генерируем числа 1 - 6
        a = random.randint(1, 6)
        b = random.randrange(6) + 1
        total = a + b
        print("\nПервая кость:", a, "Вторая кость:", b, "В сумме:", total)

        # Выводим результат
        if total == St:
             balance = balance + St
             print('Ура, вы Выиграли',name0)
             print('Ваш баланс состовляет: ',balance)
             chance0 = int(input('\n\nСыграем еще раз ?\n1.Да\n2.Нет\n'))
             if chance0 == 1:
                 continue
             else:
                 input("\n\nНажмите Enter,чтобы выйти...")
                 break
        else:
             balance = balance - St
             print('\nВы не угадали :(\n')
             print('Ваш баланс состовляет: ',balance)
             #Проверка баланса на значение NULL
             if balance == 0:
                 input('На вашем балансе нету денег !\nПриходите к нам снова :)\n\nНажмите Enter,чтобы выйти...')
                 break
             elif balance < 0:
                 input('Вы задолжали нам денег.\nЖдите гостей !!!\nНажмити Enter,чтобы выйти...')
                 break
             chance = int(input('Сыграем еще раз ?\n1.Да\n2.Нет\n'))
             if chance == 1:
                 continue
             else:
                input("\n\nНажмите Enter,чтобы выйти...")
                break
                
#Игра с компьютером
elif user == 2:
    print("Выбран режим игры 'Компьютер vs Пользователь'!")
    name = input('Игрок, введите Ваше имя: ')
    balance1 = int(input('Введите баланс: '))
    balancePC = int(input('Введите баланс компьютеру: '))
    print("\nCделайте ставку! Размер - от 2 до 12")
    #Делаем ставки
    while True:
        s1 = int(input(name + ',Введите вашу ставку: '))
        #Проверка на ставку
        if s1 < 2 or s1 > 12:
            print('Не верная ставка,попробуйте снова !\n')
            continue
        s2 = random.randint(2,12)
        print('Ставка компьютера - ', s2)
        # генерируем числа 1 - 6
        a = random.randint(1, 6)
        b = random.randrange(6) + 1
        total = a + b
        print("\nПервая кость:", a, "Вторая кость:", b, "В сумме:", total)

        # Выводим результат
        if total == s1 and total != s2:
            balance1 = balance1 + s1
            balancePC = balancePC - s2
            print('Ура, вы Выиграли',name)
            print('Ваш баланс состовляет: ',balance1)
            print('Баланс компьютера состовляет: ',balancePC)
            # Проверка баланса на значение NULL
            if balance1 <= 0:
                input('\nНа вашем счете закончились средства!\n\nНажмите Enter чтобы выйти...')
                break
            if balancePC <=0:
                input('\nНа счете компьютера закончились средства!\nВы выиграли :)\n\nНажмите Enter чтобы выйти...')
                break  
            chance1 = int(input('Сыграем еще раз ?\n1.Да\n2.Нет\n'))
            if chance1 == 1:
                 continue
            else:
                 input("\n\nНажмите Enter,чтобы выйти...")
                 break
            
        elif total != s1 and total == s2:
            balance1 = balance1 - s1
            balancePC = balancePC + s2
            print('Победил Компьютер !')
            print('Ваш баланс состовляет: ',balance1)
            print('Баланс компьютера состовляет: ',balancePC)
            input('\nНажмите Enter,чтобы выйти...')
            # Проверка баланса на значение NULL
            if balance1 <= 0:
                input('\nНа вашем счете закончились средства!\n\nНажмите Enter чтобы выйти...')
                break
            if balancePC <=0:
                input('\nНа счете компьютера закончились средства!\nВы выиграли\n\nНажмите Enter чтобы выйти...')
                break  
            chance1 = int(input('Сыграем еще раз ?\n1.Да\n2.Нет\n'))
            if chance1 == 1:
                 continue
            else:
                 input("\n\nНажмите Enter,чтобы выйти...")
                 break

        elif total == s1 and total == s2:
            print('Ничья !')
            print('Ваш баланс состовляет: ',balance1)
            print('Баланс компьютера состовляет: ',balancePC)
            input('\nНажмите Enter,чтобы выйти...')
            continue
        else:
            print('Ставка не прошла! :(\n')
            balance1 = balance1 - s1
            balancePC = balancePC - s2
            print('Ваш баланс состовляет: ',balance1)
            print('Баланс компьютера состовляет: ',balancePC)
            # Проверка баланса на значение NULL
            if balance1 <= 0:
                input('\nНа вашем счете закончились средства!\n\nНажмите Enter чтобы выйти...')
                break
            if balancePC <=0:
                input('\nНа счете компьютера закончились средства!\nВы выиграли\n\nНажмите Enter чтобы выйти...')
                break  
            chance1 = int(input('Сыграем еще раз ?\n1.Да\n2.Нет\n'))
            if chance1 == 1:
                 continue
            else:
                 input("\n\nНажмите Enter,чтобы выйти...")
                 break

#Игра с другом
elif user == 3:
    print("Выбран режим игры 'На двоих'!")
    name1 = input('Игрок 1, введите Ваше имя: ')
    name2 = input('Игрок 2, введите Ваше имя: ')
    print(name1)
    balanceName1 = int(input('Введите ваш баланс: '))
    print(name2)
    balanceName2 = int(input('Введите ваш баланс: '))
    print("\nCделайте ставку! Размер - от 2 до 12")
    # Делаем ставки
    while True:
        #Проверка на ставку
        s1 = input(name1 + ', Введите вашу ставку: ')
        s1 = int(s1)
        if s1 < 2 or s1 > 12:
            print('Не верная ставка,попробуйте снова !\n')
            continue
        s2 = input(name2 + ', Введите вашу ставку: ')
        s2 = int(s2)
        if s2 < 2 or s2 > 12:
            print('Не верная ставка,попробуйте снова !\n')
            continue
        # генерируем числа  1 - 6
        a = random.randint(1, 6)
        b = random.randrange(6) + 1
        total = a + b
        print("\nПервая кость:", a, "Вторая кость:", b, "В сумме:", total)

        # Выводим результат
        if s1 == total and total != s2:
            balanceName1 = balanceName1 - s1
            print('Выиграл -', name1,',Поздравляем !')
            print('\nВаш баланс',name1,'состовляет: ',balanceName1)
            print('Ваш баланс',name2,'состовляет: ',balanceName2)
            input('\nНажмите Enter,чтобы выйти...')
            break
        elif s1 != total and total == s2:
            balanceName2 = balanceName2 - s2
            print('Выиграл -', name2,',Поздравляем !')
            print('\nВаш баланс',name1,'состовляет: ',balanceName1)
            print('Ваш баланс',name2,'состовляет: ',balanceName2)
            input('\nНажмите Enter,чтобы выйти...')
            break
        elif s1 == total and total == s2:
            print('Ничья!')
            print('\nВаш баланс',name1,'состовляет: ',balanceName1)
            print('Ваш баланс',name2,'состовляет: ',balanceName2)
            input('\nНажмите Enter,чтобы выйти...')
            break
        else:
            balanceName1 = balanceName1 - s1
            balanceName2 = balanceName2 - s2
            print('Ставка не прошла! :(')
            print('\nВаш баланс',name1,'состовляет: ',balanceName1)
            print('Ваш баланс',name2,'состовляет: ',balanceName2)
            # Проверка баланса на значение NULL
            if balanceName1 <= 0:
                print('\nНа вашем счете',name1,'закончились средства!')
                print('Победил',name2,'Поздравляем !')
                input('\n\nНажмите Enter чтобы выйти...')
                break
            if balanceName2 <=0:
                print('\nНа вашем счете',name2,'закончились средства!')
                print('Победил',name1,'Поздравляем !')
                input('\n\nНажмите Enter чтобы выйти...')
                break  
            chance1 = int(input('Сыграем еще раз ?\n1.Да\n2.Нет\n'))
            if chance1 == 1:
                 continue
            else:
                 input("\n\nНажмите Enter,чтобы выйти...")
                 break
            chance2 = int(input('\nСыграем еще раз ?\n1.Да\n2.Нет\n'))
            if chance2 == 1:
                 continue
            else:
                 input("\n\nНажмите Enter,чтобы выйти...")
                 break

else:
    print('Неверный выбор!!!')
    input('\nНажмите Enter,чтобы выйти...')
