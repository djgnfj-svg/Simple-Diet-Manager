import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import UserInputpage from './component/page/UserInputPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<UserInputpage />} />
        <Route path="/diets" element={<div/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
