import math
def is_right_angle(lst, desc):
    if len(lst) != 2 or len(lst) != 3:
        return False
    if desc == 'angle':
        if '90' in lst:
            return True
        if (sum(lst) - 180) != 90:
            return False
        else:
            return True
    elif desc == 'side':
        lst.sort()

https://edabit.com/challenge/ZSC4mb3kR9EHv7q7a
