from flask import Flask, request, jsonify, render_template
from joblib import load
import pandas as pd

app = Flask(__name__)

# Load the model and label encoders
model = load('model.pkl')
label_encoders = load('label_encoders.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = {key: value for key, value in request.form.items() if key != 'Methadone_Recommended'}
        new_data = {}
        for column in label_encoders.keys():
            # Handle case where column not submitted (e.g., unchecked boxes)
            new_data[column] = form_data.get(column, 'No')  # Defaulting to 'No' if not provided
            # Transform new data using label encoders
            if column in new_data:
                new_data[column] = label_encoders[column].transform([new_data[column]])[0]
        df_new = pd.DataFrame([new_data])
        prediction = model.predict(df_new)[0]
        result_label = 'Yes' if prediction == 1 else 'No'

        # Customize the result message
        if result_label == 'Yes':
            message = "Sounds like methadone might be an appropriate treatment option, I encourage you to talk to your doctor about it."
        else:
            message = "We don't think methadone will be the best treatment option for you, but if you think you need help, I encourage you to ask your doctor about other treatment options available to you."
        
        # Return your response, e.g., using jsonify for an AJAX call or rendering a template with the message
        return jsonify(result=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
