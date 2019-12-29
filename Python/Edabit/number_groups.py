def number_groups(group1, group2, group3):
    nl = []
    for i in group1:
        counter1 = group2.count(i)
        counter2 = group3.count(i)
        if counter1 or counter2 > 0:
            nl = nl + [i]

    for i in group2:
        counter1 = group1.count(i)
        counter2 = group3.count(i)
        if counter1 or counter2 > 0:
            nl = nl + [i]

    for i in group3:
        counter1 = group1.count(i)
        counter2 = group2.count(i)
        if counter1 or counter2 > 0:
            nl = nl + [i]

    # removes duplicates by creating dic from list them returning back to list
    nll = list(dict.fromkeys(nl))
    nll.sort()
    return nll




number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3])