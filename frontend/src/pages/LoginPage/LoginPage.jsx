// Path: frontend\src\component\page\LoginPage.jsx
import React, { useState } from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';
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
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('/dj-rest-auth/login/', {
                email: email,
                password: password,
            });

            // 로그인 성공 시 원하는 동작을 수행합니다.
            console.log('로그인 성공!', response.data);
        } catch (error) {
            // 로그인 실패 시 원하는 동작을 수행합니다.
            console.error('로그인 실패!', error.response.data);
        }
    };
    // 버튼눌리면 동작
    const handleLogin = () => {
        alert("Ver 0.4때 구현할 예정입니다.")
    }
    return (
        <Login>
            <LoginBox>
                <h1>Login</h1>
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
