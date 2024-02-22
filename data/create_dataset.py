import pandas as pd
import random
from faker import Faker

# Initialize Faker to a random seed for reproducibility
fake = Faker()
Faker.seed(0)
random.seed(0)

# Define the number of records
num_records = 100

# Define the column headers based on the proposed dataset structure
column_headers = [
    "Patient ID", "Age", "Sex", "Weight", "Height",
    "Type of Opioid Used", "Route of Administration", "Duration of Use", "Frequency of Use", "Quantity of Use",
    "Previous Methadone Use", "Duration of Previous Methadone Treatment", "Dosage of Previous Methadone Treatment",
    "Stimulant Use", "Alcohol Use", "Use of Other Opioids or Drugs",
    "Psychiatric Conditions", "Physical Health Conditions", "Known Genetic Markers",
    "Methadone Dosage Initiated", "Adjustments in Dosage", "Duration of Current Treatment", 
    "Treatment Outcome", "Side Effects Encountered", 
    "Patient's Treatment Goals", "Patient's Preferences"
]

# Function to generate random boolean with given probability
def random_boolean(probability_true=0.5):
    return random.random() < probability_true

# Generate synthetic data
data = []
for i in range(num_records):
    record = {
        "Patient ID": i+1,
        "Age": random.randint(18, 80),  # Assuming adult patients
        "Sex": random.choice(["Male", "Female", "Non-binary"]),
        "Weight": round(random.uniform(50.0, 120.0), 1),  # Weight in kilograms
        "Height": round(random.uniform(150.0, 200.0), 1),  # Height in centimeters
        "Type of Opioid Used": random.choice(["Heroin", "Fentanyl", "Oxycodone", "Hydrocodone", "Other"]),
        "Route of Administration": random.choice(["Injection", "Oral", "Snorting", "Smoking"]),
        "Duration of Use": random.choice(["<1 year", "1-3 years", "3-5 years", ">5 years"]),
        "Frequency of Use": random.choice(["Occasionally", "Monthly", "Weekly", "Daily"]),
        "Quantity of Use": random.choice(["Low", "Medium", "High"]),
        "Previous Methadone Use": random_boolean(),
        "Duration of Previous Methadone Treatment": random.choice(["None", "<1 year", "1-2 years", "2-5 years", ">5 years"]),
        "Dosage of Previous Methadone Treatment": random.choice(["None", "Low", "Medium", "High"]),
        "Stimulant Use": random.choice(["None", "Cocaine", "Methamphetamine", "Other"]),
        "Alcohol Use": random.choice(["None", "Occasional", "Moderate", "Heavy"]),
        "Use of Other Opioids or Drugs": random_boolean(),
        "Psychiatric Conditions": random.choice(["None", "Depression", "Anxiety", "Bipolar Disorder", "PTSD", "Other"]),
        "Physical Health Conditions": random.choice(["None", "Chronic Pain", "Hepatitis", "HIV", "Diabetes", "Hypertension", "Other"]),
        "Known Genetic Markers": random.choice(["None", "OPRM1", "COMT", "CYP2D6", "Other"]),
        "Methadone Dosage Initiated": round(random.uniform(20.0, 120.0), 1),  # Dosage in milligrams
        "Adjustments in Dosage": random.choice(["None", "Increased", "Decreased"]),
        "Duration of Current Treatment": random.choice(["<1 year", "1-2 years", "2-5 years", ">5 years"]),
        "Treatment Outcome": random.choice(["Ongoing", "Completed", "Relapsed", "Interrupted"]),
        "Side Effects Encountered": random.choice(["None", "Mild", "Moderate", "Severe"]),
        "Patient's Treatment Goals": random.choice(["Abstinence", "Harm Reduction", "Maintenance"]),
        "Patient's Preferences": random.choice(["Inpatient", "Outpatient", "Counseling", "Self-help Groups"])
    }
    data.append(record)

# Create a DataFrame with the synthetic data
df_synthetic = pd.DataFrame(data, columns=column_headers)

# Save the DataFrame to a CSV file
synthetic_data_v2_file_path = '~/Projects/opioid_treatment_agent/data/synthetic_patient_data_v2.csv'
df_synthetic.to_csv(synthetic_data_v2_file_path, index=False)

synthetic_data_v2_file_path
