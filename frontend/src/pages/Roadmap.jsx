import { useState, useEffect } from 'react';
import { useParams, useSearchParams, Link } from 'react-router-dom';
import { api } from '../api';

export default function Roadmap({ user }) {
  const { careerKey } = useParams();
  const [searchParams] = useSearchParams();
  const confidence = searchParams.get('confidence');

  const [roadmap, setRoadmap] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    setLoading(true);
    api
      .getRoadmap(careerKey, user.education_level || '12th')
      .then((data) => {
        setRoadmap(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, [careerKey, user.education_level]);

  if (loading) {
    return (
      <main className="page">
        <div className="loader">
          <div className="spinner" />
        </div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="page">
        <div className="container" style={{ textAlign: 'center', padding: '4rem 0' }}>
          <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>⚠️</div>
          <h2>Roadmap Not Found</h2>
          <p style={{ color: 'var(--text-secondary)', margin: '1rem 0 2rem' }}>{error}</p>
          <Link to="/dashboard" className="btn btn-primary">← Back to Dashboard</Link>
        </div>
      </main>
    );
  }

  return (
    <main className="page">
      <div className="container">
        {/* Header */}
        <div className="roadmap-header animate-fade-in">
          <Link to="/dashboard" style={{
            color: 'var(--text-muted)',
            fontSize: '0.9rem',
            display: 'inline-flex',
            alignItems: 'center',
            gap: '0.5rem',
            marginBottom: '1rem',
          }}>
            ← Back to Dashboard
          </Link>
          <h1 className="career-title">{roadmap.career}</h1>
          <p className="career-desc">{roadmap.description}</p>
          {confidence && (
            <div style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.5rem',
              marginTop: '1rem',
              padding: '0.4rem 1rem',
              background: 'rgba(139,92,246,0.12)',
              border: '1px solid rgba(139,92,246,0.25)',
              borderRadius: 'var(--radius-full)',
              color: 'var(--accent-purple)',
              fontWeight: 600,
              fontSize: '0.9rem',
            }}>
              🎯 {confidence}% Match for You
            </div>
          )}
          <div style={{ marginTop: '0.75rem' }}>
            <span style={{
              padding: '0.3rem 0.8rem',
              background: 'rgba(6,182,212,0.12)',
              border: '1px solid rgba(6,182,212,0.25)',
              borderRadius: 'var(--radius-full)',
              color: 'var(--accent-cyan)',
              fontSize: '0.85rem',
              fontWeight: 500,
            }}>
              📚 Roadmap after {roadmap.education_level} Standard
            </span>
          </div>
        </div>

        <div className="roadmap-layout">
          {/* Timeline */}
          <div className="animate-fade-in-up delay-1">
            <h2 style={{
              fontSize: '1.4rem',
              fontWeight: 700,
              marginBottom: 'var(--space-xl)',
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem',
            }}>
              🛤️ Your Career Journey
            </h2>

            <div className="timeline">
              {roadmap.phases.map((phase, index) => (
                <div
                  key={index}
                  className="timeline-item"
                  style={{ animationDelay: `${0.15 * index}s` }}
                >
                  <div className="timeline-dot" />
                  <div className="timeline-content">
                    <div className="timeline-phase">{phase.phase}</div>
                    <div className="timeline-duration">⏱️ {phase.duration}</div>
                    <div className="timeline-details">{phase.details}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Sidebar */}
          <div className="roadmap-sidebar animate-fade-in-up delay-2">
            {/* Skills */}
            <div className="glass-card sidebar-card">
              <h3>🛠️ Skills to Build</h3>
              <ul className="sidebar-list">
                {roadmap.skills_required.map((skill) => (
                  <li key={skill}>{skill}</li>
                ))}
              </ul>
            </div>

            {/* Certifications */}
            <div className="glass-card sidebar-card">
              <h3>📜 Certifications</h3>
              <ul className="sidebar-list">
                {roadmap.certifications.map((cert) => (
                  <li key={cert}>{cert}</li>
                ))}
              </ul>
            </div>

            {/* Courses */}
            <div className="glass-card sidebar-card">
              <h3>🎓 Top Courses</h3>
              <ul className="sidebar-list">
                {roadmap.top_courses.map((course) => (
                  <li key={course}>{course}</li>
                ))}
              </ul>
            </div>

            {/* Salary */}
            <div className="glass-card sidebar-card">
              <h3>💰 Expected Salary</h3>
              <div className="salary-badge">
                {roadmap.avg_salary}
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
