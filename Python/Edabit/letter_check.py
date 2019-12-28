def letter_check(lst):
    s1 = lst[0].lower()
    s2 = lst[1].lower()
    for i in s2:
        count = s1.count(i)
        if count < 1:
            return False

    return True




letter_check(["ben", "ben"])