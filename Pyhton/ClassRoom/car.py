# Нужно написать программу "Автомобиль". В программе может быть один или несколько классов, в каждом из которых прописаны необходимые атрибуты и методы.
# Объект Автомобиль должен иметь необходимый функционал:
# 1. Зажигание
# 2. Езда
# 3. Тормоз
# 4. Остановка двигателя
# 5. Включение фар
# 6. Открытие и закрытие дверей

# Функциональность Автомобиля должна соответствовать логике, т.е. например, нельзя завести автомобиль два раза подрят. Нельзя начать езду если нажат тормоз и так далее.

class ZajiganieIdvijok:
    zajj = "Включили зажигание"
    zajjOff = "Выключили зажигание"
    dvjON = "Завели авто"
    dvjOff = "Заглушили двигатель"
    def dvijokOFF(self):
        print(self.dvjOff)
    def dvijokON(self):
        print(self.dvjON)
    def zajiganie(self):
        print(self.zajj)
    def zajiganieOFF(self):
        print(self.zajjOff)

class Ezda:
    km1 = "Едем со скорость 40 км/час"
    km2 = "Едем со скорость 80 км/час"
    km3 = "Едем со скорость 160 км/час"
    status1 = "Едем"
    status2 = "Стоим"
    def km40(self):
        print(self.km1)
    def km80(self):
        print(self.km2)
    def km160(self):
        print(self.km3)
    def statusEzdaGoing(self):
        print(self.status1)
    def statusEzdaStop(self):
        print(self.status2)

class Tormoz:
    s = "Остановили авто"
    def stop(self):
        print(self.s)
        
class Lights:
    f1 = "Включили фары"
    f2 = "Выключили фары"
    f3 = "Включите зажигание!"
    def fariON(self):
        print(self.f1)
    def fariOFF(self):
        print(self.f2)
    def ErrorFari(self):
        print(self.f3)
        
class Doors:
    dv = "Открыли дверь"
    dv1 = "Закрыли дверь"
    def doorsOpen(self):
        print(self.dv)
    def doorsClose(self):
        print(self.dv1)
    

#Обьекты.
zaj = ZajiganieIdvijok()
ezda = Ezda()
tormoz = Tormoz()
far = Lights()
doors = Doors()


def menu():
    print("""                               KuvaldinCar:
1.Зажигание
2.Двигатель
3.Езда
4.Тормоз
5.Включить/Выключить фары
6.Открытие и закрытие дверей
0.Выход""")


