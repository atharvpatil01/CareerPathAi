# 🎯 CareerPath AI — Career Guidance System

An AI-powered career guidance system that provides **personalized career predictions and roadmaps** for students who just passed **10th or 12th standard**. Built with a Python Flask backend (ML-powered) and a modern React frontend.

---

## 📸 Screenshots

### Landing Page
Premium dark-themed landing page with animated hero section and feature highlights.

### Profile Assessment
Interactive profile page with score sliders, skill tags, and interest selection.

### AI Career Predictions
Dashboard showing top 3 career recommendations with confidence scores from the ML ensemble.

### Personalized Roadmap
Step-by-step career roadmap tailored to the student's education level (after 10th or 12th).

---

## 🏗️ System Architecture

```
┌─────────────────────────────┐
│     User Interface (React)  │
└─────────────┬───────────────┘
              ▼
┌─────────────────────────────┐
│   Input Processing Module   │
│  (Scores, Skills, Interest) │
└─────────────┬───────────────┘
              ▼
┌─────────────────────────────┐
│  Feature Engineering &      │
│  Preprocessing              │
└──────┬──────────────┬───────┘
       ▼              ▼
┌──────────────┐ ┌──────────────┐
│ Random Forest│ │   XGBoost    │
│  Classifier  │ │  Classifier  │
└──────┬───────┘ └──────┬───────┘
       └────────┬───────┘
                ▼
┌─────────────────────────────┐
│  Prediction & Recommendation│
│  (Weighted Ensemble)        │
└─────────────┬───────────────┘
              ▼
┌─────────────────────────────┐
│   Output — Career Results   │
│  Suggestions, Skills, etc.  │
└─────────────────────────────┘
```

---

## 🔄 Workflow

| Step | Process | Description |
|------|---------|-------------|
| 1 | **User Registration** | Student creates account with education level (10th/12th) |
| 2 | **Skill & Interest Analysis** | System collects academic scores, skills, and interests |
| 3 | **Career Domain Prediction** | ML model predicts suitable career domains |
| 4 | **Career Mapping** | System maps careers to required skills and courses |
| 5 | **Roadmap Generation** | Personalized career roadmap is created |
| 6 | **Dashboard Display** | Career options, certifications, and timeline displayed |

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | Backend language |
| **Flask** | REST API framework |
| **scikit-learn** | Random Forest classifier |
| **XGBoost** | XGBoost classifier |
| **PyJWT** | JWT authentication |
| **Flask-CORS** | Cross-origin support |
| **NumPy** | Numerical computing |

### Frontend
| Technology | Purpose |
|------------|---------|
| **React 19** | UI library |
| **Vite** | Build tool & dev server |
| **React Router** | Client-side routing |
| **Vanilla CSS** | Custom design system |
| **Google Fonts (Inter)** | Typography |

---

## 📁 Project Structure

```
CareerPathAi/
├── backend/
│   ├── app.py                  # Flask entry point
│   ├── requirements.txt        # Python dependencies
│   ├── models/
│   │   ├── career_data.py      # Career datasets, roadmaps, training data
│   │   └── ml_model.py         # RF + XGBoost ensemble predictor
│   └── routes/
│       ├── auth.py             # Register/Login (JWT)
│       ├── predict.py          # Career prediction endpoint
│       └── roadmap.py          # Roadmap generation endpoint
│
├── frontend/
│   ├── index.html              # Entry HTML
│   ├── package.json            # Node dependencies
│   ├── vite.config.js          # Vite configuration
│   └── src/
│       ├── main.jsx            # React entry point
│       ├── App.jsx             # Router & auth state
│       ├── api.js              # Backend API client
│       ├── index.css           # Design system (dark theme)
│       ├── components/
│       │   └── Navbar.jsx      # Navigation bar
│       └── pages/
│           ├── Landing.jsx     # Hero & features page
│           ├── Auth.jsx        # Login/Register page
│           ├── Profile.jsx     # Score/Skill/Interest input
│           ├── Dashboard.jsx   # Career prediction results
│           └── Roadmap.jsx     # Personalized career roadmap
│
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+** installed
- **Node.js 18+** and **npm** installed
- **Git** installed

### 1. Clone the Repository
```bash
git clone https://github.com/atharvpatil01/CareerPathAi.git
cd CareerPathAi
```

### 2. Setup Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```
The backend will:
- Generate synthetic training data (2400 samples)
- Train Random Forest + XGBoost models
- Start the API server on **http://localhost:5000**

