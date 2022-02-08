def greet():
    print('Welcome to the tic-tac-toe!')
    print('input data format: x, y')
    print('x - is the line number')
    print('y - is the column number')

field = [[' ']*3 for i in range(3)]
num = 0

def show():
    print()
    print('     | 0  | 1  | 2  |')
    print('   -------------------')
    for i, row in enumerate(field):
        row_inf = f"  {i}  |  {' |  '.join(field[i])} |"
        print(row_inf)
        print('  --------------------')
    print()

def ask():
    while True:
        cor = input('make a move...').split()
        if len(cor) != 2:
            print('Input TWO numbers!')
            continue

        x, y = cor

        if not (x.isdigit()) or not (y.isdigit()):
            print('input the NATURAL NUMBERS!')
            continue

        x, y = int(x), int(y)

        if 0 <= x <=2 and 0<= y <=2 :
            if field[x][y] == ' ':
                return x, y
            else:
                print('The cage is occupied! try again...')
                continue
        else:
            print('The values is out of the range! try again...')
            continue

    return x, y

def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print("X is winner!")
            return True
        if symbols == ["0", "0", "0"]:
            print("0 is winner")
            return True
    return False

greet()

while True:
    num += 1
    show()
    if num % 2 == 1:
        print('X make a move: ')
    else:
        print('0 make a move: ')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'x'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if num == 9:
        print('Standoff!')
        break






