import './App.css';
import 'bootstrap/dist/css/bootstrap.css';

import { BrowserRouter, Routes, Route } from 'react-router-dom';

import UserInputpage from './pages/UserInputPage/UserInputPage';
import WeekDietOutputPage from './pages/WeekDietOutputPage/WeekDietOutputPage';
import DietDetailPage from './pages/DietDetailPage/DietDetailPage';
import FoodListPage from './pages/FoodListPage/FoodListPage';
import LoginPage from './pages/LoginPage/LoginPage';
import RegistrationPage from './pages/RegistrationPage/RegistrationPage';
import ProfilePage from './pages/ProfilePage/ProfilePage';
import Footer from './components/Footer/Footer';
import My_Navbar from './components/Navbar/Navbar';
function App() {
  return (
      <BrowserRouter>
        <My_Navbar />
        <Routes>
          <Route path="/" element={<UserInputpage />} />
          <Route path="/diets" element={<WeekDietOutputPage />} />
          <Route path="/diets/:id" element={<DietDetailPage />} />
          <Route path="/food-list" element={<FoodListPage />} />
          <Route path="/profile" element={<ProfilePage />} /> {/* TODO: change to profile page */}
          <Route path="/login" element={<LoginPage />} />
          <Route path="/registration" element={<RegistrationPage />} />
        </Routes>
        <Footer />
      </BrowserRouter>
  );
}

export default App;
