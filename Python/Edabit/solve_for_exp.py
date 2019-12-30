def solve_for_exp(a,b):
    counter = 1
    h = 0
    while h != b:
        h = a ** counter
        counter = counter +1
    return counter - 1

solve_for_exp(4, 1024)