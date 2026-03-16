"""
Career data module — curated synthetic dataset for training ML models.
Maps academic scores + skills + interests → career domains.
Tailored for students who just passed 10th or 12th standard.
"""

import numpy as np
import random

# All available career domains
CAREER_DOMAINS = [
    "Software Engineering",
    "Data Science",
    "Medicine",
    "Law",
    "Business & Finance",
    "Design & UX",
    "Teaching & Education",
    "Mechanical Engineering",
    "Civil Engineering",
    "Journalism & Media",
    "Psychology & Counseling",
    "Biotechnology",
]

# Available skills a student can select
AVAILABLE_SKILLS = [
    "Programming",
    "Mathematics",
    "Communication",
    "Problem Solving",
    "Creativity",
    "Leadership",
    "Analytical Thinking",
    "Writing",
    "Research",
    "Teamwork",
    "Public Speaking",
    "Critical Thinking",
    "Design",
    "Data Analysis",
    "Time Management",
]

# Available interests a student can select
AVAILABLE_INTERESTS = [
    "Technology",
    "Science",
    "Arts",
    "Business",
    "Healthcare",
    "Social Work",
    "Sports",
    "Music",
    "Literature",
    "Environment",
    "Politics",
    "Education",
    "Media",
    "Engineering",
    "Finance",
]

# Career profiles: defines ideal score ranges and associated skills/interests
CAREER_PROFILES = {
    "Software Engineering": {
        "scores": {"math": (75, 100), "science": (65, 100), "english": (50, 85), "logical_reasoning": (80, 100)},
        "skills": ["Programming", "Problem Solving", "Analytical Thinking", "Mathematics", "Critical Thinking"],
        "interests": ["Technology", "Engineering", "Science"],
    },
    "Data Science": {
        "scores": {"math": (80, 100), "science": (70, 100), "english": (50, 85), "logical_reasoning": (75, 100)},
        "skills": ["Mathematics", "Data Analysis", "Programming", "Analytical Thinking", "Research"],
        "interests": ["Technology", "Science", "Finance"],
    },
    "Medicine": {
        "scores": {"math": (60, 95), "science": (85, 100), "english": (55, 90), "logical_reasoning": (65, 95)},
        "skills": ["Research", "Critical Thinking", "Communication", "Teamwork", "Problem Solving"],
        "interests": ["Healthcare", "Science", "Social Work"],
    },
    "Law": {
        "scores": {"math": (40, 75), "science": (40, 75), "english": (80, 100), "logical_reasoning": (75, 100)},
        "skills": ["Communication", "Writing", "Critical Thinking", "Public Speaking", "Analytical Thinking"],
        "interests": ["Politics", "Social Work", "Literature"],
    },
    "Business & Finance": {
        "scores": {"math": (70, 100), "science": (45, 80), "english": (60, 90), "logical_reasoning": (65, 95)},
        "skills": ["Leadership", "Communication", "Analytical Thinking", "Mathematics", "Time Management"],
        "interests": ["Business", "Finance", "Technology"],
    },
    "Design & UX": {
        "scores": {"math": (45, 80), "science": (40, 75), "english": (55, 85), "logical_reasoning": (55, 90)},
        "skills": ["Creativity", "Design", "Problem Solving", "Communication", "Critical Thinking"],
        "interests": ["Arts", "Technology", "Media"],
    },
    "Teaching & Education": {
        "scores": {"math": (55, 90), "science": (55, 90), "english": (65, 95), "logical_reasoning": (55, 90)},
        "skills": ["Communication", "Public Speaking", "Leadership", "Teamwork", "Time Management"],
        "interests": ["Education", "Social Work", "Literature"],
    },
    "Mechanical Engineering": {
        "scores": {"math": (75, 100), "science": (75, 100), "english": (45, 80), "logical_reasoning": (70, 100)},
        "skills": ["Mathematics", "Problem Solving", "Analytical Thinking", "Research", "Critical Thinking"],
        "interests": ["Engineering", "Technology", "Science"],
    },
    "Civil Engineering": {
        "scores": {"math": (70, 100), "science": (70, 95), "english": (45, 80), "logical_reasoning": (65, 95)},
        "skills": ["Mathematics", "Problem Solving", "Teamwork", "Leadership", "Analytical Thinking"],
        "interests": ["Engineering", "Environment", "Technology"],
    },
    "Journalism & Media": {
        "scores": {"math": (35, 70), "science": (35, 70), "english": (80, 100), "logical_reasoning": (55, 85)},
        "skills": ["Writing", "Communication", "Creativity", "Public Speaking", "Research"],
        "interests": ["Media", "Literature", "Politics"],
    },
    "Psychology & Counseling": {
        "scores": {"math": (45, 80), "science": (60, 90), "english": (65, 95), "logical_reasoning": (60, 90)},
        "skills": ["Communication", "Critical Thinking", "Research", "Writing", "Teamwork"],
        "interests": ["Social Work", "Healthcare", "Education"],
    },
    "Biotechnology": {
        "scores": {"math": (65, 95), "science": (80, 100), "english": (50, 85), "logical_reasoning": (65, 95)},
        "skills": ["Research", "Analytical Thinking", "Critical Thinking", "Data Analysis", "Mathematics"],
        "interests": ["Science", "Healthcare", "Environment"],
    },
}

