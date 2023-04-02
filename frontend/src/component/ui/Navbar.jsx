

// navbnrar component
import React from 'react';
import styled from 'styled-components';

const Nav = styled.nav`
    height: 70px;
    background: #090b13;
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



function Navbar() {
  return (
    <Nav>
      <Logo>
        <a href='/'>
        <img  src={`${process.env.PUBLIC_URL}/simple_diet.ico`} alt="Disney+" />
        </a>
      </Logo>
    </Nav>
  );
}


export default Navbar;
