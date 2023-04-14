import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import UserInputpage from './component/page/UserInputPage';
import WeekDietOutputPage from './component/page/WeekDietOutputPage';
import DietDetailPage from './component/page/DietDetailPage';
import Navbar from './component/ui/Navbar';

function App() {
  return (
    <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path="/" element={<UserInputpage />} />
        <Route path="/diets" element={<WeekDietOutputPage/>} />
        <Route path="/diets/:id" element={<DietDetailPage/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
