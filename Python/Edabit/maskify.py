def maskify(txt):
    if len(txt) > 4:
        length = len(txt)
        x = length - 4
        star = '#' * x
        last = txt[-4:]
        anwser = star + last
        return anwser

    else:
        return txt

maskify('111111131')

