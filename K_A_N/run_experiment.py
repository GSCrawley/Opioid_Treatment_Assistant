import subprocess
from model import train_and_evaluate, predict_eligibility, generate_single_patient

def run_create_dataset():
    subprocess.run(["python", "create_dataset.py"], check=True)

def main():
    prediction_label = 'No'
    while prediction_label != 'Yes':
        run_create_dataset()
        model, label_encoders = train_and_evaluate()
        new_patient = generate_single_patient()
        prediction_label = predict_eligibility(new_patient, model, label_encoders)
        print(prediction_label)

if __name__ == "__main__":
    main()
