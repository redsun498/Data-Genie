import pandas as pd 
import numpy as np
import re
import nltk
from nltk.corpus import stopwords


def combine_ingredients(row):
    '''
    This function processes the individual ingredient columns in a row to create a combined string of cleaned and preprocessed ingredient names.

    ### Parameters
    - `row`: A pandas DataFrame row representing a single cocktail entry.

    ### Returns
    - A string representing the combined, cleaned, and preprocessed ingredients from the input row.
    ''' 
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

def get_cocktail_recommendations(df,ingredient_similarities,cocktail_index, n_recommendations=5):
    '''
    This function retrieves cocktail recommendations based on ingredient similarities using a precomputed similarity matrix.

    ### Parameters
    - `df`: The DataFrame containing cocktail information and data.
    
    - `ingredient_similarities`: A precomputed matrix of ingredient similarities between cocktails.

    - `cocktail_index`: The index of the target cocktail for which recommendations are to be generated.

    - `n_recommendations` (optional): The number of recommendations to retrieve (default value is 5).

    ### Returns
    - A list of recommended cocktails based on ingredient similarities.
    '''
    ingredient_scores = list(enumerate(ingredient_similarities[cocktail_index]))
    ingredient_scores = sorted(ingredient_scores, key=lambda x: x[1], reverse=True)
    ingredient_recommendations = [df['strDrink'][i] for i, _ in ingredient_scores[1:n_recommendations+1]]

    return ingredient_recommendations
