import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import cross_val_score
from joblib import dump

def train_and_evaluate():
    # Load the dataset
    df = pd.read_csv('/Users/gideoncrawley/Projects/Opioid_Treatment_Agent/K_A_N/opioid_users_methadone_assessment.csv')  # Adjust the path as necessary

    # Preprocess the dataset
    label_encoders = {}
    for column in df.columns[:-1]:  # Exclude the target
        if df[column].dtype == object:
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
            label_encoders[column] = le

    # Split the dataset
    X = df.drop('Methadone_Recommended', axis=1)
    y = df['Methadone_Recommended']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train the model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Confusion Matrix:", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:", classification_report(y_test, y_pred))

    # Save the model and label encoders
    # dump(model, 'model.pkl')
    # dump(label_encoders, 'label_encoders.pkl')

    return model, label_encoders

def predict_eligibility(patients_data, model, label_encoders):
    predictions = []
    for new_data in patients_data:
        for column, le in label_encoders.items():
            if column in new_data:
                new_data[column] = le.transform([new_data[column]])[0]
        df_new = pd.DataFrame([new_data])
        prediction = model.predict(df_new)[0]
        prediction_label = 'No' if prediction == 1 else 'Yes'
    
        predictions.append(prediction_label)
    return predictions

def generate_single_patient_1():
    return {
        'Severity_of_Opioid_Use': np.random.choice(['Low', 'Moderate', 'High'], p=[0.3, 0.3, 0.4]),
        'Previous_Treatment_Attempts': np.random.choice(['Zero', 'One', 'Multiple'], p=[0.3, 0.4, 0.3]),
        'Co_occurring_Mental_Health_Conditions': np.random.choice(['Yes', 'No'], p=[0.5, 0.5]),
        'Physical_Health_Conditions': np.random.choice(['Yes', 'No'], p=[0.4, 0.6]),
        'Substance_Use_History': np.random.choice(['Opioids', 'Alcohol', 'Cocaine'], p=[0.4, 0.3, 0.3]),
        'Social_Support_System': np.random.choice(['Strong', 'Moderate', 'Weak'], p=[0.3, 0.5, 0.2]),
        'Compliance_Potential': np.random.choice(['High', 'Moderate', 'Low'], p=[0.3, 0.5, 0.2]),
}

def generate_single_patient_2():
    return {
        'Severity_of_Opioid_Use': np.random.choice(['Low', 'Moderate', 'High'], p=[0.1, 0.2, 0.7]),
        'Previous_Treatment_Attempts': np.random.choice(['Zero', 'One', 'Multiple'], p=[0.3, 0.4, 0.3]),
        'Co_occurring_Mental_Health_Conditions': np.random.choice(['Yes', 'No'], p=[0.5, 0.5]),
        'Physical_Health_Conditions': np.random.choice(['Yes', 'No'], p=[0.4, 0.6]),
        'Substance_Use_History': np.random.choice(['Opioids', 'Alcohol', 'Cocaine'], p=[0.8, 0.1, 0.1]),
        'Social_Support_System': np.random.choice(['Strong', 'Moderate', 'Weak'], p=[0.3, 0.5, 0.2]),
        'Compliance_Potential': np.random.choice(['High', 'Moderate', 'Low'], p=[0.3, 0.5, 0.2]),
}

if __name__ == "__main__":
    model, label_encoders = train_and_evaluate()
    # Generating a list of new patients
    new_patient_list = [generate_single_patient_1(), generate_single_patient_2()]
    # Predicting eligibility for each patient in the list
    predictions = predict_eligibility(new_patient_list, model, label_encoders)
    for prediction in predictions:
        print(prediction)