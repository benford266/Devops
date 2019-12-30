def duplicate_count(txt):
    counter = 0
    dit = dict(txt)
    for i in dit:
        countc = txt.count(i)
        if countc > 2:
            counter = counter + 1


    print(counter)

duplicate_count('abcda')