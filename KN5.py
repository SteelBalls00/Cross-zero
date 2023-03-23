but1 = [i for i in range(1,10)] # [1, 2, 3, 4, 5, 6, 7, 8, 9] - пронумерованное поле для понимания что выбирать игроку
but2 = ['-' for i in range(9)] # ['-', '-', '-', '-', '-', '-', '-', '-', '-', ] - пустое поле, элементы которого будем заменять каждым ходом


def check(i, user):
   if ((but2[0] == but2[1] == but2[2] == i) or # Проеряем одинаковость клеток на Х или О
           (but2[3] == but2[4] == but2[5] == i) or
           (but2[6] == but2[7] == but2[8] == i) or
           (but2[0] == but2[3] == but2[6] == i) or
           (but2[1] == but2[4] == but2[7] == i) or
           (but2[2] == but2[5] == but2[8] == i) or
           (but2[0] == but2[4] == but2[8] == i) or
           (but2[2] == but2[4] == but2[6] == i)):
      print(f'Победил {user}')
      return False
   elif '-' not in but2: # Проеряем заолненность поля
      print('Поле заполнено - НИЧЬЯ!')
      return False
   else:
      return True


def turn(per, znach): # ход игрока
   tn = (int(input(f'Ход {per} игрока. Введите номер клетки: '))) # ввод номера клетки поля
   while tn>9 or tn<1 or but2[(tn - 1)] != '-': # проверка на пустую клетку
      tn = (int(input("Введите число незанятой клетки от 1 до 9: ")))
   but2[(tn - 1)] = znach # установка в клетку Х или О игрока

def printab(tabl): # вывод игрового поля
   print(f'|\t\t|\t\t|\t\t|')
   print(f'|\t{tabl[6]}\t|\t{tabl[7]}\t|\t{tabl[8]}\t|')
   print(f'|\t\t|\t\t|\t\t|')
   print('-------------------------')
   print(f'|\t\t|\t\t|\t\t|')
   print(f'|\t{tabl[3]}\t|\t{tabl[4]}\t|\t{tabl[5]}\t|')
   print(f'|\t\t|\t\t|\t\t|')
   print('-------------------------')
   print(f'|\t\t|\t\t|\t\t|')
   print(f'|\t{tabl[0]}\t|\t{tabl[1]}\t|\t{tabl[2]}\t|')
   print(f'|\t\t|\t\t|\t\t|')


print('''Новая игра. Сетка представлена в виде пронумерованных клеток, как на num-pad(е) клавиатуры.
Для выбора клетки вам потребуется ввести цифру с ее номером.''')
printab(but1) # начало игры

last = None
game = True
while game: # цикл запуска функций для игры, который хз как остановить
   turn(per='первого', znach='X')
   printab(but2)
   game = check('X', user='игрок 1')
   if not game:
      break
   turn(per='второго', znach='O')
   printab(but2)
   game = check('O', user='игрок 2')