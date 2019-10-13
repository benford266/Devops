def valid_parentheses(string):
    opencount = string.count('(')
    closecount = string.count(')')
    counter = 0
    if opencount != closecount:
        return False
    else:
        for i in string:
            if i == '(':
                counter = counter +1
                if counter < 0:
                    return False
            elif i == ')':
                counter = counter -1 
                if counter < 0:
                    return False

    return True 

