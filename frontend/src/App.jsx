import { useState } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import Landing from './pages/Landing';
import Auth from './pages/Auth';
import Profile from './pages/Profile';
import Dashboard from './pages/Dashboard';
import Roadmap from './pages/Roadmap';
import './index.css';

function App() {
  const [user, setUser] = useState(() => {
    const saved = localStorage.getItem('user');
    return saved ? JSON.parse(saved) : null;
  });

  const [predictions, setPredictions] = useState(() => {
    const saved = sessionStorage.getItem('predictions');
    return saved ? JSON.parse(saved) : null;
  });

  const handleLogin = (userData, token) => {
    setUser(userData);
    localStorage.setItem('user', JSON.stringify(userData));
    localStorage.setItem('token', token);
  };

  const handleLogout = () => {
    setUser(null);
    setPredictions(null);
    localStorage.removeItem('user');
    localStorage.removeItem('token');
    sessionStorage.removeItem('predictions');
  };

  const handlePredictions = (preds) => {
    setPredictions(preds);
    sessionStorage.setItem('predictions', JSON.stringify(preds));
  };

  return (
    <BrowserRouter>
      <Navbar user={user} onLogout={handleLogout} />
      <Routes>
        <Route path="/" element={<Landing user={user} />} />
        <Route
          path="/auth"
          element={
            user ? <Navigate to="/profile" /> : <Auth onLogin={handleLogin} />
          }
        />
        <Route
          path="/profile"
          element={
            user ? (
              <Profile user={user} onPredict={handlePredictions} />
            ) : (
              <Navigate to="/auth" />
            )
          }
        />
        <Route
          path="/dashboard"
          element={
            user ? (
              <Dashboard predictions={predictions} user={user} />
            ) : (
              <Navigate to="/auth" />
            )
          }
        />
        <Route
          path="/roadmap/:careerKey"
          element={
            user ? <Roadmap user={user} /> : <Navigate to="/auth" />
          }
        />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
      <footer className="footer">
        <p>© 2026 CareerPath AI — Empowering Students to Find Their Future</p>
      </footer>
    </BrowserRouter>
  );
}

export default App;