### 3. Setup Frontend
```bash
cd frontend
npm install
npm run dev
```
The frontend will start on **http://localhost:5173**

### 4. Open the App
Navigate to **http://localhost:5173** in your browser and start exploring!

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/register` | Register new user (name, email, password, education_level) |
| `POST` | `/api/login` | Login with email & password |
| `POST` | `/api/predict` | Get career predictions (scores, skills, interests) |
| `GET` | `/api/options` | Get available skills & interests |
| `GET` | `/api/roadmap/<career>` | Get career roadmap (query: education_level) |
| `GET` | `/api/careers` | List all available careers |
| `GET` | `/api/health` | Health check |

### Example: Predict Career
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "scores": {"math": 85, "science": 78, "english": 70, "logical_reasoning": 90},
    "skills": ["Programming", "Problem Solving", "Analytical Thinking"],
    "interests": ["Technology", "Science", "Engineering"]
  }'
```

---

## 🤖 ML Model Details

### Ensemble Architecture
The system uses a **weighted ensemble** of two classifiers:
- **Random Forest** (150 estimators, max_depth=15) — Weight: 45%
- **XGBoost** (150 estimators, max_depth=8, lr=0.1) — Weight: 55%

### Training Data
- **2400 synthetic samples** generated from career profiles
- **34 features**: 4 academic scores + 15 skill indicators + 15 interest indicators
- **12 career domains** with distinct score/skill/interest patterns

### Career Domains
| Domain | Key Strengths |
|--------|--------------|
| 💻 Software Engineering | High math + logical reasoning + programming |
| 📊 Data Science | High math + analytical thinking + data analysis |
| 🏥 Medicine | High science + research + healthcare interest |
| ⚖️ Law | High english + communication + critical thinking |
| 📈 Business & Finance | High math + leadership + business interest |
| 🎨 Design & UX | Creativity + design skills + arts interest |
| 👩‍🏫 Teaching & Education | Communication + public speaking + education interest |
| ⚙️ Mechanical Engineering | High math + science + engineering interest |
| 🏗️ Civil Engineering | High math + science + environment interest |
| 📰 Journalism & Media | High english + writing + media interest |
| 🧠 Psychology & Counseling | Communication + empathy + social work interest |
| 🧬 Biotechnology | High science + research + healthcare interest |

---

## 🗺️ Personalized Roadmaps

Each career provides a **tailored roadmap** based on whether the student passed **10th or 12th standard**, including:

- 📚 **Step-by-step educational path** (stream selection, degree, specialization)
- 🛠️ **Skills to develop** (technical + soft skills)
- 📜 **Certifications** to pursue
- 🎓 **Top courses & colleges** recommended
- 💰 **Expected salary range** in India

---

## ✨ Features

- 🔐 **JWT Authentication** — Secure register/login with token-based auth
- 📊 **Interactive Score Input** — Slider-based academic score entry
- 🏷️ **Tag Selection** — Click-to-select skills and interests
- 🤖 **AI Predictions** — Top 3 career matches with confidence percentages
- 🗺️ **Visual Roadmap** — Animated timeline with career milestones
- 🌙 **Premium Dark Theme** — Glassmorphism, gradients, micro-animations
- 📱 **Responsive Design** — Works on desktop, tablet, and mobile
- ⚡ **Fast & Modern** — Vite-powered frontend with hot reload

---

## 🧪 Testing

### Backend API Test
```bash
# Health check
curl http://localhost:5000/api/health

# Register
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@test.com","password":"1234","education_level":"12th"}'

# Get options
curl http://localhost:5000/api/options
```

