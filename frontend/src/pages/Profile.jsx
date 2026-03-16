import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api';

export default function Profile({ user, onPredict }) {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [availableSkills, setAvailableSkills] = useState([]);
  const [availableInterests, setAvailableInterests] = useState([]);

  const [scores, setScores] = useState({
    math: 75,
    science: 75,
    english: 75,
    logical_reasoning: 75,
  });
  const [selectedSkills, setSelectedSkills] = useState([]);
  const [selectedInterests, setSelectedInterests] = useState([]);

  useEffect(() => {
    api.getOptions()
      .then((data) => {
        setAvailableSkills(data.skills);
        setAvailableInterests(data.interests);
      })
      .catch(() => {
        // Fallback
        setAvailableSkills([
          'Programming', 'Mathematics', 'Communication', 'Problem Solving',
          'Creativity', 'Leadership', 'Analytical Thinking', 'Writing',
          'Research', 'Teamwork', 'Public Speaking', 'Critical Thinking',
          'Design', 'Data Analysis', 'Time Management',
        ]);
        setAvailableInterests([
          'Technology', 'Science', 'Arts', 'Business', 'Healthcare',
          'Social Work', 'Sports', 'Music', 'Literature', 'Environment',
          'Politics', 'Education', 'Media', 'Engineering', 'Finance',
        ]);
      });
  }, []);

  const toggleSkill = (skill) => {
    setSelectedSkills((prev) =>
      prev.includes(skill) ? prev.filter((s) => s !== skill) : [...prev, skill]
    );
  };

  const toggleInterest = (interest) => {
    setSelectedInterests((prev) =>
      prev.includes(interest) ? prev.filter((i) => i !== interest) : [...prev, interest]
    );
  };

  const handleSubmit = async () => {
    if (selectedSkills.length === 0) {
      setError('Please select at least one skill');
      return;
    }
    if (selectedInterests.length === 0) {
      setError('Please select at least one interest');
      return;
    }

    setError('');
    setLoading(true);

    try {
      const data = await api.predict({
        scores,
        skills: selectedSkills,
        interests: selectedInterests,
      });
      onPredict(data.predictions);
      navigate('/dashboard');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const scoreLabels = {
    math: '📐 Mathematics',
    science: '🔬 Science',
    english: '📖 English',
    logical_reasoning: '🧩 Logical Reasoning',
  };

  return (
    <main className="page">
      <div className="container">
        <div className="page-header animate-fade-in">
          <h1>Your Academic Profile</h1>
          <p>
            Tell us about your scores, skills, and interests — our AI will analyze
            your unique combination to find the best career paths for you.
          </p>
        </div>

        {error && (
          <div className="error-message animate-fade-in" style={{ maxWidth: 500, margin: '0 auto var(--space-xl)' }}>
            {error}
          </div>
        )}

        <div className="profile-grid">
          {/* Scores */}
          <div className="profile-section animate-fade-in-up delay-1">
            <h3>📊 Academic Scores</h3>
            <div className="glass-card">
              <div className="scores-grid">
                {Object.entries(scores).map(([key, value]) => (
                  <div key={key} className="score-slider">
                    <label>
                      <span>{scoreLabels[key]}</span>
                      <span className="score-value">{value}%</span>
                    </label>
                    <input
                      type="range"
                      min="0"
                      max="100"
                      value={value}
                      onChange={(e) =>
                        setScores((prev) => ({ ...prev, [key]: parseInt(e.target.value) }))
                      }
                    />
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Skills */}
          <div className="profile-section animate-fade-in-up delay-2">
            <h3>🛠️ Your Skills <span style={{ fontWeight: 400, fontSize: '0.85rem', color: 'var(--text-muted)' }}>({selectedSkills.length} selected)</span></h3>
            <div className="glass-card">
              <div className="tags-container">
                {availableSkills.map((skill) => (
                  <span
                    key={skill}
                    className={`tag ${selectedSkills.includes(skill) ? 'selected' : ''}`}
                    onClick={() => toggleSkill(skill)}
                  >
                    {selectedSkills.includes(skill) ? '✓ ' : ''}{skill}
                  </span>
                ))}
              </div>
            </div>
          </div>

          {/* Interests - Full Width */}
          <div className="profile-section animate-fade-in-up delay-3" style={{ gridColumn: '1 / -1' }}>
            <h3>💡 Your Interests <span style={{ fontWeight: 400, fontSize: '0.85rem', color: 'var(--text-muted)' }}>({selectedInterests.length} selected)</span></h3>
            <div className="glass-card">
              <div className="tags-container">
                {availableInterests.map((interest) => (
                  <span
                    key={interest}
                    className={`tag ${selectedInterests.includes(interest) ? 'selected' : ''}`}
                    onClick={() => toggleInterest(interest)}
                  >
                    {selectedInterests.includes(interest) ? '✓ ' : ''}{interest}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Submit */}
        <div className="submit-section animate-fade-in-up delay-4">
          <button
            className="btn btn-primary btn-lg"
            onClick={handleSubmit}
            disabled={loading}
          >
            {loading ? '🔄 Analyzing with AI...' : '🎯 Get Career Predictions'}
          </button>
          <p>Powered by Random Forest + XGBoost ML Ensemble</p>
        </div>
      </div>
    </main>
  );
}
