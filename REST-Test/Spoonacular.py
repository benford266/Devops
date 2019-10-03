#! spoonacular.py
# Script to get 5 random recipies 

import spoonacular as sp
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


api = sp.API("7e44755f4fa74d75ab82245e8dda7522")

def getrecipe():

    response = api.get_random_recipes('1')

    data = response.json()['recipes']
    # Recipe name
    title = []
    for d in data:
        titlename = d['title']
        title.append(titlename)
    
    # Ingredients

    ingredients = []
    for ingred in data:
        ingedient = ingred['extendedIngredients']
        for single in ingedient:
            a = json.loads(single)
            orginaltext = a['orginalString']
            ingredients.append(orginaltext)

    print(title)
    print(ingredients)

getrecipe()