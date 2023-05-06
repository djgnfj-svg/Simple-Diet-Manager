import React from "react";
import styled from "styled-components";

const StyleButton = styled.button`
    background-color: #2196f3;
    color: white;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s ease-in-out;

    &:hover {
        background-color: #1976d2;
    }

    &:focus {
        outline: none;
    }
`;


function Button(props) {
    const { title, onClick, disabled, isLoading } = props;
    return <StyleButton onClick={onClick}
     disabled={disabled || isLoading}>
        {title || "button"}
        </StyleButton>;
}

export default Button;