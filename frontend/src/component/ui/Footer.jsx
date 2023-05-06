import React from "react";
import styled from "styled-components";

const FooterWrapper = styled.footer`
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 50px;
  background-color: #eee;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const FooterText = styled.p`
  font-size: 14px;
  color: #333;
`;

function Footer() {
    return (
        <FooterWrapper>
            <FooterText>연락 : djgnfj8923@naver.com</FooterText>
        </FooterWrapper>
    );
}

export default Footer;
