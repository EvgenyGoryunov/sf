def privetstvie():                          # функция приветствия и ввода данных игроков
    print('\nДобро пожаловать в игру "Крестики-нолики"" ')
    global name_player_1
    name_player_1 = input('\nВведите имя первого игрока: ')
    name_player_1 = name_player_1.title()
    print(f'Приветствую, {name_player_1}, ты будешь играть крестиками')
    global name_player_2
    name_player_2 = input('\nВведите имя второго игрока: ')
    name_player_2 = name_player_2.title()
    print(f'Приветствую, {name_player_2}, ты будешь играть ноликами')
    print('\nЧтобы сделать ход, необходимо ввести координаты ячейки')
    print('сначала номер строки, затем столбца')

privetstvie()



field = [[" "]*3 for i in range(3)]         # переменной field присваивается значение в виде списка, состоящий из
                                            # трех списков, состоящих из трех пробелов ([" "]*3)


def create_field():                         # функция создания поля
    print('\n  |  0  |  1  |  2  |')        # создание верхней строчки с цифрами
    print('---------------------')          # создание подчеркивания под цифрами
    for i in range(len(field)):
        print(str(i) + " |  " + "  |  ".join(field[i]) + "  |  ")       # формирование горизонтальных строк через склеивание аргументов
                                                                        # значение i склеить с пробелом и | и так 3 раза
        print("---------------------")                                  # условное подчеркивание новых строк, для красоты


def xod():                                                              # функция ввода координат хода
    while True:
        xod = input("\nВаш ход, сначала строки, затем столбцы: ").split()       # вводим координаты и разбиваем их на два значения
        if len(xod) != 2:
            print("\nВводить можно только две координаты и через пробел!")
            continue
        if not(xod[0].isdigit()) or not (xod[1].isdigit()):                     # блок проверки, чтоб игрок не ввел буквы
            print("\nВводить можно только числа!")
            continue
        x, y = map(int, xod)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('\nВведеные координаты вне поля игры (0-2)!')
            continue
        if field[x][y] != " ":
            print("\nКлетка занята, введи другие координаты")
            continue
        break
    return x, y


def win_check():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            create_field()
            print("\nВыиграл X")
            print(f"\nПоздравляю, {name_player_1}, ты - best of the best!!!")
            return True
        if symbols == ["0", "0", "0"]:
            create_field()
            print("\nВыиграл 0")
            print(f"\nПоздравляю, {name_player_2}, ты - best of the best!!!")
            return True
    return False



count = 0
while True:
    count += 1
    create_field()

    if not count % 2 == 0:          # реализован алгорит поочередного хода, если остатка нет, ходит Х и т.д.
        print("Крестик ходит")
    else:
        print("Нолик ходит")

    x, y = xod()                    # берем параметры Х и У из функции "хода"

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_check():
        break

    if count == 9:
        print("Ничья")
        break