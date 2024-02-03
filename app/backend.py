import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import re
import nltk
from nltk.corpus import stopwords

def load_data():
    #data = pd.read_csv("r..\..\data_files\cleaned\'all_drinks_cleaned.csv")
    data = pd.read_csv("C:/Users/Estudiante/Documents/GitHub/Iron Hack/Final-Project-Brief-End-to-End-Data-Analytics-Project/data/cleaned/all_drinks_cleaned.csv")    
    return data

def vectorizer():
    vectorizer = TfidfVectorizer()
    return vectorizer

def ingredient_vectors(data):
    vectorizer_obj = vectorizer()
    ingredient_vectors = vectorizer_obj.fit_transform(data['ingredients_combined'])
    return ingredient_vectors

def training(data):
    vectorizer_obj = vectorizer()
    ingredient_vectors_obj = ingredient_vectors(data)
    ingredient_similarities = linear_kernel(ingredient_vectors_obj, ingredient_vectors_obj)
    return ingredient_similarities

def get_cocktail_recommendations(data, cocktail_name, n_recommendations=5):
    cocktail_index = data[data['strDrink'].str.lower() == cocktail_name].index
    if len(cocktail_index) > 0:
        cocktail_index = cocktail_index[0]
        ingredient_similarities = training(data)
        ingredient_scores = list(enumerate(ingredient_similarities[cocktail_index]))
        ingredient_scores = sorted(ingredient_scores, key=lambda x: x[1], reverse=True)
        ingredient_recommendations = [data['strDrink'][i] for i, _ in ingredient_scores[1:n_recommendations+1]]
        return ingredient_recommendations
    else:
        return []