# Detailed roadmap data for each career
CAREER_ROADMAPS = {
    "Software Engineering": {
        "description": "Build software applications, systems, and platforms that power the digital world.",
        "after_10th": [
            {"phase": "11th-12th (Science Stream)", "duration": "2 years", "details": "Take PCM (Physics, Chemistry, Mathematics) with Computer Science. Focus on building strong math and logic foundations."},
            {"phase": "B.Tech/B.E. in Computer Science", "duration": "4 years", "details": "Pursue a degree in Computer Science or IT from a reputed university. Learn data structures, algorithms, and software engineering."},
            {"phase": "Internships & Projects", "duration": "During college", "details": "Build real-world projects, contribute to open source, and complete 2-3 internships at tech companies."},
            {"phase": "Entry-Level Software Engineer", "duration": "1-2 years", "details": "Join a tech company as a junior developer. Focus on learning the tech stack and best practices."},
            {"phase": "Mid-Senior Level", "duration": "3-5 years", "details": "Specialize in areas like full-stack, cloud, AI/ML, or DevOps. Take on leadership responsibilities."},
        ],
        "after_12th": [
            {"phase": "B.Tech/B.E. in Computer Science", "duration": "4 years", "details": "Pursue a degree in Computer Science or IT. Focus on core CS fundamentals and practical projects."},
            {"phase": "Internships & Projects", "duration": "During college", "details": "Build portfolio, do internships, participate in hackathons and coding competitions."},
            {"phase": "Entry-Level Software Engineer", "duration": "1-2 years", "details": "Start career at a product or service company. Master your domain."},
            {"phase": "Mid-Senior Level", "duration": "3-5 years", "details": "Grow into specialized roles. Consider M.Tech or MS for research roles."},
        ],
        "skills_required": ["Python", "JavaScript", "Data Structures", "Algorithms", "Git", "SQL", "System Design"],
        "certifications": ["AWS Certified Developer", "Google Cloud Professional", "Meta Front-End Developer Certificate"],
        "top_courses": ["CS50 (Harvard)", "Full Stack Open (University of Helsinki)", "NPTEL Programming Courses"],
        "avg_salary": "₹6-25 LPA (India)",
    },
    "Data Science": {
        "description": "Analyze complex data to extract insights and build predictive models that drive business decisions.",
        "after_10th": [
            {"phase": "11th-12th (Science Stream)", "duration": "2 years", "details": "Take PCM with focus on Statistics and Mathematics. Start learning Python basics."},
            {"phase": "B.Tech/B.Sc in CS/Statistics/Math", "duration": "3-4 years", "details": "Pursue a degree in Computer Science, Statistics, or Mathematics. Take electives in ML and Data Science."},
            {"phase": "Specialization & Projects", "duration": "1-2 years", "details": "Complete online certifications in ML/AI. Build data science projects with real datasets."},
            {"phase": "Junior Data Scientist", "duration": "1-2 years", "details": "Join a data team. Work on data pipelines, analysis, and basic ML models."},
            {"phase": "Senior Data Scientist / ML Engineer", "duration": "3-5 years", "details": "Lead ML projects, design architectures, mentor juniors. Consider M.Tech/MS in AI."},
        ],
        "after_12th": [
            {"phase": "B.Tech/B.Sc in CS/Statistics", "duration": "3-4 years", "details": "Focus on mathematics, statistics, and programming. Take ML courses as electives."},
            {"phase": "M.Sc/M.Tech in Data Science", "duration": "2 years", "details": "Optional but highly recommended for deeper expertise."},
            {"phase": "Data Science Career", "duration": "Ongoing", "details": "Start as analyst, grow to data scientist, then lead/principal roles."},
        ],
        "skills_required": ["Python", "R", "SQL", "Machine Learning", "Statistics", "Deep Learning", "Data Visualization"],
        "certifications": ["Google Data Analytics Certificate", "IBM Data Science Professional", "Andrew Ng's ML Course"],
        "top_courses": ["Applied Data Science (Coursera)", "Fast.ai", "NPTEL Data Science Courses"],
        "avg_salary": "₹8-30 LPA (India)",
    },
    "Medicine": {
        "description": "Diagnose and treat illnesses, improve patient health, and contribute to medical research.",
        "after_10th": [
            {"phase": "11th-12th (Science - Biology)", "duration": "2 years", "details": "Take PCB (Physics, Chemistry, Biology). Prepare for NEET examination alongside board exams."},
            {"phase": "NEET Exam & MBBS", "duration": "5.5 years", "details": "Clear NEET UG to get admission to a medical college. Complete MBBS degree."},
            {"phase": "Internship", "duration": "1 year", "details": "Compulsory rotating internship in various hospital departments."},
            {"phase": "PG Specialization (MD/MS)", "duration": "3 years", "details": "Appear for NEET PG. Specialize in Surgery, Pediatrics, Cardiology, etc."},
            {"phase": "Practice / Super-Specialization", "duration": "Ongoing", "details": "Start practice or pursue DM/MCh for super-specialization."},
        ],
        "after_12th": [
            {"phase": "NEET Exam & MBBS", "duration": "5.5 years", "details": "Clear NEET UG and pursue MBBS from a recognized medical college."},
            {"phase": "Internship", "duration": "1 year", "details": "Complete compulsory internship and gain clinical experience."},
            {"phase": "MD/MS Specialization", "duration": "3 years", "details": "Specialize through NEET PG in your chosen field."},
            {"phase": "Independent Practice", "duration": "Ongoing", "details": "Start private practice or join a hospital."},
        ],
        "skills_required": ["Biology", "Chemistry", "Patient Communication", "Clinical Skills", "Research Methodology"],
        "certifications": ["NEET UG", "NEET PG", "USMLE (for abroad)"],
        "top_courses": ["MBBS", "AIIMS courses", "WHO Online Courses"],
        "avg_salary": "₹8-50 LPA (India)",
    },
    "Law": {
        "description": "Advocate for justice, draft legal documents, and represent clients in courts.",
        "after_10th": [
            {"phase": "11th-12th (Any Stream)", "duration": "2 years", "details": "Any stream works. Arts/Humanities recommended. Focus on English and Social Studies."},
            {"phase": "5-Year Integrated LLB (BA LLB/BBA LLB)", "duration": "5 years", "details": "Clear CLAT or AILET. Enroll in a National Law University for integrated law degree."},
            {"phase": "Internships & Mooting", "duration": "During college", "details": "Intern at law firms, courts, and NGOs. Participate in moot court competitions."},
            {"phase": "Junior Advocate / Associate", "duration": "2-3 years", "details": "Start practicing under a senior advocate or join a law firm."},
            {"phase": "Independent Practice / Specialization", "duration": "Ongoing", "details": "Specialize in Corporate Law, Criminal Law, IP Law, or Constitutional Law."},
        ],
        "after_12th": [
            {"phase": "5-Year BA LLB / 3-Year LLB", "duration": "3-5 years", "details": "Clear CLAT for 5-year program or complete graduation first then 3-year LLB."},
            {"phase": "Bar Council Registration", "duration": "After LLB", "details": "Register with Bar Council of India to practice law."},
            {"phase": "Legal Career", "duration": "Ongoing", "details": "Litigation, corporate law, judiciary preparation, or legal consulting."},
        ],
        "skills_required": ["Legal Research", "Argumentation", "Writing", "Public Speaking", "Constitutional Knowledge"],
        "certifications": ["CLAT", "AILET", "Bar Council Registration"],
        "top_courses": ["NLU Programs", "Coursera Legal Courses", "NALSAR Distance Education"],
        "avg_salary": "₹5-30 LPA (India)",
    },
    "Business & Finance": {
        "description": "Manage businesses, analyze financial markets, and drive organizational growth.",
        "after_10th": [
            {"phase": "11th-12th (Commerce Stream)", "duration": "2 years", "details": "Take Commerce with Mathematics. Study Accountancy, Business Studies, and Economics."},
            {"phase": "BBA / B.Com (Hons)", "duration": "3 years", "details": "Pursue business or commerce degree from a top college."},
            {"phase": "MBA / CA / CFA", "duration": "2-3 years", "details": "Get MBA from a top B-school (CAT/GMAT) or pursue CA/CFA for finance specialization."},
            {"phase": "Management Trainee / Analyst", "duration": "1-2 years", "details": "Join consulting firms, banks, or corporates as a management trainee."},
            {"phase": "Senior Management", "duration": "5+ years", "details": "Grow into VP, Director, or C-suite roles with experience."},
        ],
        "after_12th": [
            {"phase": "BBA / B.Com / BMS", "duration": "3 years", "details": "Pursue an undergraduate business degree. Start preparing for CA if interested."},
            {"phase": "MBA / Professional Cert", "duration": "2 years", "details": "Write CAT/XAT for MBA or pursue CA/CFA."},
            {"phase": "Corporate Career", "duration": "Ongoing", "details": "Banking, consulting, startups, or financial markets."},
        ],
        "skills_required": ["Financial Analysis", "Excel", "Communication", "Strategy", "Leadership", "Data Analysis"],
        "certifications": ["CA", "CFA", "MBA (IIM)", "CPA"],
        "top_courses": ["IIM Programs", "CFA Institute", "Coursera Business Specializations"],
        "avg_salary": "₹6-40 LPA (India)",
    },
    "Design & UX": {
        "description": "Create beautiful, user-friendly digital experiences and solve problems through visual design.",
        "after_10th": [
            {"phase": "11th-12th (Any Stream)", "duration": "2 years", "details": "Any stream. Focus on developing artistic skills. Start learning design software."},
            {"phase": "B.Des / BFA / B.Sc in Design", "duration": "4 years", "details": "Clear NID/NIFT/UCEED entrance exams. Study design fundamentals and specialization."},
            {"phase": "Portfolio & Internships", "duration": "During college", "details": "Build a strong portfolio. Intern at design studios and tech companies."},
            {"phase": "Junior Designer / UX Designer", "duration": "1-2 years", "details": "Join a product company or design agency."},
            {"phase": "Senior / Lead Designer", "duration": "3-5 years", "details": "Lead design teams, work on complex product design challenges."},
        ],
        "after_12th": [
            {"phase": "B.Des at NID/NIFT/IIT", "duration": "4 years", "details": "Pursue a design degree from top design institutes."},
            {"phase": "Build Portfolio", "duration": "Ongoing", "details": "Create case studies, freelance projects, and design challenges."},
            {"phase": "Design Career", "duration": "Ongoing", "details": "UI/UX design, product design, brand design, or motion design."},
        ],
        "skills_required": ["Figma", "Adobe Creative Suite", "User Research", "Prototyping", "Visual Design", "Typography"],
        "certifications": ["Google UX Design Certificate", "Interaction Design Foundation", "NID Diploma"],
        "top_courses": ["NID Programs", "Google UX Design (Coursera)", "Designlab"],
        "avg_salary": "₹5-25 LPA (India)",
    },
    "Teaching & Education": {
        "description": "Shape future generations by educating students and innovating learning methods.",
        "after_10th": [
            {"phase": "11th-12th (Any Stream)", "duration": "2 years", "details": "Choose a stream aligned with the subject you want to teach."},
            {"phase": "B.A/B.Sc + B.Ed", "duration": "4-5 years", "details": "Complete graduation in your subject, then pursue B.Ed for teaching qualification."},
            {"phase": "TET / CTET Exam", "duration": "After B.Ed", "details": "Clear TET/CTET for government school teaching positions."},
            {"phase": "Teaching Career", "duration": "Ongoing", "details": "Join schools or coaching institutes. Pursue NET/SET for college teaching."},
            {"phase": "M.Ed / Ph.D", "duration": "2-5 years", "details": "For higher education teaching and educational research."},
        ],
        "after_12th": [
            {"phase": "Integrated B.A.B.Ed / B.Sc.B.Ed", "duration": "4 years", "details": "Opt for an integrated program or complete graduation + B.Ed."},
            {"phase": "Teaching Certification", "duration": "1 year", "details": "Clear CTET/TET for certification."},
            {"phase": "Teaching Career", "duration": "Ongoing", "details": "School teacher, EdTech, private tutor, or professor track."},
        ],
        "skills_required": ["Communication", "Patience", "Subject Expertise", "Classroom Management", "EdTech Tools"],
        "certifications": ["B.Ed", "CTET", "NET/SET", "Cambridge Teaching Certificate"],
        "top_courses": ["B.Ed Programs", "Coursera Teaching Specializations", "Cambridge TKT"],
        "avg_salary": "₹3-15 LPA (India)",
    },
    "Mechanical Engineering": {
        "description": "Design, analyze, and manufacture mechanical systems from engines to robots.",
        "after_10th": [
            {"phase": "11th-12th (Science - PCM)", "duration": "2 years", "details": "Take Physics, Chemistry, Mathematics. Focus on physics and applied math."},
            {"phase": "B.Tech in Mechanical Engineering", "duration": "4 years", "details": "Clear JEE Main/Advanced. Study mechanics, thermodynamics, manufacturing, and design."},
            {"phase": "Internships & Projects", "duration": "During college", "details": "Intern at manufacturing companies, work on SAE/robotics projects."},
            {"phase": "Graduate Engineer Trainee", "duration": "1-2 years", "details": "Join automotive, aerospace, or manufacturing companies."},
            {"phase": "Senior Engineer / Specialist", "duration": "3-5 years", "details": "Specialize in design, thermal, automotive, or robotics."},
        ],
        "after_12th": [
            {"phase": "B.Tech Mechanical Engineering", "duration": "4 years", "details": "Pursue mechanical engineering from a reputed college."},
            {"phase": "Industry Experience", "duration": "2-3 years", "details": "Work in core mechanical roles or transition to allied fields."},
            {"phase": "M.Tech / MBA", "duration": "2 years", "details": "Specialize further or move to management roles."},
        ],
        "skills_required": ["AutoCAD", "SolidWorks", "Thermodynamics", "Material Science", "FEA", "3D Printing"],
        "certifications": ["GATE", "AutoCAD Professional", "Six Sigma", "SolidWorks Associate"],
        "top_courses": ["IIT B.Tech Programs", "NPTEL Courses", "Coursera Engineering Specializations"],
        "avg_salary": "₹4-20 LPA (India)",
    },
    "Civil Engineering": {
        "description": "Plan, design, and supervise construction of infrastructure like bridges, roads, and buildings.",
        "after_10th": [
            {"phase": "11th-12th (Science - PCM)", "duration": "2 years", "details": "Take PCM. Focus on mathematics and physics fundamentals."},
            {"phase": "B.Tech in Civil Engineering", "duration": "4 years", "details": "Clear JEE Main. Study structural engineering, geotechnics, and surveying."},
            {"phase": "Internships & Site Experience", "duration": "During college", "details": "Intern at construction companies. Visit project sites for practical exposure."},
            {"phase": "Junior Civil Engineer", "duration": "1-2 years", "details": "Join construction or consulting firms. Work on real projects."},
            {"phase": "Senior Engineer / Project Manager", "duration": "3-5 years", "details": "Lead projects, manage teams, and get professional certifications."},
        ],
        "after_12th": [
            {"phase": "B.Tech Civil Engineering", "duration": "4 years", "details": "Pursue civil engineering from a reputed engineering college."},
            {"phase": "GATE / M.Tech", "duration": "2 years", "details": "For PSU recruitment or higher studies specialization."},
            {"phase": "Civil Engineering Career", "duration": "Ongoing", "details": "Construction firms, government departments, consultancies."},
        ],
        "skills_required": ["AutoCAD", "STAAD Pro", "Surveying", "Project Management", "Structural Analysis"],
        "certifications": ["GATE", "PMP", "LEED Green Associate", "AutoCAD Civil 3D"],
        "top_courses": ["IIT/NIT Programs", "NPTEL Civil Engineering", "Coursera Construction Management"],
        "avg_salary": "₹4-18 LPA (India)",
    },
    "Journalism & Media": {
        "description": "Report news, create content, and inform the public through various media channels.",
        "after_10th": [
            {"phase": "11th-12th (Arts/Humanities)", "duration": "2 years", "details": "Take Arts with English, Political Science, History. Develop writing and current affairs knowledge."},
            {"phase": "BA in Journalism / Mass Communication", "duration": "3 years", "details": "Enroll in a reputed journalism school. Learn reporting, editing, and media production."},
            {"phase": "Internships & Portfolio", "duration": "During college", "details": "Write for newspapers, blogs, and student magazines. Intern at media houses."},
            {"phase": "Junior Reporter / Content Creator", "duration": "1-2 years", "details": "Join a media organization. Build your byline and reporting experience."},
            {"phase": "Senior Journalist / Editor", "duration": "3-5 years", "details": "Specialize in beats like politics, tech, or business. Move to editorial roles."},
        ],
        "after_12th": [
            {"phase": "BJMC / BA Mass Communication", "duration": "3 years", "details": "Pursue journalism degree from a recognized university."},
            {"phase": "MA / PG Diploma", "duration": "2 years", "details": "Specialize in broadcast, digital, or print journalism."},
            {"phase": "Media Career", "duration": "Ongoing", "details": "Print, digital, broadcast, or independent journalism."},
        ],
        "skills_required": ["Writing", "Storytelling", "Video Production", "Social Media", "Investigative Research"],
        "certifications": ["Google News Initiative", "Reuters Journalism Courses", "Digital Marketing Certificates"],
        "top_courses": ["IIMC Programs", "ACJ Chennai", "Coursera Journalism Specializations"],
        "avg_salary": "₹3-15 LPA (India)",
    },
    "Psychology & Counseling": {
        "description": "Understand human behavior, provide mental health support, and help people improve their well-being.",
        "after_10th": [
            {"phase": "11th-12th (Any Stream, Arts preferred)", "duration": "2 years", "details": "Arts recommended. Take Psychology as a subject if available."},
            {"phase": "BA / B.Sc in Psychology", "duration": "3 years", "details": "Study psychology fundamentals, research methods, and clinical basics."},
            {"phase": "MA / M.Sc in Psychology", "duration": "2 years", "details": "Specialize in Clinical, Counseling, Organizational, or Child Psychology."},
            {"phase": "RCI Registration / Certification", "duration": "After M.Phil", "details": "M.Phil in Clinical Psychology for RCI license to practice as a clinical psychologist."},
            {"phase": "Professional Practice", "duration": "Ongoing", "details": "Private practice, hospitals, corporate wellness, or research."},
        ],
        "after_12th": [
            {"phase": "BA/B.Sc Psychology", "duration": "3 years", "details": "Pursue an undergraduate degree in psychology."},
            {"phase": "MA + M.Phil", "duration": "3-4 years", "details": "Required for clinical practice registration with RCI."},
            {"phase": "Psychology Career", "duration": "Ongoing", "details": "Clinical practice, school counseling, corporate HR, or academia."},
        ],
        "skills_required": ["Active Listening", "Empathy", "Assessment Tools", "CBT/DBT", "Research Methods"],
        "certifications": ["RCI Registration", "NLP Certification", "REBT Certification"],
        "top_courses": ["TISS Programs", "Coursera Psychology Courses", "APA Online Learning"],
        "avg_salary": "₹3-12 LPA (India)",
    },
    "Biotechnology": {
        "description": "Apply biology and technology to develop solutions in healthcare, agriculture, and environment.",
        "after_10th": [
            {"phase": "11th-12th (Science - PCB/PCM)", "duration": "2 years", "details": "Take PCB (or PCM with Biology). Focus on Biology and Chemistry."},
            {"phase": "B.Tech/B.Sc in Biotechnology", "duration": "3-4 years", "details": "Learn molecular biology, genetics, bioinformatics, and bioprocess engineering."},
            {"phase": "M.Tech/M.Sc + Research", "duration": "2-3 years", "details": "Specialize in genomics, bioinformatics, or pharmaceutical biotech. Publish research."},
            {"phase": "Industry / Research Career", "duration": "Ongoing", "details": "Join pharma companies, biotech startups, or research organizations like CSIR."},
        ],
        "after_12th": [
            {"phase": "B.Tech/B.Sc Biotechnology", "duration": "3-4 years", "details": "Pursue biotechnology degree from a reputed university."},
            {"phase": "GATE / Higher Studies", "duration": "2-3 years", "details": "Clear GATE for M.Tech or go abroad for MS/PhD."},
            {"phase": "Biotech Career", "duration": "Ongoing", "details": "R&D labs, pharma industry, agri-biotech, or bioinformatics."},
        ],
        "skills_required": ["Molecular Biology", "Bioinformatics", "Laboratory Techniques", "Data Analysis", "Research Writing"],
        "certifications": ["GATE Biotech", "Bioinformatics Certification", "GLP/GMP Training"],
        "top_courses": ["IIT Biotech Programs", "NPTEL Biotech Courses", "Coursera Genomics"],
        "avg_salary": "₹4-15 LPA (India)",
    },
}


