#! disemvoewel.py

def disemvowel(string):
    string = string.replace('a','')
    string = string.replace('e','')
    string = string.replace('i','')
    string = string.replace('o','')
    string = string.replace('u','')
    string = string.replace('y','')
    string = string.replace('w','')
    return string

print(disemvowel("This website is for losers LOL!"))