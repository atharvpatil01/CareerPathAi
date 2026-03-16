"""
Prediction route — accepts student data, returns ML-powered career predictions.
"""

from flask import Blueprint, jsonify, request

from models.career_data import AVAILABLE_INTERESTS, AVAILABLE_SKILLS, CAREER_PROFILES
from models.ml_model import predictor

predict_bp = Blueprint("predict", __name__)


@predict_bp.route("/api/predict", methods=["POST"])
def predict_career():
    """
    Predict top career domains based on student's scores, skills, and interests.

    Expected JSON body:
    {
        "scores": {
            "math": 85,
            "science": 78,
            "english": 70,
            "logical_reasoning": 90
        },
        "skills": ["Programming", "Problem Solving", "Mathematics"],
        "interests": ["Technology", "Science"]
    }
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    scores = data.get("scores", {})
    skills = data.get("skills", [])
    interests = data.get("interests", [])

    # Validate scores
    required_scores = ["math", "science", "english", "logical_reasoning"]
    for score_name in required_scores:
        if score_name not in scores:
            return jsonify({"error": f"Missing score: {score_name}"}), 400
        try:
            val = float(scores[score_name])
            if val < 0 or val > 100:
                return jsonify({"error": f"{score_name} must be between 0 and 100"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": f"Invalid value for {score_name}"}), 400

    # Validate skills
    invalid_skills = [s for s in skills if s not in AVAILABLE_SKILLS]
    if invalid_skills:
        return jsonify({"error": f"Invalid skills: {invalid_skills}"}), 400

    # Validate interests
    invalid_interests = [i for i in interests if i not in AVAILABLE_INTERESTS]
    if invalid_interests:
        return jsonify({"error": f"Invalid interests: {invalid_interests}"}), 400

    # Get predictions
    try:
        predictions = predictor.predict(scores, skills, interests)
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500

    # Enrich predictions with career details
    enriched = []
    for pred in predictions:
        career = pred["career"]
        profile = CAREER_PROFILES.get(career, {})
        enriched.append({
            "career": career,
            "confidence": pred["confidence"],
            "description": CAREER_PROFILES.get(career, {}).get("description", ""),
            "skills_required": profile.get("skills", []),
            "related_interests": profile.get("interests", []),
        })

    return jsonify({
        "predictions": enriched,
        "input_summary": {
            "scores": scores,
            "skills_selected": len(skills),
            "interests_selected": len(interests),
        },
    }), 200


@predict_bp.route("/api/options", methods=["GET"])
def get_options():
    """Return available skills and interests for the frontend form."""
    return jsonify({
        "skills": AVAILABLE_SKILLS,
        "interests": AVAILABLE_INTERESTS,
    }), 200
