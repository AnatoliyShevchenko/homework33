class Checkers:
    __pole = {
        1 : ['#','#','#','#','#','#','#','#'],
        2 : ['#','l','l','l','l','l','l','#'],
        3 : ['#','#','#','#','#','#','#','#'],
        4 : ['#','#','#','#','#','#','#','#'],
        5 : ['#','#','#','#','#','#','#','#'],
        6 : ['#','#','#','#','#','#','#','#'],
        7 : ['#','p','p','p','p','p','p','#'],
        8 : ['#','#','#','#','#','#','#','#'],
    }

    def get_position(cls):
        for i in cls.__pole:
            print(cls.__pole[i])

    def set_positionPlOne(cls, a, b, c, d):
        if 'p' in cls.__pole[a][b]:
            if c == a-1 and d == b-1 or d == b+1:
                if cls.__pole[c][d] == 'l':
                    print('надо рубить')
                elif cls.__pole[c][d] == 'p':
                    print('клетка занята')
                else:
                    cls.__pole[a][b] = '#'
                    cls.__pole[c][d] = 'p'
                    print('Ход сделан')
            elif cls.__pole[c-1][d-1] == 'l':
                cls.__pole[c-1][d-1] = '#'
                cls.__pole[a][b] = '#'
                cls.__pole[c][d] = 'p'
                print('Зарубил')
            elif cls.__pole[c-1][d+1] == 'l':
                cls.__pole[c-1][d+1] = '#'
                cls.__pole[a][b] = '#'
                cls.__pole[c][d] = 'p'
                print('Зарубил')
            elif cls.__pole[c+1][d-1] == 'l':
                cls.__pole[c+1][d-1] = '#'
                cls.__pole[a][b] = '#'
                cls.__pole[c][d] = 'p'
                print('Зарубил')
            elif cls.__pole[c+1][d+1] == 'l':
                cls.__pole[c+1][d+1] = '#'
                cls.__pole[a][b] = '#'
                cls.__pole[c][d] = 'p'
                print('Зарубил')
            else:
                print("так ходить нельзя")

    def set_positionPlTwo(cls, a, b, c, d):
        if 'l' in cls.__pole[a][b]:
            if c == a+1 and d == b-1 or d == b+1:
                if cls.__pole[c][d] == 'p':
                    print('надо рубить')
                elif cls.__pole[c][d] == 'l':
                    print('клетка занята')
                else:
                    cls.__pole[a][b] = '#'
                    cls.__pole[c][d] = 'l'
                    print('Ход сделан')
            elif cls.__pole[c-1][d-1] == 'p':
                cls.__pole[c-1][d-1] = '#'
                cls.__pole[a][b] = '#'
                cls.__pole[c][d] = 'l'
                print('Зарубил')
            elif cls.__pole[c-1][d+1] == 'p':
                cls.__pole[c-1][d+1] = '#'
                cls.__pole[a][b] = '#'
                cls.__pole[c][d] = 'l'
                print('Зарубил')
            elif cls.__pole[c+1][d-1] == 'p':
                cls.__pole[c+1][d-1] = '#'
                cls.__pole[a][b] = '#'
                cls.__pole[c][d] = 'l'
                print('Зарубил')
            elif cls.__pole[c+1][d+1] == 'p':
                cls.__pole[c+1][d+1] = '#'
                cls.__pole[a][b] = '#'
                cls.__pole[c][d] = 'l'
                print('Зарубил')
            else:
                print("так ходить нельзя")


n = Checkers()

n.get_position()
n.set_positionPlTwo(2, 2, 3, 3)
n.set_positionPlTwo(3, 3, 4, 4)
n.set_positionPlTwo(2, 6, 3, 7)
n.set_positionPlTwo(3, 7, 4, 6)
n.set_positionPlOne(7, 1, 6, 2)
n.set_positionPlOne(6, 2, 5, 3)
n.set_positionPlTwo(2, 1, 3, 2)
n.set_positionPlTwo(3, 2, 4, 3)
n.set_positionPlTwo(4, 3, 5, 4)
n.set_positionPlTwo(5, 4, 6, 5)
n.set_positionPlTwo(6, 5, 8, 7)
n.set_positionPlTwo(2, 5, 3, 4)
n.set_positionPlTwo(2, 3, 3, 4)
n.get_position()