#! narrnumber.py 

def narcissistic( value ):
    numbers = []
    for i in value:
        num = i^ len(value)
        print num 