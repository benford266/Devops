#! divisors.py

def divisors(integer):
    intdiv = []
    if integer >1 :
        for i in range(2,integer):
            if (integer % i) == 0:
                intdiv.append(i)
            
    if intdiv == []:
        return '{} is prime'.format(integer)
    else:
        return intdiv