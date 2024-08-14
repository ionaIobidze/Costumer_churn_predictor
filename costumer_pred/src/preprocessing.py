import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    data = pd.read_csv(file_path)
    # Handle missing values if any
    data.fillna(method='ffill', inplace=True)
    return data

def preprocess_data(data):
    # Encode categorical variables
    label_encoder = LabelEncoder()
    
    data['Gender'] = label_encoder.fit_transform(data['Gender'])
    data['Subscription Type'] = label_encoder.fit_transform(data['Subscription Type'])
    data['Contract Length'] = label_encoder.fit_transform(data['Contract Length'])
    
    # Selecting features
    features = ['Age', 'Gender', 'Tenure', 'Usage Frequency', 
                'Support Calls', 'Payment Delay', 'Subscription Type', 
                'Contract Length', 'Total Spend', 'Last Interaction']
    
    X = data[features]
    y = data['Churn']
    
    return X, y

# Example usage
data = load_data('/home/iona/ai_proeqtebi/Costumer_churn_predictor/costumer_pred/data/customer_churn_dataset-testing-master.csv')
X, y = preprocess_data(data)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the processed data
X_train.to_csv('../data/X_train.csv', index=False)
X_test.to_csv('../data/X_test.csv', index=False)
y_train.to_csv('../data/y_train.csv', index=False)
y_test.to_csv('../data/y_test.csv', index=False)
