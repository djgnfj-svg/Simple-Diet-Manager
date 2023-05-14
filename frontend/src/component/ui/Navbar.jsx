// navbnrar component
import React from 'react';
import styled from 'styled-components';

const Nav = styled.nav`
    height: 70px;
    background: #4BBDDC;
    display: flex;
    align-items: center;
    padding: 0 36px;
`;

const Logo = styled.a`
    width: 80px;
    margin-top: 4px;
    max-height: 70px;
    font-size: 0;
    display: inline-block;

    img {
        display: block;
        width: 70%;
    }
`;

const MenuItem = styled.a`
    color: white;
    font-size: 16px;
    text-decoration: none;
    margin-right: 20px;
    transition: opacity 0.3s ease;

    &:hover {
        opacity: 0.8;
    }
`;

const LoginButton = styled.button`
    background-color: transparent;
    border: none;
    color: white;
    font-size: 16px;
    cursor: pointer;
    margin-left: auto;
    padding: 10px;
    transition: background-color 0.3s ease;

    &:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }
`;


function Navbar() {
    return (
        <Nav>
            <Logo>
                <a href='/'>
                    <img src={`${process.env.PUBLIC_URL}/simple_diet.ico`} alt="Disney+" />
                </a>
            </Logo>
            <MenuItem href="/food-list">식품 리스트</MenuItem>
            <LoginButton>Login</LoginButton>
        </Nav>
    );
}

export default Navbar;
