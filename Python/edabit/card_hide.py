def card_hide(card):
    length = len(card)
    last4 = card[-4:]
    start = (length-4) * '*'
    return start + last4


card_hide('11202039392839')