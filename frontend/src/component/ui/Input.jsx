import React from "react";
import styled from "styled-components";



const StyleInput = styled.input`
    display:block;
    height:50px;
    width:100%;
    border:none;
    border-bottom:1px solid #ccc;
    &::placeholder{
    -webkit-transform:translateY(0px);
        transform:translateY(0px);
    -webkit-transition:.5s;
        transition:.5s;
    }
    &:hover,
    &:focus,
    &:active:focus{
    color:#ff5722;
    outline:none;
    border-bottom:1px solid #ff5722;
    &::placeholder{
        color:#ff5722;
        position:relative;
        -webkit-transform:translateY(-20px);
        transform:translateY(-20px);
        
    }
    }
`;

function Input(props) {
    const {type, placeholder, onChange} = props;
    return <StyleInput type={type} placeholder={placeholder} onChange={onChange} />;
}

export default Input;