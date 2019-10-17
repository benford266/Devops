def first_non_repeating_letter(string):
    letter = ''
    if string == '':
        return string
    else:
        for l in string:
            stringlow = string.lower()
            llow = l.lower()
            count = stringlow.count(llow)
            if count == 1:
                letter = l
                break
            
        
    if letter != '':
        return letter
    else:
        return ''