def main():
    zajiganie = 0 #Проверка зажигания.
    countDvijok = 0 #Проверка состояние двигателя.
    goOrNot = 0 #Проверкa движения автомобиля.
    faru = 0 #Проверка включения/выключения фар.
    door = 0 #Проверка открыта или закрыта дверь.
    vMahine = 0 #Проверка на наличие пользователя в авто.
    while exit != '0':   
        selection = input('')
        if selection == '1': # Зажигание
            if vMahine == 0:
                print("Сядьте в машину !")
                menu()
                continue
            print("Зажигание:\n1 - Включить/2 - Выключить?")
            z = input('')
            if z == '1':
                if zajiganie == 1:
                    print("Зажигание и так включено !")
                    menu()
                    continue
                zaj.zajiganie()
                zajiganie = 1
                menu()
            elif z == '2':
                if countDvijok == 1:
                    print("Заглушите двигатель !")
                    menu()
                    continue
                elif zajiganie == 0:
                    print("Зажигание и так  выключено !")
                    menu()
                    continue
                zaj.zajiganieOFF()
                zajiganie = 0
                menu()
        elif selection == '2': #Двигатель
            if vMahine == 0:
                print("Сядьте в машину !")
                menu()
                continue
            print("Завести двигатель (1 - Завести/2 - Заглушить/3 - Выйти в меню.) ?")
            s = input("")
            if s == '1':
                if zajiganie == 0:
                    print("Включите зажигание,чтобы завести двигатель !")
                    menu()
                    continue
                elif countDvijok == 1:
                    print("Двигатель уже заведен,его можно только заглушить.\nГлушим двигатель (Y/n) ?")
                    gd = input('')
                    if gd == 'Y' or gd == 'y':
                        if goOrNot == 1:
                            print("Остоновите автомобиль чтобы заглушить двигатель!")
                            menu()
                            continue
                    zaj.dvijokOFF()
                    countDvijok = 0
                    menu()
                    continue    
                zaj.dvijokON(),print('\n')
                countDvijok = 1
                menu()
            elif s == '2':
                if countDvijok == 0:
                    print("Двигатель и так заглушен,думайте что жмете !\n")
                    menu()
                    continue
                elif goOrNot == 1:
                    print("Остановитесь,чтобы заглушить двигатель !")
                    menu()
                    continue
                zaj.dvijokOFF()
                countDvijok = 0
                menu()
            elif s == '3':
                menu() 
        elif selection == '3': #Езда
            if countDvijok == 1:
                if door == 1:
                    print("Закройте дверь,чтобы начать движение !")
                    menu()
                    continue
                print("С какой скоростью будем ехать ?\n1.40км/час.\n2.80км/час.\n3.160км/час.")
                speed = input('')
                if speed == '1':
                    ezda.km40()
                    goOrNot = 1
                    menu()
                elif speed == '2':
                    ezda.km80()
                    goOrNot = 1
                    menu()
                elif speed == '3':
                    ezda.km160()
                    goOrNot = 1
                    menu()
            else:
                print("Заведите двигатель чтобы ехать!")
                menu()
                continue
        elif selection == '4': #Тормоз
            if countDvijok == 1 and goOrNot == 1:
                goOrNot = 0
                tormoz.stop()
                menu()
            else:
                print('Вы стоите на месте,зачем тормозить ?\nПрокатитесь с ветерком на KuvaldinCar и потом жмите на тормоз.')
                menu()
        elif selection == '5': #Фары
            if zajiganie == 1:
                print("Включить - 1\nВыключить - 2")
                fr = input('')
                if fr == '1':
                    if faru == 1:
                        print("Фары уже включены !")
                        menu()
                        continue
                    far.fariON()
                    faru = 1
                    menu()
                elif fr == '2':
                    if faru == 0:
                        print("Фары уже выключены !")
                        menu()
                        continue
                    far.fariOFF()
                    faru = 0
                    menu()
            else:
                print("Включите зажигание !")
                menu()
        elif selection == '6': #Двери
            if vMahine == 1:
                print("Вы находитесь в машине,вы можете только:\n1 - Закрыть дверь")
                mmm = input('')
                if mmm == '1':
                    if door == 0:
                        print("Дверь уже закрыта !")
                        menu()
                        continue
                    doors.doorsClose()
                    door = 0
                    menu()
                    continue
            if door == 1:
                print("Дверьи открыты уже, вы можете:\n1 - Сесть в авто\n2 - Закрыть дверь.")
                mm = input('')
                if mm == '1':
                    print("Вы сели в Авто.")
                    vMahine = 1
                    menu()
                    continue
                elif mm == '2':
                    doors.doorsClose()
                    door = 0
                    menu()
                    continue
            print("1 - Открыть дверь.\n2 - Закрыть дверь.")
            d = input('')
            if d == '1': 
                if goOrNot == 1:
                    print("Вы находитесь в движении !")
                    menu()
                    continue
                elif door == 1:
                    print("Дверь и так открыта !")
                    menu()
                    continue
                doors.doorsOpen()
                door = 1
                print("Хотите сесть в авто ?\n1 - Да\n2 - Нет")
                m = input('')
                if m == '1':
                    print("Вы сели в Авто.")
                    vMahine = 1
                    menu()
                else:
                    menu()
            elif d == '2':
                if door == 0:
                    print("Дверь и так закрыта !")
                    menu()
                    continue
                doors.doorsClose()
                door = 0
                menu()
        elif selection == '0': # Exit
            input("\nНажмите Enter,чтобы выйти...)")
            break
            
#Вызов функций.            
menu()
main()
