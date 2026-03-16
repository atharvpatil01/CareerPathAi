/**
 * API utility — handles all backend communication.
 */

const API_BASE = 'http://localhost:5000/api';

async function request(endpoint, options = {}) {
  const url = `${API_BASE}${endpoint}`;
  const token = localStorage.getItem('token');

  const headers = {
    'Content-Type': 'application/json',
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...options.headers,
  };

  const res = await fetch(url, { ...options, headers });
  const data = await res.json();

  if (!res.ok) {
    throw new Error(data.error || 'Something went wrong');
  }

  return data;
}

export const api = {
  // Auth
  register: (body) => request('/register', { method: 'POST', body: JSON.stringify(body) }),
  login: (body) => request('/login', { method: 'POST', body: JSON.stringify(body) }),

  // Prediction
  predict: (body) => request('/predict', { method: 'POST', body: JSON.stringify(body) }),
  getOptions: () => request('/options'),

  // Roadmap
  getRoadmap: (careerKey, educationLevel) =>
    request(`/roadmap/${careerKey}?education_level=${educationLevel}`),
  listCareers: () => request('/careers'),

  // Health
  health: () => request('/health'),
};
