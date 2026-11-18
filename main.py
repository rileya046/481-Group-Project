from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import f1_score
import pandas
import numpy


# import dataset
### csv → DataFrame

# preprocessing
### CountVectorizer (lowercase / punctuation / stop words handled)

# split training vs testing
### train_test_split — scikit-learn 1.6.0 documentation - sklearn 

# model training
### model = MultinomialNB() 
### model.fit(x_train, y_train)

# split words to phishing vs safe
### map to 0/1 for ease of evaluating
### map, key word value amount