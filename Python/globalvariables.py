# change the global variable inside a function

x = "awesome"

def myfunc():
    global x
    x = "Fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)