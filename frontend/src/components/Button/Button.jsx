import React from "react";
import styled from "styled-components";

const StyleButton = styled.button`
box-sizing: border-box;
-webkit-appearance: none;
   -moz-appearance: none;
        appearance: none;
background-color: transparent;
border: 2px solid #e74c3c;
border-radius: 0.6em;
color: #e74c3c;
cursor: pointer;
align-self: center;
font-size: 1rem;
font-weight: 400;
line-height: 1;
margin: 20px;
padding: 1.2em 2.8em;
text-decoration: none;
text-align: center;
text-transform: uppercase;
font-family: "Montserrat", sans-serif;
font-weight: 700;


&:hover, &:focus {
    color: #fff;
    outline: 0;
    box-shadow: 0 0 40px 40px #e74c3c inset;
  }
  transition: box-shadow 300ms ease-in-out, color 300ms ease-in-out;

`;

const Wapper = styled.div`
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

`;


function Button(props) {
    const { title, onClick, disabled, isLoading, type } = props;
    return (
            <StyleButton onClick={onClick} disabled={disabled || isLoading} type={type}>
                {title || "button"}
            </StyleButton>
    );
}

export default Button;