import json
import plotly
import pandas as pd
import numpy as np
import nltk
import string

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


app = Flask(__name__)

stopwords = nltk.corpus.stopwords.words('english')

def lower_words(text):
    text = text.lower()
    return text
    
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def clean_text(text):
    t_text_tokenized_list=[]
    t_text_cleaned_list=[]

    # Create lists containing split and cleaned words from sentences in text
    for i in text:
        t_text = nltk.word_tokenize(i)
        t_text_tokenized_list.append(t_text)
        t_text_cleaned = [word for word in t_text if word not in stopwords]
        t_text_cleaned_list.append(t_text_cleaned)

    return(t_text_tokenized_list, t_text_cleaned_list)

# Authors order: EAP HPL MWS
def predict(text):
    text = lower_words(text)
    text_without_punctuation = remove_punctuation(text)
    tokenized_text_list, cleaned_text_list = clean_text([text_without_punctuation])

    X_vectorized = count_vect.transform(cleaned_text_list[0])
    X_tfidf = tfidf_transformer.transform(X_vectorized[0])

    return model.predict_proba(X_tfidf)[0]

# load model
model = joblib.load("./models/model.pkl")
count_vect = joblib.load("./count_vectorizer.pkl")
tfidf_transformer = joblib.load("./tfidf_transformer.pkl")

authors = {
  0: 'Edgar Allan Poe',
  1: 'HP Lovecraft',
  2: 'Mary Wollstonecraft Shelley'
}


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    query = request.args.get('query', '')
    predictions = []
    graph = {}
    author_name = ''

    if query is not '':
        predictions = predict(query)
        author_name = authors[pd.Series(predictions).idxmax()]

        graph = {
            'data': [
                Bar(
                    x = [
                      'Edgar Allan Poe',
                      'HP Lovecraft',
                      'Mary Wollstonecraft Shelley'
                    ],
                    y = [x * 100 for x in predictions]
                )
            ],
            'layout': {
                'title': 'Predicted probabilities',
                'yaxis': {
                    'title': "Probability [%]"
                },
                'xaxis': {
                    'title': "Author name"
                }
            }
        }

    return render_template(
        'index.html',
        author_name=author_name,
        query=query,
        graph=json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()
