import pandas as pd 
import numpy as np
import re
import nltk
from nltk.corpus import stopwords


def combine_ingredients(row):
    ingredient_columns = ['strIngredient1', 'strIngredient2', 'strIngredient3', 'strIngredient4', 'strIngredient5', 'strIngredient6',
                      'strIngredient7', 'strIngredient8', 'strIngredient9', 'strIngredient10', 'strIngredient11']
    ingredients = []
    for ingredient_col in ingredient_columns:
        if pd.notnull(row[ingredient_col]):
            ingredient = row[ingredient_col]
            # Clean the text data
            ingredient = re.sub(r'[^a-zA-Z\s]', '', ingredient)  # Remove special characters
            ingredient = ingredient.lower()  # Convert to lowercase
            
            # Remove stopwords
            stop_words = set(stopwords.words('english'))
            ingredient = ' '.join([word for word in ingredient.split() if word not in stop_words])
            
            ingredients.append(ingredient)
    return ', '.join(ingredients)
