# Игра <<Кости>>

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
    print("\nCделайте ставку! Размер - от 2 до 12\n")
    while True:
        ## Делаем ставку
        St = int(input(name0 + ',Введите вашу ставку: '))
        # генерируем числа 1 - 6
        a = random.randint(1, 6)
        b = random.randrange(6) + 1
        total = a + b
        print("\nПервая кость:", a, "Вторая кость:", b, "В сумме:", total)

        # Выводим результат
        if total == St:
             print('Ура, вы Выиграли',name0)
             input('\nНажмите Enter,чтобы выйти...')
             break
        else:
             chance = int(input('Вы не угадали :(\n\nСыграем еще раз ?\n1.Да\n2.Нет\n'))
             if chance == 1:
                 continue
             else:
                 input("\n\nНажмите Enter,чтобы выйти...")
                 break
                
#Игра с компьютером
elif user == 2:
    print("Выбран режим игры 'Компьютер vs Пользователь'!")
    name = input('Игрок, введите Ваше имя: ')
    print("\nCделайте ставку! Размер - от 2 до 12")
    #Делаем ставки
    while True:
        s1 = int(input(name + ',Введите вашу ставку: '))
        s2 = random.randint(2,12)
        print('Ставка компьютера - ', s2)
        # генерируем числа 1 - 6
        a = random.randint(1, 6)
        b = random.randrange(6) + 1
        total = a + b
        print("\nПервая кость:", a, "Вторая кость:", b, "В сумме:", total)

        # Выводим результат
        if total == s1 and total != s2:
            print('Ура, вы Выиграли',name)
            input('\nНажмите Enter,чтобы выйти...')
            break
        elif total != s1 and total == s2:
            print('Победил Компьютер !')
            input('\nНажмите Enter,чтобы выйти...')
            break
        elif total == s1 and total == s2:
            print('Ничья !')
            input('\nНажмите Enter,чтобы выйти...')
            break
        else:
            chance1 = int(input('Ставка не прошла! :(\n\nСыграем еще раз ?\n1.Да\n2.Нет\n'))
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
    print("\nCделайте ставку! Размер - от 2 до 12")
    # Делаем ставки
    while True:
        s1 = input(name1 + ', Введите вашу ставку: ')
        s1 = int(s1)
        s2 = input(name2 + ', Введите вашу ставку: ')
        s2 = int(s2)
        # генерируем числа  1 - 6
        a = random.randint(1, 6)
        b = random.randrange(6) + 1
        total = a + b
        print("\nПервая кость:", a, "Вторая кость:", b, "В сумме:", total)

        # Выводим результат
        if s1 == total and total != s2:
            print('Победитель -', name1,',Поздравляем !')
            input('\nНажмите Enter,чтобы выйти...')
            break
        elif s1 != total and total == s2:
            print('Победитель -', name2,',Поздравляем !')
            input('\nНажмите Enter,чтобы выйти...')
            break
        elif s1 == total and total == s2:
            print('Ничья!')
            input('\nНажмите Enter,чтобы выйти...')
            break
        else:
            chance2 = int(input('Ставка не прошла! :(\n\nСыграем еще раз ?\n1.Да\n2.Нет\n'))
            if chance2 == 1:
                 continue
            else:
                 input("\n\nНажмите Enter,чтобы выйти...")
                 break

else:
    print('Неверный выбор!!!')
    input('\nPlease, press enter to exit...')