def generate_training_data(n_samples=2000):
    """Generate synthetic training data for ML models."""
    np.random.seed(42)
    random.seed(42)

    samples = []
    labels = []

    samples_per_career = n_samples // len(CAREER_DOMAINS)

    for career in CAREER_DOMAINS:
        profile = CAREER_PROFILES[career]
        score_ranges = profile["scores"]
        career_skills = profile["skills"]
        career_interests = profile["interests"]

        for _ in range(samples_per_career):
            # Generate scores within the career's profile range with some noise
            math = np.clip(np.random.normal(
                (score_ranges["math"][0] + score_ranges["math"][1]) / 2,
                (score_ranges["math"][1] - score_ranges["math"][0]) / 4
            ), 0, 100)
            science = np.clip(np.random.normal(
                (score_ranges["science"][0] + score_ranges["science"][1]) / 2,
                (score_ranges["science"][1] - score_ranges["science"][0]) / 4
            ), 0, 100)
            english = np.clip(np.random.normal(
                (score_ranges["english"][0] + score_ranges["english"][1]) / 2,
                (score_ranges["english"][1] - score_ranges["english"][0]) / 4
            ), 0, 100)
            logical = np.clip(np.random.normal(
                (score_ranges["logical_reasoning"][0] + score_ranges["logical_reasoning"][1]) / 2,
                (score_ranges["logical_reasoning"][1] - score_ranges["logical_reasoning"][0]) / 4
            ), 0, 100)

            # Generate skill vector (1 if selected, 0 otherwise)
            skill_vector = []
            for skill in AVAILABLE_SKILLS:
                if skill in career_skills:
                    skill_vector.append(1 if random.random() < 0.75 else 0)
                else:
                    skill_vector.append(1 if random.random() < 0.15 else 0)

            # Generate interest vector
            interest_vector = []
            for interest in AVAILABLE_INTERESTS:
                if interest in career_interests:
                    interest_vector.append(1 if random.random() < 0.75 else 0)
                else:
                    interest_vector.append(1 if random.random() < 0.12 else 0)

            feature = [math, science, english, logical] + skill_vector + interest_vector
            samples.append(feature)
            labels.append(career)

    return np.array(samples), np.array(labels)


def get_feature_names():
    """Return ordered list of feature names."""
    return (
        ["math", "science", "english", "logical_reasoning"]
        + [f"skill_{s.lower().replace(' ', '_')}" for s in AVAILABLE_SKILLS]
        + [f"interest_{i.lower().replace(' ', '_')}" for i in AVAILABLE_INTERESTS]
    )
