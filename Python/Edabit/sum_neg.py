def sum_neg(lst):
    pos = []
    neg = []
    for i in lst:
        if i < 0:
            neg = neg + [i]
        else:
            pos = pos + [i]
    if (len(pos) == 0) and (sum(neg)) == 0:
        anwser =[]
    else:
        anwser = [len(pos),sum(neg)]
    return anwser


sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])


