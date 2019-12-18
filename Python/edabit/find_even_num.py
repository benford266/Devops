def find_even_nums(num):
    evens = []
    for i in range(0,num+1):
        if (i % 2) == 0:
            evens = evens +[i]

    return evens