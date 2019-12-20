def society_name(friends):
    friends.sort()
    anwser =''
    for i in friends:
        anwser = anwser + i[0]
    return anwser

society_name(['Adam', 'Sarah', 'Malcolm'])