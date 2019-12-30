def return_unique(lst):
    returner = []
    for i in lst:
        q = lst.count(i)
        if q == 1:
            returner = returner +[i]

    return returner
    

return_unique([2, 2, -19, 2, 7, 7, 4, 9, 9, 0, 0, 3, 3, 3])