"""
Roadmap route — returns personalized career roadmap based on chosen career.
"""

from flask import Blueprint, jsonify, request

from models.career_data import CAREER_ROADMAPS

roadmap_bp = Blueprint("roadmap", __name__)


@roadmap_bp.route("/api/roadmap/<career_key>", methods=["GET"])
def get_roadmap(career_key):
    """
    Get personalized roadmap for a specific career.

    URL params:
        career_key: career name with underscores (e.g., 'software_engineering')

    Query params:
        education_level: '10th' or '12th' (default: '12th')
    """
    education_level = request.args.get("education_level", "12th")

    if education_level not in ["10th", "12th"]:
        return jsonify({"error": "education_level must be '10th' or '12th'"}), 400

    # Convert URL key to career name
    # e.g., "software_engineering" -> "Software Engineering"
    career_name = career_key.replace("_", " ").title()

    # Handle special cases in naming
    name_mapping = {
        "Business And Finance": "Business & Finance",
        "Business & Finance": "Business & Finance",
        "Design And Ux": "Design & UX",
        "Design & Ux": "Design & UX",
        "Teaching And Education": "Teaching & Education",
        "Teaching & Education": "Teaching & Education",
        "Journalism And Media": "Journalism & Media",
        "Journalism & Media": "Journalism & Media",
        "Psychology And Counseling": "Psychology & Counseling",
        "Psychology & Counseling": "Psychology & Counseling",
    }

    career_name = name_mapping.get(career_name, career_name)

    roadmap = CAREER_ROADMAPS.get(career_name)
    if not roadmap:
        available = list(CAREER_ROADMAPS.keys())
        return jsonify({
            "error": f"Roadmap not found for '{career_name}'",
            "available_careers": available,
        }), 404

    # Select roadmap based on education level
    phases_key = f"after_{education_level}"
    phases = roadmap.get(phases_key, roadmap.get("after_12th", []))

    return jsonify({
        "career": career_name,
        "education_level": education_level,
        "description": roadmap["description"],
        "phases": phases,
        "skills_required": roadmap["skills_required"],
        "certifications": roadmap["certifications"],
        "top_courses": roadmap["top_courses"],
        "avg_salary": roadmap["avg_salary"],
    }), 200


@roadmap_bp.route("/api/careers", methods=["GET"])
def list_careers():
    """List all available careers with brief descriptions."""
    careers = []
    for name, data in CAREER_ROADMAPS.items():
        careers.append({
            "name": name,
            "key": name.lower().replace(" & ", "_and_").replace(" ", "_"),
            "description": data["description"],
            "avg_salary": data["avg_salary"],
        })
    return jsonify({"careers": careers}), 200
