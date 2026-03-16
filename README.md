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
