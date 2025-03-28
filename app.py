from flask import Flask, request, render_template
import os
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and vectorizer
model_dir = os.path.join(os.path.dirname(__file__), 'models')
model_path = os.path.join(model_dir, 'ranking_model.pkl')
vectorizer_path = os.path.join(model_dir, 'nlp_vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form data
        skills = request.form['skills']
        experience = float(request.form['experience'])
        education_10 = float(request.form['education_10'])
        education_12 = float(request.form['education_12'])
        cgpa = float(request.form['cgpa'])

        # Vectorize the skills input
        skills_vectorized = vectorizer.transform([skills])
        skills_df = pd.DataFrame(skills_vectorized.toarray(), columns=vectorizer.get_feature_names_out())

        # Create a DataFrame for the input features
        input_features = pd.concat([skills_df, pd.DataFrame([[experience, education_10, education_12, cgpa]],
                                                             columns=['experience', 'education_10', 'education_12', 'cgpa'])], axis=1)

        # Ensure all features match the model's expectations
        missing_cols = set(model.feature_names_in_) - set(input_features.columns)
        for col in missing_cols:
            input_features[col] = 0

        # Reorder columns to match the model's training data
        input_features = input_features[model.feature_names_in_]

        # Make prediction
        prediction = model.predict(input_features)
        job_relevance_score = prediction[0]

        return render_template('result.html', score=job_relevance_score)

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
