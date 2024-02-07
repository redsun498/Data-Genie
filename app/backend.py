import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import io
from pywaffle import Waffle
import streamlit as st 

def load_data():
    data = pd.read_csv("../data/cleaned/all_drinks_cleaned.csv")
    return data

def vectorizer():
    vectorizer = TfidfVectorizer()
    return vectorizer

def ingredient_vectors(data):
    vectorizer = vectorizer()
    ingredient_vectors = vectorizer.fit_transform(data['ingredients_combined'])
    return ingredient_vectors


    # Define the TfidfVectorizer and use it to transform the data in a single function
def calculate_ingredient_similarities(data):
    vectorizer = TfidfVectorizer()
    ingredient_vectors = vectorizer.fit_transform(data['ingredients_combined'])
    ingredient_similarities = linear_kernel(ingredient_vectors, ingredient_vectors)
    return ingredient_similarities

# Use the calculated ingredient similarities for recommendations
def get_cocktail_recommendations(data, cocktail_name, n_recommendations=5):
    cocktail_index = data[data['strDrink'].str.lower() == cocktail_name].index
    if len(cocktail_index) > 0:
        cocktail_index = cocktail_index[0]
        ingredient_similarities = calculate_ingredient_similarities(data)
        ingredient_scores = list(enumerate(ingredient_similarities[cocktail_index]))
        ingredient_scores = sorted(ingredient_scores, key=lambda x: x[1], reverse=True)
        ingredient_recommendations = [data['strDrink'][i] for i, _ in ingredient_scores[1:n_recommendations+1]]
        return ingredient_recommendations
    else:
        return []

def wordcloud_graph(data):
    all_ingredients_string = ', '.join(data['ingredients_combined'])
    all_ingredients_string
    text = all_ingredients_string

    wordcloud = WordCloud(background_color="white",width = 1000,height=500, scale = 0.02).generate(text)

    fig,ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig,clear_figure = True)
    return wordcloud

def generate_wordcloud(data):
    all_ingredients_string = ', '.join(data['ingredients_combined'])

    # Create the word cloud
    wordcloud = WordCloud(background_color="white").generate(all_ingredients_string)

    # Save the word cloud to a bytes object
    wordcloud_image = io.BytesIO()
    wordcloud.to_image().save(wordcloud_image, format='PNG')
    wordcloud_image.seek(0)

    return wordcloud_image

def generate_waffle(data):
    waffle_fig = plt.figure(
        FigureClass=Waffle,
        rows=6,
        columns=13,
        values=data['strAlcoholic'].value_counts(),
        labels=['Alcoholic', 'Non alcoholic','Optional alcohol'], 
        legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
    )
    
    # Save the waffle chart to a bytes object
    waffle_image = io.BytesIO()
    waffle_fig.savefig(waffle_image, format='png')
    waffle_image.seek(0)

    return waffle_image
