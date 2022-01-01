def begin(): # Прифветствие и объявление правил игры
    print('--------------------------------')
    print('           ПРИВЕТСТВУЮ!!!\n\n'
          '      ЭТО ИГРА КРЕСТИКИ-НОЛИКИ\n\n'
          '           ПРАВИЛА ИГРЫ:\n'
          'Игроки ходят по очереди внося координаты\n'
          'поля в котором хотят поставить X или Y\n'
          'координаты вводятся в виде двух цифр от 1 до 3 через пробел\n'
          'в свледующем порядке Х=    У=  \n'
          'побеждает игрок собравший в линию три X или три 0\n'
          'по горизонтали, вертикали или диагонали'
          )
    print('--------------------------------')

field = [[' ']*3 for i in range(3)] # Создаётся список полей


def Game_field():  # Функция вывовода полей на экран
    print(f'  |  0  |  1  |  2  |\n' # номера столбцов поля
          f'_____________________'
          )
    for i in range(3):    # цикл собирает игровое поле
        line = f"{i} |  {'  |  '.join(field[i])}  |" # сборка линии игрового поля {i} - выводмт номер линии
        print(line)
        print('_____________________')

def move():     # Функция проверки пользовательсого кода
    while True:
        coordinates = input('  Ввидите координаты').split()

        if len(coordinates) != 2:      # Проверка сколько пользователь ввёл координат
            print('    Нужно ввести две координаты')
            continue
        x, y = coordinates

        if not (x.isdigit()) or not (y.isdigit()):   # Проверка является ли введённые данные цифрой (числом)
            print('    Введите цифры')
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:    # Проверка данных на вхождение в диапазон от 0 до 2
            print('    Значения выходят за рамки диапазона\n'
                  '    введите значения Х и У от 0 до 2'
                  )
            continue
        if field[x][y] != ' ':        # Проверка свободна ли клетка с такими координатами
            print('   Клетка занята ')
            continue
        return x, y


def winer():        # Определение побдителя
    for i in range(3):
        win_card = []
        for j in range(3):
            win_card.append(field[i][j])    # Определение по строке
        if win_card == ['X', 'X', 'X']:
            print('Х - ПОБЕДИЛИ!!!!')
            return True
        if win_card == ['0', '0', '0']:
            print('0 - ПОБЕДИЛИ!!!!')
            return True

    for i in range(3):
        win_card = []
        for j in range(3):
            win_card.append(field[j][i])   # Определение по столбцу
        if win_card == ['X', 'X', 'X']:
            print('Х - ПОБЕДИЛИ!!!!')
            return True
        if win_card == ['0', '0', '0']:
            print('0 - ПОБЕДИЛИ!!!!')
            return True

    win_card = []
    for i in range(3):
        win_card.append(field[i][i])       # Определение по основной диагонали
    if win_card == ['X', 'X', 'X']:
        print('Х - ПОБЕДИЛИ!!!!')
        return True
    if win_card == ['0', '0', '0']:
        print('0 - ПОБЕДИЛИ!!!!')
        return True

    win_card = []
    for i in range(3):
        win_card.append(field[i][2 - i])    # Определение по вторичной диагонали
    if win_card == ['X', 'X', 'X']:
        print('Х - ПОБЕДИЛИ!!!!')
        return True
    if win_card == ['0', '0', '0']:
        print('0 - ПОБЕДИЛИ!!!!')
        return True



begin()
nam_muve = 0       # Счётчик ходов
while True:        # Основной цикл
    nam_muve += 1
    Game_field()

    if nam_muve % 2 == 0:     # Определение очерёдности хода
        print('      Ходит Х')
    else:
        print('      Ходит 0')
    x, y = move()

    if nam_muve % 2 == 0:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if winer():
        break

    if nam_muve == 9:
        print('       Ничья!')
        break

