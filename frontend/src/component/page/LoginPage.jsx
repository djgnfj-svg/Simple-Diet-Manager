// Path: frontend\src\component\page\LoginPage.jsx
import React, { useState } from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const Login = styled.div`
    width: 100%;
    height: 100vh;
    background: #4BBDDC;
    display: flex;
    justify-content: center;
    align-items: center;
`;

const LoginBox = styled.div`
    width: 400px;
    height: 400px;
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
    const [isHovered, setIsHovered] = useState(false);
    const [isPressed, setIsPressed] = useState(false);

    const handleMouseEnter = () => {
        setIsHovered(true);
    };

    const handleMouseLeave = () => {
        setIsHovered(false);
    };

    const handleMouseDown = () => {
        setIsPressed(true);
    };

    const handleMouseUp = () => {
        setIsPressed(false);
    };

    let buttonImage = `${process.env.PUBLIC_URL}/btn_google_signin_dark_normal_web.png`;

    if (isPressed) {
        buttonImage = `${process.env.PUBLIC_URL}/btn_google_signin_dark_pressed_web.png`;
    } else if (isHovered) {
        buttonImage = `${process.env.PUBLIC_URL}/btn_google_signin_dark_focus_web.png`;
    }

    // 버튼눌리면 동작
    const handleLogin = () => {
        alert("Ver 0.4때 구현할 예정입니다.")
    }
    return (
        <Login>
            <LoginBox>
                <h1>Login</h1>
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
