class Animal:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age
    
steve = Animal('Steve',"Dog",7)

print('{} is a {}, he is {} years old'.format(steve.name, steve.type, steve.age))