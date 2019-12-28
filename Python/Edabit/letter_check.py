def letter_check(lst):
    for i in lst[0]:
        count = lst[1].count(i)
        if count < 1:
            return False
            break
        else:
            continue



letter_check(["trances", "nectar"])