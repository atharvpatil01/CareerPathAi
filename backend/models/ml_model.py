"""
ML Model module — Random Forest + XGBoost ensemble for career prediction.
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

from models.career_data import (
    AVAILABLE_INTERESTS,
    AVAILABLE_SKILLS,
    CAREER_DOMAINS,
    generate_training_data,
    get_feature_names,
)


class CareerPredictor:
    """Ensemble career predictor using Random Forest + XGBoost."""

    def __init__(self):
        self.rf_model = None
        self.xgb_model = None
        self.label_encoder = LabelEncoder()
        self.is_trained = False
        self.feature_names = get_feature_names()

    def train(self):
        """Train both models on synthetic data."""
        print("[ML] Generating training data...")
        X, y = generate_training_data(n_samples=2400)

        # Encode labels
        y_encoded = self.label_encoder.fit_transform(y)

        # Train Random Forest
        print("[ML] Training Random Forest classifier...")
        self.rf_model = RandomForestClassifier(
            n_estimators=150,
            max_depth=15,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1,
        )
        self.rf_model.fit(X, y_encoded)

        # Train XGBoost
        print("[ML] Training XGBoost classifier...")
        self.xgb_model = XGBClassifier(
            n_estimators=150,
            max_depth=8,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            use_label_encoder=False,
            eval_metric="mlogloss",
        )
        self.xgb_model.fit(X, y_encoded)

        self.is_trained = True
        print("[ML] Models trained successfully!")

        # Print training accuracy
        rf_acc = self.rf_model.score(X, y_encoded)
        xgb_acc = self.xgb_model.score(X, y_encoded)
        print(f"[ML] Random Forest accuracy: {rf_acc:.4f}")
        print(f"[ML] XGBoost accuracy: {xgb_acc:.4f}")

    def prepare_features(self, scores, skills, interests):
        """
        Convert user input into feature vector.

        Args:
            scores: dict with keys math, science, english, logical_reasoning (0-100)
            skills: list of selected skill strings
            interests: list of selected interest strings

        Returns:
            numpy array of shape (1, n_features)
        """
        # Normalize scores to 0-100
        math = float(scores.get("math", 50))
        science = float(scores.get("science", 50))
        english = float(scores.get("english", 50))
        logical = float(scores.get("logical_reasoning", 50))

        # One-hot encode skills
        skill_vector = [1 if s in skills else 0 for s in AVAILABLE_SKILLS]

        # One-hot encode interests
        interest_vector = [1 if i in interests else 0 for i in AVAILABLE_INTERESTS]

        feature = [math, science, english, logical] + skill_vector + interest_vector
        return np.array([feature])

    def predict(self, scores, skills, interests):
        """
        Predict career domains using ensemble of RF + XGBoost.

        Returns:
            list of top 3 predictions, each with career name and confidence score
        """
        if not self.is_trained:
            raise RuntimeError("Models not trained. Call train() first.")

        X = self.prepare_features(scores, skills, interests)

        # Get probability predictions from both models
        rf_probs = self.rf_model.predict_proba(X)[0]
        xgb_probs = self.xgb_model.predict_proba(X)[0]

        # Ensemble: weighted average (0.45 RF + 0.55 XGBoost)
        ensemble_probs = 0.45 * rf_probs + 0.55 * xgb_probs

        # Get top 3 predictions
        top_indices = np.argsort(ensemble_probs)[::-1][:3]

        results = []
        for idx in top_indices:
            career = self.label_encoder.inverse_transform([idx])[0]
            confidence = float(ensemble_probs[idx])
            results.append({
                "career": career,
                "confidence": round(confidence * 100, 1),
            })

        return results


# Global model instance
predictor = CareerPredictor()
