import React from "react";
import styled from "styled-components";

const StyleButton = styled.button`
    background-color: #96ff33;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
    transition-duration: 0.4s;
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);

    :hover {
        background-color: #8AE52E;
        box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
    }
`;


function Button(props) {
    const { title, onClick, disabled } = props;
    return <StyleButton onClick={onClick} disabled={disabled}>{title || "button"}</StyleButton>;
}

export default Button;