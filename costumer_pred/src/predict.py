import pandas as pd
import joblib

def load_test_data(file_path):
    data = pd.read_csv(file_path)
    return data

def make_predictions(model, data):
    predictions = model.predict(data)
    return predictions

def save_predictions(predictions, output_file):
    pd.DataFrame(predictions, columns=["Prediction"]).to_csv(output_file, index=False)

if __name__ == "__main__":
    # Load the model
    model = joblib.load('../api/model.pkl')
    
    # Load the test data (excluding the target column if it's there)
    test_data = load_test_data('../data/X_test.csv')
    
    # Make predictions
    predictions = make_predictions(model, test_data)
    
    # Save predictions to a file
    save_predictions(predictions, '../data/predictions.csv')
    
    print("Predictions saved to '../data/predictions.csv'")
