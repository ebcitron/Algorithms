#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # make sure you have all ingredients by name that recipe calls for. 
  #if recipe is in ingredients,
  #   --  ingredients = ingredients - recipe
  #        maxBatches +=1
  #      return maxbatches
  # else maxbatches = 0
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))