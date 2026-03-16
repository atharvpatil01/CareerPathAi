"""
Authentication routes — register and login with JWT tokens.
"""

import datetime
import hashlib
import os

import jwt
from flask import Blueprint, jsonify, request

auth_bp = Blueprint("auth", __name__)

# In-memory user store (for demo purposes)
users_db = {}

# Secret key for JWT
JWT_SECRET = os.environ.get("JWT_SECRET", "career-guidance-secret-key-2024")


def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


@auth_bp.route("/api/register", methods=["POST"])
def register():
    """Register a new user."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")
    education_level = data.get("education_level", "")  # "10th" or "12th"

    if not all([name, email, password, education_level]):
        return jsonify({"error": "All fields are required: name, email, password, education_level"}), 400

    if education_level not in ["10th", "12th"]:
        return jsonify({"error": "education_level must be '10th' or '12th'"}), 400

    if email in users_db:
        return jsonify({"error": "User with this email already exists"}), 409

    # Create user
    users_db[email] = {
        "name": name,
        "email": email,
        "password": hash_password(password),
        "education_level": education_level,
        "created_at": datetime.datetime.utcnow().isoformat(),
    }

    # Generate JWT token
    token = jwt.encode(
        {
            "email": email,
            "name": name,
            "education_level": education_level,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
        },
        JWT_SECRET,
        algorithm="HS256",
    )

    return jsonify({
        "message": "Registration successful",
        "token": token,
        "user": {
            "name": name,
            "email": email,
            "education_level": education_level,
        },
    }), 201


@auth_bp.route("/api/login", methods=["POST"])
def login():
    """Login an existing user."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not all([email, password]):
        return jsonify({"error": "Email and password are required"}), 400

    user = users_db.get(email)
    if not user or user["password"] != hash_password(password):
        return jsonify({"error": "Invalid email or password"}), 401

    # Generate JWT token
    token = jwt.encode(
        {
            "email": email,
            "name": user["name"],
            "education_level": user["education_level"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
        },
        JWT_SECRET,
        algorithm="HS256",
    )

    return jsonify({
        "message": "Login successful",
        "token": token,
        "user": {
            "name": user["name"],
            "email": email,
            "education_level": user["education_level"],
        },
    }), 200
