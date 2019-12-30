def sum_two_smallest_nums(lst):
    lst.sort()
    nlst = [item for item in lst if item >=0]
    anwser = nlst[0] + nlst[1]
    return anwser


sum_two_smallest_nums([19, 5, 42, 2, 77])