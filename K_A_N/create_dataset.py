import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# # Sample size
# n = 1000
# Generating random data for each variable
data = {
    'Severity_of_Opioid_Use': np.random.choice(['Low', 'Moderate', 'High'], 1000, p=[0.2, 0.3, 0.5]),
    'Previous_Treatment_Attempts': np.random.choice(['Zero', 'One', 'Multiple'], 1000, p=[0.3, 0.4, 0.3]),
    'Co_occurring_Mental_Health_Conditions': np.random.choice(['Yes', 'No'], 1000, p=[0.5, 0.5]),
    'Physical_Health_Conditions': np.random.choice(['Yes', 'No'], 1000, p=[0.4, 0.6]),
    'Substance_Use_History': np.random.choice(['Opioids', 'Alcohol', 'Cocaine'], 1000, p=[0.6, 0.2, 0.2]),
    'Social_Support_System': np.random.choice(['Strong', 'Moderate', 'Weak'], 1000, p=[0.3, 0.5, 0.2]),
    'Compliance_Potential': np.random.choice(['High', 'Moderate', 'Low'], 1000, p=[0.3, 0.5, 0.2]),
    'Methadone_Recommended': np.random.choice(['Yes', 'No'], 1000, p=[0.5, 0.5]),
}

# Convert to DataFrame
df = pd.DataFrame(data)

# logic for methadone recommendation:
# Recommend methadone if Substance Use History is Opioids, with a High Severity of Use
df["Methadone_Recommended"] = np.where(
    (df["Substance_Use_History"] == "Opioids") & (df["Severity_of_Opioid_Use"] == "High"),
    "Yes",  # Recommend methadone if both conditions are met
    "No"    # Do not recommend methadone otherwise
)


# Save to CSV file
csv_file_path = "opioid_users_methadone_assessment.csv"
df.to_csv(csv_file_path, index=False)

csv_file_path
