def wave(str):
    stringarr = []
    newarry = []
    stringarr = list(str)
    i = 0
    while i != len(str):
        if stringarr[i] != ' ':
            stringarr[i] = stringarr[i].upper()
            join = ''.join(stringarr)
            newarry.append(join)
            stringarr[i] = stringarr[i].lower()
            i = i +1
        else:
            i = i +1
        
    return newarry