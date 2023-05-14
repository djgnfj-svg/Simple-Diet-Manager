import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import UserInputpage from './component/page/UserInputPage';
import WeekDietOutputPage from './component/page/WeekDietOutputPage';
import DietDetailPage from './component/page/DietDetailPage';
import FoodListPage from './component/page/FoodListPage';
import Navbar from './component/ui/Navbar';
import Footer from './component/ui/Footer';
import LoginPage from './component/page/LoginPage';

function App() {
  return (
    <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path="/" element={<UserInputpage />} />
        <Route path="/diets" element={<WeekDietOutputPage/>} />
        <Route path="/diets/:id" element={<DietDetailPage/>} />
        <Route path="/food-list" element={<FoodListPage/>} />
        <Route path="/login" element={<LoginPage/>} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