### Full Flow Test
1. Open http://localhost:5173
2. Register with your details (select 10th or 12th)
3. Fill in academic scores, select skills & interests
4. Click "Get Career Predictions"
5. View your top 3 career matches
6. Click "View Career Roadmap" for detailed guidance

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Atharv Patil**
- GitHub: [@atharvpatil01](https://github.com/atharvpatil01)

---

<p align="center">
  Made with ❤️ for students navigating their career paths
</p>

---

## 📋 Project Methodology

### 1. Introduction & Problem Statement

**Problem:** Students who have just passed their 10th or 12th standard face a critical decision about their career path but often lack personalised, data-driven guidance.

**Solution:** An AI-powered web application that takes a student's academic scores, skills, and interests as input and uses Machine Learning to predict the top 3 suitable career domains — along with a personalised step-by-step roadmap.

---

### 2. Development Methodology

The project follows a **modified Agile/Iterative** approach split into clearly defined phases:

#### Phase 1 — Requirement Analysis & Data Modelling
| Activity | Output |
|---|---|
| Identify target audience (10th/12th pass students) | User persona document |
| Map 12 career domains with score ranges, skills, and interests | `career_data.py` — `CAREER_PROFILES` dictionary |
| Define input features (4 scores + 15 skills + 15 interests = 34 features) | Feature schema |
| Design career roadmaps for each domain (after 10th & after 12th) | `CAREER_ROADMAPS` dictionary |

#### Phase 2 — Machine Learning Model Development
| Activity | Output |
|---|---|
| Generate synthetic training data (2,400 samples) using CAREER_PROFILES | `generate_training_data()` in `career_data.py` |
| Train Random Forest (150 estimators, max_depth=15) | Trained RF model in `ml_model.py` |
| Train XGBoost (150 estimators, max_depth=8, lr=0.1) | Trained XGB model in `ml_model.py` |
| Build weighted ensemble (RF 45% + XGBoost 55%) | `CareerPredictor.predict()` method |
| Validate training accuracy | Accuracy printed on startup |

#### Phase 3 — Backend API Development (Flask)
| Activity | Output |
|---|---|
| Create Flask app with CORS support | `app.py` — `create_app()` |
| Implement JWT-based auth (register/login) | `routes/auth.py` |
| Build prediction endpoint | `routes/predict.py` — `POST /api/predict` |
| Build roadmap generation endpoint | `routes/roadmap.py` — `GET /api/roadmap/<career>` |
| Add utility endpoints (health, options, careers) | Various routes |

#### Phase 4 — Frontend Development (React + Vite)
| Activity | Output |
|---|---|
| Design dark-themed design system (CSS variables, glassmorphism) | `index.css` — 22 KB design system |
| Build responsive Navbar with auth awareness | `Navbar.jsx` |
| Build Landing page with hero section & features | `Landing.jsx` |
| Build Auth page (login/register toggle) | `Auth.jsx` |
| Build Profile page (sliders for scores, tag-select for skills/interests) | `Profile.jsx` |
| Build Dashboard (top 3 predictions with confidence bars) | `Dashboard.jsx` |
| Build Roadmap page (animated timeline) | `Roadmap.jsx` |
| Wire up API client | `api.js` |

#### Phase 5 — Integration & Testing
| Activity | Output |
|---|---|
| Connect frontend → backend via REST API | `api.js` baseURL → `localhost:5000` |
| End-to-end flow testing (register → login → profile → predict → roadmap) | Manual test script in README |
| API endpoint testing with `curl` | Test commands documented |

---

### 3. Technology Stack Justification

| Layer | Choice | Rationale |
|---|---|---|
| **ML — Random Forest** | scikit-learn | Robust, interpretable, handles tabular data well |
| **ML — XGBoost** | xgboost | Best-in-class gradient boosting for structured data |
| **Ensemble Strategy** | Weighted average (45/55) | Combines RF's stability with XGBoost's precision |
| **Backend** | Flask | Lightweight, Pythonic, easy ML integration |
| **Auth** | PyJWT | Stateless token-based auth, no DB dependency |
| **Frontend** | React 19 + Vite | Fast dev server, modern JSX, component reusability |
| **Styling** | Vanilla CSS | Full control, no framework overhead, premium dark theme |
| **Routing** | React Router | SPA navigation, auth-protected routes |

---

### 4. Data Flow — Complete User Journey

```
Student                    React Frontend              Flask Backend               ML Ensemble
  │                              │                           │                          │
  ├── Register ────────────────► POST /api/register ────────►│                          │
  │◄──────────── JWT Token ◄──── JWT Token ◄────────────────┤                          │
  │                              │                           │                          │
  ├── Input Scores/Skills ─────► POST /api/predict ─────────► prepare_features()        │
  │                              │                           ├── 34-dim vector ────────►│
  │                              │                           │   RF predict_proba       │
  │                              │                           │   XGB predict_proba      │
  │                              │                           │◄── Ensemble (0.45*RF     │
  │                              │                           │     + 0.55*XGB)  ◄───────┤
  │◄──── Dashboard (3 cards) ◄── Top 3 careers + confidence◄┤                          │
  │                              │                           │                          │
  ├── Click "View Roadmap" ────► GET /api/roadmap/<career> ─►│                          │
  │◄──── Animated Timeline  ◄─── Roadmap phases, skills ◄───┤                          │
```

---

### 5. ML Model Methodology

#### 5.1 Synthetic Data Generation

Since real student-career outcome data is not available, the system generates **2,400 synthetic training samples** (200 per career domain) using the curated `CAREER_PROFILES`:

- **Score features** (4): Gaussian distribution centred on each career's ideal range (e.g., Software Engineering → math 75–100, logical 80–100)
- **Skill features** (15): Binary flags, 75% probability if the skill is associated with the career, 15% otherwise
- **Interest features** (15): Binary flags, 75% probability if associated, 12% otherwise

#### 5.2 Model Training

| Model | Hyperparameters |
|---|---|
| **Random Forest** | `n_estimators=150`, `max_depth=15`, `min_samples_split=5`, `min_samples_leaf=2` |
| **XGBoost** | `n_estimators=150`, `max_depth=8`, `learning_rate=0.1`, `subsample=0.8`, `colsample_bytree=0.8` |

#### 5.3 Ensemble Prediction
```
ensemble_probabilities = 0.45 × RF_probabilities + 0.55 × XGB_probabilities
```
Top 3 indices are extracted via `argsort()`, inverse-label-transformed to career names, and returned with confidence percentages.

---

### 6. Frontend Page Architecture

| Page | Route | Purpose |
|---|---|---|
| **Landing** | `/` | Hero section, feature highlights, CTA |
| **Auth** | `/auth` | Login/Register form with toggle |
| **Profile** | `/profile` | Score sliders, skill/interest tag selection → submit |
| **Dashboard** | `/dashboard` | Top 3 career prediction cards with confidence bars |
| **Roadmap** | `/roadmap/:career` | Step-by-step animated career roadmap timeline |

---

### 7. Testing Strategy

| Test Type | Method | Scope |
|---|---|---|
| **API Smoke Test** | `curl http://localhost:5000/api/health` | Backend is running, model trained |
| **Registration Test** | `curl POST /api/register` with JSON body | User creation + JWT return |
| **Prediction Test** | `curl POST /api/predict` with sample data | ML pipeline end-to-end |
| **Full Flow (Manual)** | Browser walk-through: register → profile → predict → roadmap | Complete user journey |

---

### 8. Future Enhancements

| Enhancement | Description |
|---|---|
| **Real Dataset** | Replace synthetic data with real student-career outcome data |
| **Database** | Add SQLite / PostgreSQL for persistent user storage |
| **Model Persistence** | Save/load trained models with `joblib` instead of retraining on every startup |
| **More Careers** | Expand from 12 to 20+ career domains |
| **Feedback Loop** | Let users rate predictions to improve model accuracy over time |
| **Deployment** | Deploy backend on Render/Railway, frontend on Vercel/Netlify |
