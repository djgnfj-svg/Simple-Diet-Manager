import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import UserInputpage from './component/page/UserInputPage';
import WeekDietOutputPage from './component/page/WeekDietOutputPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<UserInputpage />} />
        <Route path="/diets" element={<WeekDietOutputPage/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
