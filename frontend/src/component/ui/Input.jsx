import React from "react";
import styled from "styled-components";



const StyleInput = styled.input`
    width: 100%;
    font-size: 32px;
    border-width: 1px;
    border-radius: 8px;
`;

function Input(props) {
    const {type, placeholder, onChange} = props;
    return <StyleInput type={type} placeholder={placeholder} onChange={onChange} />;
}

export default Input;