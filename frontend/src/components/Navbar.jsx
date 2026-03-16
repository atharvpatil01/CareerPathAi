import { Link, useLocation } from 'react-router-dom';

export default function Navbar({ user, onLogout }) {
  const location = useLocation();

  const isActive = (path) => location.pathname === path ? 'active' : '';

  return (
    <nav className="navbar">
      <Link to="/" className="navbar-brand">
        <span className="brand-icon">🎯</span>
        CareerPath AI
      </Link>
      <ul className="navbar-links">
        <li><Link to="/" className={isActive('/')}>Home</Link></li>
        {user ? (
          <>
            <li><Link to="/profile" className={isActive('/profile')}>Profile</Link></li>
            <li><Link to="/dashboard" className={isActive('/dashboard')}>Dashboard</Link></li>
            <li>
              <span style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>
                Hi, {user.name.split(' ')[0]}
              </span>
            </li>
            <li>
              <button onClick={onLogout} className="btn btn-sm btn-secondary">
                Logout
              </button>
            </li>
          </>
        ) : (
          <li>
            <Link to="/auth" className="btn btn-sm btn-primary">
              Get Started
            </Link>
          </li>
        )}
      </ul>
    </nav>
  );
}
