def counterpartCharCode(char):
    ulc = char.isupper()
    if ulc == True:
        nc = char.lower()
    else:
        nc = char.upper()
    return ord(nc)


counterpartCharCode('a')