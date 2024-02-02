import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import re
import nltk
from nltk.corpus import stopwords

def load_data():
    data = pd.read_csv(r"..\..\data_files\cleaned\'all_drinks_cleaned.csv")
    return data

