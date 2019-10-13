#! towerbuilder.py


def tower_builder(n_floors):
    n = n_floors
    output = []
    for floor in range(n_floors):
        n -= 1
        floornew = ' ' * n
        print(floornew)
        test = floor * 2 + 1
        star = '*' * test
        string = floornew + star + floornew
        print(floor)
        output.append(string)

    return output

    