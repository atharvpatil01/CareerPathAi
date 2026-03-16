"""
Career Path Guidance System — Flask Backend
Entry point with CORS config and route registration.
"""

from flask import Flask
from flask_cors import CORS

from models.ml_model import predictor
from routes.auth import auth_bp
from routes.predict import predict_bp
from routes.roadmap import roadmap_bp


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Enable CORS for frontend
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Register route blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(roadmap_bp)

    # Health check
    @app.route("/api/health", methods=["GET"])
    def health():
        return {"status": "ok", "model_trained": predictor.is_trained}

    return app


if __name__ == "__main__":
    # Train ML models on startup
    predictor.train()

    # Create and run the app
    app = create_app()
    print("\n🚀 Career Guidance API running on http://localhost:5000")
    print("   Endpoints:")
    print("   POST /api/register   — Register a new user")
    print("   POST /api/login      — Login")
    print("   POST /api/predict    — Get career predictions")
    print("   GET  /api/options    — Get available skills & interests")
    print("   GET  /api/roadmap/<career> — Get career roadmap")
    print("   GET  /api/careers    — List all careers")
    print("   GET  /api/health     — Health check\n")
    app.run(debug=True, port=5000)
