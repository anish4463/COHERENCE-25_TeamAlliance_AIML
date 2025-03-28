import pickle
import numpy as np

def rank_candidates(resume_features):
    """Rank resumes based on ML model predictions."""
    model_path = "models/ranking_model.pkl"
    vectorizer_path = "models/nlp_vectorizer.pkl"
    
    # Load trained model
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)

    # Load NLP vectorizer
    with open(vectorizer_path, "rb") as vec_file:
        vectorizer = pickle.load(vec_file)

    # Convert resume text to feature vectors
    features = vectorizer.transform(resume_features)

    # Predict rankings (higher score is better)
    scores = model.predict_proba(features)[:, 1]  # Get probability of being a good candidate

    # Return sorted resumes based on scores
    ranked_indices = np.argsort(scores)[::-1]
    return ranked_indices, scores[ranked_indices]
