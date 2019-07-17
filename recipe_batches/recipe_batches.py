#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  temp = []
  for key in recipe:
    if ingredients.get(key) and (ingredients[f"{key}"] / recipe[f"{key}"]) >= 1:
      temp.append(ingredients[f"{key}"] // recipe[f"{key}"])
    else:
      return 0

  return min(temp)

# recipe_batches({ 'milk': 100, 'butter': 50, 'flour': 5 }, {})

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


