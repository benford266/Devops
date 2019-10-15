#! openOrSenior.py


def openOrSenior(data):
  for app in data:
    if app[0] > 54:
        if app[1] > 7:
            return 'Senior'
        else :
            return 'Open'
    else :
        return 'Open'


openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]])