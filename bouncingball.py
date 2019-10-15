def bouncingBall(h, bounce, window):
    bouncecount = 0
    if 0 < bounce < 1:
        bounceheight = h * bounce
        while bounceheight > 1.5:
            bouncecount = bouncecount + 2
            print(bouncecount)
       