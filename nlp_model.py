```python
# nlp_model.py

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from config import NLP_MODEL_PATH

class NLPModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = None
        try:
            with open(NLP_MODEL_PATH, 'rb') as file:
                self.model = pickle.load(file)
        except:
            print("No pre-trained model found. Please train the model.")

    def train(self, corpus):
        self.model = self.vectorizer.fit_transform(corpus)
        with open(NLP_MODEL_PATH, 'wb') as file:
            pickle.dump(self.model, file)

    def predict(self, query):
        if self.model is not None:
            query_vector = self.vectorizer.transform([query])
            similarity_scores = cosine_similarity(self.model, query_vector)
            return similarity_scores
        else:
            print("Model not trained. Please train the model.")
            return None
```
