# Игра <<ОЧКО>>

import random

k = [2,3,4,5,6,7,8,9,10,11]
i = random.choice(k)
print('Приветствую вас в игре <<ОЧКО>>\nВам выпало:',i)
exit = 1
while exit == 1:
	if i == 21:
		print('Вы выиграли, набрав 21 очко.')
		print('Хотите продолжить играть? (Y/n)')
		d = input()
		if d == 'y':
			print('Продолжаем.')
			i = random.choice(k)
			print(i)
		else:
			print('Выход из программы.')
			exit = 0
	elif i > 21:
		print('Вы проиграли, набрав больше 21 очка.')
		print('Хотите начать игру заново? (Y/n)')
		d = input()
		if d == 'y':
			print('Продолжаем.')
			i = random.choice(k)
			print(i)
		else:
			print('Выход из программы.')
			exit = 0
	elif i < 21:
		print('У вас меньше 21 очка, добавить еще одну карту? (Y/n)')
		d = input()
		if d == 'y':
			print('Добавляем карту.')
			i = i + random.choice(k)
			print(i)
		else:
			print('Выход из программы.')
			exit = 0
