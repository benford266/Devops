def isValidWalk(walk):
    h = 0
    v = 0
    print(walk)
    if len(walk) == 10:
        for i in walk:
            if i == 'n':
                h = h + 1
            elif i == 's':
                h = h - 1
            elif i == 'e':
                v = v + 1
            elif i =='w':
                v = v - 1
        if (h == 0 and v ==0):
            return True
        else:
            return False

    else:
        return False