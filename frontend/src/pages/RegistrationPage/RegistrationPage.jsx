// Path: frontend\src\component\page\LoginPage.jsx
import React, { useState } from 'react';
import styled from 'styled-components';
import { Link, useNavigate } from 'react-router-dom';
import Input from '../../components/Input/Input';
import Button from '../../components/Button/Button';
import axios from 'axios';

const Registration = styled.div`
    width: 100%;
    height: 100vh;
    background: #4BBDDC;
    display: flex;
    justify-content: center;
    align-items: center;
`;

const RegistrationBox = styled.div`
    width: 500px;
    height: 600px;
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

function RegistrationPage() {
    const navigate = useNavigate();

    // 구글 로그인 버튼
    const [isHovered, setIsHovered] = useState(false);
    const [isPressed, setIsPressed] = useState(false);
    let buttonImage = `${process.env.PUBLIC_URL}/btn_google_signin_dark_normal_web.png`;
    const handleMouseEnter = () => { setIsHovered(true);};
    const handleMouseLeave = () => { setIsHovered(false);};
    const handleMouseDown = () => { setIsPressed(true);};
    const handleMouseUp = () => { setIsPressed(false);};

    if (isPressed) {
        buttonImage = `${process.env.PUBLIC_URL}/btn_google_signin_dark_pressed_web.png`;
    } else if (isHovered) {
        buttonImage = `${process.env.PUBLIC_URL}/btn_google_signin_dark_focus_web.png`;
    }
    const handleLogin = () => {
        alert("Ver 0.4때 구현할 예정입니다.")
    }

    // 회원가입
    const [email, setEmail] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(`${process.env.REACT_APP_API}/dj-rest-auth/registration/`, {
                email: email,
                password1: password1,
                password2: password2,
            });
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            navigate('/profile');
        } catch (error) {
            alert("회원가입에 실패했습니다.")
            console.log(error.response.data);
            alert(error.response.data);
        }
    };

    const handleSignin = () => {
        navigate('/login');
    };

    return (
        <Registration>
            <RegistrationBox>
                <h1>회원가입</h1>
                <form style={{ alignItems: 'center' }} onSubmit={handleSubmit}>
                    <Input
                        type="text"
                        placeholder="Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                    <Input
                        type="password"
                        placeholder="Password1"
                        value={password1}
                        onChange={(e) => setPassword1(e.target.value)}
                    />
                    <Input
                        type="password"
                        placeholder="Password2"
                        value={password2}
                        onChange={(e) => setPassword2(e.target.value)}
                    />
                    <Button type="submit" title="회원가입" />
                </form>
                <Button title="로그인으로" onClick={handleSignin} />
                <LoginButton
                    src={buttonImage}
                    alt="Google"
                    onMouseEnter={handleMouseEnter}
                    onMouseLeave={handleMouseLeave}
                    onMouseDown={handleMouseDown}
                    onMouseUp={handleMouseUp}
                    onClick={handleLogin}
                />
            </RegistrationBox>
        </Registration>
    );
}

export default RegistrationPage;