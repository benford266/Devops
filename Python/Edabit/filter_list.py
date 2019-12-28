def filter_list(lst):
    nl = []
    for i in lst:
        if type(i) == int:
            nl = nl + [i]
    print(nl)
filter_list([1, 2, "a", "b"])