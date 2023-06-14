import axios from 'axios';
import React, { useState, useEffect } from 'react'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { useNavigate } from 'react-router-dom';

function My_Navbar() {
  const [auth, setAuth] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    // 현재는 토큰이 있다면 ~ 으로 되어있지만 추후 토큰이 유효한지 확인하는 로직을 넣어야함
    if (token !== null) {
      setAuth(true);
    }
  }, []);

  // 로그아웃함수
  const logout = async () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');

    axios.post(`${process.env.REACT_APP_API}/dj-rest-auth/logout/`,
      {},);

    setAuth(false);
    navigate('/');
  }

  return (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
      <Container>
        <Navbar.Brand href="/">간단식단</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/food-list">식품</Nav.Link>
          </Nav>
          <Nav>
            {/* TODO : 로그인 여부에 따라서 바뀌는 로직 */}
            {auth ? (
              <>
                <Nav.Link eventKey={2} href="/profile">
                  프로필
                </Nav.Link>
                <Nav.Link eventKey={3} onClick={logout}>
                  로그아웃
                </Nav.Link>
              </>
            ) : (
              <Nav.Link eventKey={2} href="/login">
                로그인
              </Nav.Link>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default My_Navbar;