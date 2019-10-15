#! validatepin.py


def validate_pin(pin):
    
    if '.' in pin:
        return False
    elif '-' in pin:
        return False
    elif 'a' in pin:
        return False
    elif len(pin) == 4:
        try:
            if len(int(pin)) == 4:
                return True        
        except ValueError:
            return False
        return True
    elif len(pin) == 6:
        try:
            if len(int(pin)) == 6:
                return True        
        except ValueError:
            return False
    else:
        return False