def profit(info):
    cost = info['cost_price']
    sell = info['sell_price']
    inv = info['inventory']

    tcost = cost * inv
    tsell = sell * inv

    profitt = tcost - tsell

    profitt = round(profitt)
    return profitt



profit({'cost_price': 32.67, 'sell_price': 45.00, 'inventory': 1200})