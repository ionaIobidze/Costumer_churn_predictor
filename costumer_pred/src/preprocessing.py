import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    data = pd.read_csv(file_path)
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    return data

def preprocess_data(data):
    # Feature engineering
    data['session_length'] = data['last_login'] - data['first_login']
    # Convert categorical data to numeric
    data = pd.get_dummies(data)
    return data

# Example usage
data = load_data('data/customers.csv')
processed_data = preprocess_data(data)
train, test = train_test_split(processed_data, test_size=0.2)
