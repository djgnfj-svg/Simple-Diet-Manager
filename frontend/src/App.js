import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import UserInputpage from './component/page/UserInputPage';
import WeekDietOutputPage from './component/page/WeekDietOutputPage';
import Navbar from './component/ui/Navbar';

function App() {
  return (
    <BrowserRouter>
      {/* TODO : navbar 만들기 */}
      <Navbar/>
      <Routes>
        <Route path="/" element={<UserInputpage />} />
        <Route path="/diets" element={<WeekDietOutputPage/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
