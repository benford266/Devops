
# new list
list = ["Hello","World","What","A","Nice","Day"]
# function to print contense of list
def printlist():
    for item in range(0,6):
        print(list[item])

# print list 
printlist()

# edit list 
list[4] = input("What kind of day do you fancy ?")

# reprint list 
printlist()

# how many items are there in the list 
print("There are {} items in the list".format(len(list)))