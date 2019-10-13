def find_outlier(integers):
    odd = 0
    even = 0
    lodd = 0
    leven=0
    if len(integers) < 3:
        return 1
    else:
        for i in integers:
            if (i % 2) == 0:
                even = even +1
                leven = i
            else:
                odd = odd +1 
                lodd = i
    if even > 1:
        return lodd
    else:
        return leven