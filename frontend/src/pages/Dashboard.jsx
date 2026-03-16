import { Link } from 'react-router-dom';

export default function Dashboard({ predictions, user }) {
  if (!predictions || predictions.length === 0) {
    return (
      <main className="page">
        <div className="container" style={{ textAlign: 'center' }}>
          <div className="animate-fade-in" style={{ padding: '4rem 0' }}>
            <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>📊</div>
            <h2 style={{ fontSize: '1.8rem', fontWeight: 700, marginBottom: '1rem' }}>
              No Predictions Yet
            </h2>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem' }}>
              Complete your profile to get AI-powered career predictions.
            </p>
            <Link to="/profile" className="btn btn-primary btn-lg">
              ✏️ Fill Your Profile
            </Link>
          </div>
        </div>
      </main>
    );
  }

  const getCareerKey = (name) =>
    name.toLowerCase().replace(/ & /g, '_and_').replace(/ /g, '_');

  const careerEmojis = {
    'Software Engineering': '💻',
    'Data Science': '📊',
    'Medicine': '🏥',
    'Law': '⚖️',
    'Business & Finance': '📈',
    'Design & UX': '🎨',
    'Teaching & Education': '👩‍🏫',
    'Mechanical Engineering': '⚙️',
    'Civil Engineering': '🏗️',
    'Journalism & Media': '📰',
    'Psychology & Counseling': '🧠',
    'Biotechnology': '🧬',
  };

  return (
    <main className="page">
      <div className="container">
        <div className="page-header animate-fade-in">
          <h1>Your Career Predictions</h1>
          <p>
            Based on your scores, skills, and interests — here are the top career
            paths recommended by our AI engine.
          </p>
        </div>

        <div className="predictions-grid">
          {predictions.map((pred, index) => (
            <div
              key={pred.career}
              className={`glass-card career-card animate-fade-in-up delay-${index + 1}`}
            >
              <div className={`card-rank rank-${index + 1}`}>#{index + 1}</div>

              <div style={{ fontSize: '2.5rem', marginBottom: 'var(--space-md)' }}>
                {careerEmojis[pred.career] || '🎯'}
              </div>

              <h3>{pred.career}</h3>
              <p className="card-description">{pred.description}</p>

              <div className="confidence-label">
                <span>Match Confidence</span>
                <span className="confidence-value">{pred.confidence}%</span>
              </div>
              <div className="confidence-bar">
                <div
                  className="confidence-fill"
                  style={{ width: `${pred.confidence}%` }}
                />
              </div>

              {pred.skills_required && pred.skills_required.length > 0 && (
                <div className="card-skills">
                  <h4>Key Skills Required</h4>
                  <div className="skill-tags">
                    {pred.skills_required.map((skill) => (
                      <span key={skill} className="skill-tag">{skill}</span>
                    ))}
                  </div>
                </div>
              )}

              <div className="card-action">
                <Link
                  to={`/roadmap/${getCareerKey(pred.career)}?confidence=${pred.confidence}`}
                  className="btn btn-primary"
                  style={{ width: '100%' }}
                >
                  🗺️ View Career Roadmap
                </Link>
              </div>
            </div>
          ))}
        </div>

        <div style={{ textAlign: 'center', marginTop: 'var(--space-2xl)' }} className="animate-fade-in-up delay-4">
          <Link to="/profile" className="btn btn-secondary">
            🔄 Try Different Inputs
          </Link>
        </div>
      </div>
    </main>
  );
}
