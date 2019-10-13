#! python3
# dinnerpicker.py
#
# Script to pick what to eat for each day of week. 
# Imports
import random

foods = ['pizza','sausge surprise','pasta bake','hotdogs','pad thai','curry','meatballs','stir fry']

def pickfood():
    rand = random.randint(0,7)
    print(foods[rand])

pickfood()
