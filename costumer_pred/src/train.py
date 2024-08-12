from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

def train_model(train_data):
    X = train_data.drop('churn', axis=1)
    y = train_data['churn']
    model = LogisticRegression()
    model.fit(X, y)
    joblib.dump(model, 'models/churn_model.pkl')
    return model

# Example usage
model = train_model(train)
