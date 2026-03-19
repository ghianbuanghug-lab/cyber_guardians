// App.tsx
import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import { LoadingScreen } from './components/UI';
import AuthPage from './pages/AuthPage';
import Dashboard from './pages/Dashboard';
import Room1 from './pages/Room1';
import Room2 from './pages/Room2';
import Room3 from './pages/Room3';
import Results from './pages/Results';

function PrivateRoute({ children }: { children: React.ReactNode }) {
  const { user, isLoading } = useAuth();
  if (isLoading) return <LoadingScreen message="AUTHENTICATING..." />;
  if (!user) return <Navigate to="/auth" replace />;
  return <>{children}</>;
}

function PublicRoute({ children }: { children: React.ReactNode }) {
  const { user, isLoading } = useAuth();
  if (isLoading) return <LoadingScreen message="AUTHENTICATING..." />;
  if (user) return <Navigate to="/" replace />;
  return <>{children}</>;
}

function AppRoutes() {
  return (
    <Routes>
      <Route path="/auth" element={
        <PublicRoute><AuthPage /></PublicRoute>
      } />
      <Route path="/" element={
        <PrivateRoute><Dashboard /></PrivateRoute>
      } />
      <Route path="/room1" element={
        <PrivateRoute><Room1 /></PrivateRoute>
      } />
      <Route path="/room2" element={
        <PrivateRoute><Room2 /></PrivateRoute>
      } />
      <Route path="/room3" element={
        <PrivateRoute><Room3 /></PrivateRoute>
      } />
      <Route path="/results" element={
        <PrivateRoute><Results /></PrivateRoute>
      } />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <AppRoutes />
      </AuthProvider>
    </BrowserRouter>
  );
}
