import { Link } from 'react-router-dom';

export default function Landing({ user }) {
  const particles = Array.from({ length: 20 }, (_, i) => ({
    id: i,
    left: `${Math.random() * 100}%`,
    top: `${Math.random() * 100}%`,
    delay: `${Math.random() * 5}s`,
    size: `${3 + Math.random() * 4}px`,
    opacity: 0.15 + Math.random() * 0.25,
  }));

  return (
    <main className="page">
      <div className="container">
        {/* Hero */}
        <section className="hero animate-fade-in">
          <div className="hero-particles">
            {particles.map((p) => (
              <div
                key={p.id}
                className="hero-particle"
                style={{
                  left: p.left,
                  top: p.top,
                  animationDelay: p.delay,
                  width: p.size,
                  height: p.size,
                  opacity: p.opacity,
                }}
              />
            ))}
          </div>

          <h1 className="animate-fade-in-up">
            Discover Your <span className="gradient-text">Perfect Career</span>
            <br />
            After 10th & 12th
          </h1>
          <p className="animate-fade-in-up delay-1">
            AI-powered career guidance tailored for Indian students.
            Get personalized recommendations based on your scores, skills,
            and interests — with a complete roadmap to success.
          </p>
          <div className="hero-buttons animate-fade-in-up delay-2">
            <Link to={user ? '/profile' : '/auth'} className="btn btn-primary btn-lg">
              🚀 Start Your Journey
            </Link>
            <a href="#features" className="btn btn-secondary btn-lg">
              Learn More ↓
            </a>
          </div>
        </section>

        {/* Stats */}
        <section style={{
          display: 'flex',
          justifyContent: 'center',
          gap: '3rem',
          marginTop: '4rem',
          flexWrap: 'wrap',
        }}>
          {[
            { value: '12+', label: 'Career Domains' },
            { value: 'AI', label: 'ML Predictions' },
            { value: '100%', label: 'Personalized' },
            { value: 'Free', label: 'For Students' },
          ].map((stat, i) => (
            <div key={i} className={`animate-fade-in-up delay-${i + 1}`} style={{ textAlign: 'center' }}>
              <div style={{
                fontSize: '2rem',
                fontWeight: 800,
                background: 'var(--gradient-primary)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                backgroundClip: 'text',
              }}>
                {stat.value}
              </div>
              <div style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginTop: '0.25rem' }}>
                {stat.label}
              </div>
            </div>
          ))}
        </section>

        {/* Features */}
        <section id="features" className="features-grid" style={{ paddingBottom: '4rem' }}>
          {[
            {
              icon: '📝',
              title: 'Smart Assessment',
              desc: 'Enter your academic scores, select your skills, and pick your interests. Our system analyzes your unique combination.',
            },
            {
              icon: '🤖',
              title: 'AI Career Prediction',
              desc: 'Our ML engine (Random Forest + XGBoost ensemble) predicts the best career domains for you with confidence scores.',
            },
            {
              icon: '🗺️',
              title: 'Personalized Roadmap',
              desc: 'Get a step-by-step career roadmap tailored to your education level — with courses, certifications, and timelines.',
            },
            {
              icon: '📊',
              title: 'Skill Mapping',
              desc: 'See which skills you already have and which ones you need to develop for your chosen career path.',
            },
            {
              icon: '🎓',
              title: 'Course Recommendations',
              desc: 'Discover the best courses, colleges, and certifications to fast-track your career journey.',
            },
            {
              icon: '💰',
              title: 'Salary Insights',
              desc: 'Know the expected salary ranges for each career path in India to make informed decisions.',
            },
          ].map((feature, i) => (
            <div key={i} className={`glass-card feature-card animate-fade-in-up delay-${(i % 5) + 1}`}>
              <span className="feature-icon">{feature.icon}</span>
              <h3>{feature.title}</h3>
              <p>{feature.desc}</p>
            </div>
          ))}
        </section>

        {/* How it works */}
        <section style={{ textAlign: 'center', paddingBottom: '4rem' }}>
          <h2 style={{
            fontSize: '2rem',
            fontWeight: 800,
            marginBottom: '3rem',
            background: 'var(--gradient-primary)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
          }}>
            How It Works
          </h2>
          <div style={{
            display: 'flex',
            justifyContent: 'center',
            gap: '2rem',
            flexWrap: 'wrap',
          }}>
            {[
              { step: '1', title: 'Register', desc: 'Create your account' },
              { step: '2', title: 'Fill Profile', desc: 'Enter scores & skills' },
              { step: '3', title: 'Get Predictions', desc: 'AI analyzes your data' },
              { step: '4', title: 'View Roadmap', desc: 'Follow your career path' },
            ].map((item, i) => (
              <div key={i} className={`animate-fade-in-up delay-${i + 1}`} style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: '0.75rem',
                width: '180px',
              }}>
                <div style={{
                  width: '3.5rem',
                  height: '3.5rem',
                  borderRadius: '50%',
                  background: 'var(--gradient-primary)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '1.3rem',
                  fontWeight: 800,
                  color: 'white',
                  boxShadow: '0 0 20px rgba(139,92,246,0.3)',
                }}>
                  {item.step}
                </div>
                <h4 style={{ fontWeight: 700 }}>{item.title}</h4>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>{item.desc}</p>
              </div>
            ))}
          </div>
        </section>
      </div>
    </main>
  );
}
