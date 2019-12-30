def pie_chart(data):
    counter = int()
    for i in data.values():
        counter = counter + i
    percents = 360 / counter
    for i in data:
        a = percents * data[i]
        if a.is_integer():
            data[i] = round(a)
        else:
            data[i] = round(a, 1)
    return data


pie_chart({ "a": 1, "b": 2 })