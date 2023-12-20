
# models/classifier_model.py
# This file contains the ClassifierModel class.
from sklearn.linear_model import LogisticRegression
from utils.language_utils import extract_features

class ClassifierModel:
    def __init__(self):
        self.model = LogisticRegression()

    def update_model(self, new_data, feedback_data):
        features = [extract_features(example["user_input"]) for example in new_data]
        labels = [example["topic"] for example in new_data]
        self.model.fit(features, labels)
