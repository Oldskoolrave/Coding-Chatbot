
# utils/language_utils.py
# This file contains utility functions related to language processing.
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_user_input(user_input):
    tokens = nltk.word_tokenize(user_input)
    lemmatized_tokens = [nltk.WordNetLemmatizer().lemmatize(token) for token in tokens]
    return lemmatized_tokens

def extract_features(user_input):
    features = TfidfVectorizer().fit_transform([user_input])
    return features.toarray()[0]
