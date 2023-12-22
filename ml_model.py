```python
# ml_model.py

import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from config import ML_MODEL_PATH

class MLModel:
    def __init__(self):
        self.model = None
        try:
            with open(ML_MODEL_PATH, 'rb') as file:
                self.model = pickle.load(file)
        except:
            print("No pre-trained model found. Please train the model.")

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier(n_estimators=100)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(f"Model trained with accuracy: {accuracy_score(y_test, y_pred)}")

        with open(ML_MODEL_PATH, 'wb') as file:
            pickle.dump(self.model, file)

    def predict(self, X):
        if self.model is not None:
            return self.model.predict(X)
        else:
            print("Model not trained. Please train the model.")
            return None
```
