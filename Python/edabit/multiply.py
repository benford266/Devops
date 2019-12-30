def list_of_multiples(num, length):
    array = []
    t = length + 1
    for i in range(1, t):
        multi = num * i
        array = array + [multi]
    return array

list_of_multiples(5,10)