// Path: frontend\src\component\page\LoginPage.jsx
import React, { useState } from 'react';
import styled from 'styled-components';
import { Link, useNavigate  } from 'react-router-dom';
import Input from '../../components/Input/Input';
import Button from '../../components/Button/Button';
import axios from 'axios';

const Login = styled.div`
    width: 100%;
    height: 100vh;
    background: #4BBDDC;
    display: flex;
    justify-content: center;
    align-items: center;
`;

const LoginBox = styled.div`
    width: 500px;
    height: 500px;
    background: white;
    border-radius: 10px;
    padding: 40px;
    text-align: center;

    h1 {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 30px;
    }
`;

const LoginButton = styled.img`
    cursor: pointer;
    transition: opacity 0.5s ease;

    &:hover {
        opacity: 0.8;
    }
`;

function LoginPage() {
    const navigate = useNavigate();

    // 구글 로그인 버튼
    const [isHovered, setIsHovered] = useState(false);
    const [isPressed, setIsPressed] = useState(false);
    const handleMouseEnter = () => {setIsHovered(true);};
    const handleMouseLeave = () => {setIsHovered(false);};
    const handleMouseDown = () => {setIsPressed(true);};
    const handleMouseUp = () => {setIsPressed(false);};
    let buttonImage = `${process.env.PUBLIC_URL}/btn_google_signin_dark_normal_web.png`;
    if (isPressed) {
        buttonImage = `${process.env.PUBLIC_URL}/btn_google_signin_dark_pressed_web.png`;
    } else if (isHovered) {
        buttonImage = `${process.env.PUBLIC_URL}/btn_google_signin_dark_focus_web.png`;
    }
    
    // 버튼눌리면 동작
    const handleLogin = () => {
        alert("현재 V0.2로 구현 중입니다.")
    }
    // 로그인 버튼
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post(`${process.env.REACT_APP_API}/dj-rest-auth/login/`, {
                email: email,
                password: password,
            });
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            window.location.replace('/profile');
        } catch (error) {
            alert("로그인 실패하였습니다.")
            console.log(error.response.data.email)
        }
    };
    
    const handleSignup = () => {
        navigate('/registration');
      };

    return (
        <Login>
            <LoginBox>
                <h1>로그인</h1>
                    <form style={{alignItems: 'center'}} onSubmit={handleSubmit}>
                        <Input
                            type="text"
                            placeholder="Email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        <Input
                            type="password"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <Button type="submit" title="로그인" />
                    </form>
                <Button title="회원가입으로" onClick={handleSignup} />
                <LoginButton
                    src={buttonImage}
                    alt="Google"
                    onMouseEnter={handleMouseEnter}
                    onMouseLeave={handleMouseLeave}
                    onMouseDown={handleMouseDown}
                    onMouseUp={handleMouseUp}
                    onClick={handleLogin}
             />
                </LoginBox>
</Login>
);
}

export default LoginPage;