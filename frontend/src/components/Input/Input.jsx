import React from "react";
import styled from "styled-components";

const StyleInput = styled.div`
  position: relative;
  display: block;
  height: 50px;
  width: 100%;
  margin-bottom: 20px;

  & input {
    position: relative;
    display: block;
    height: 100%;
    width: 100%;
    border: none;
    border-bottom: 1px solid #ccc;
    padding: 0 10px;
    font-size: 16px;
    z-index: 1;
    background-color: transparent;

    &:focus {
      outline: none;
      border-bottom: 1px solid #ff5722;
    }

    &:focus + label,
    &:valid + label {
      top: 0;
      font-size: 12px;
      color: #ff5722;
      transform: translateY(-100%);
    }
  }

  & label {
    position: absolute;
    top: ${props => props.value ? '0' : '50%'};
    left: 10px;
    font-size: ${props => props.value ? '12px' : '16px'};
    color: ${props => props.value ? '#ff5722' : '#999'};
    transform: ${props => props.value ? 'translateY(-100%)' : 'translateY(-50%)'};
    transition: .3s ease-out;
    z-index: 0;
    pointer-events: none;
    background-color: #fff;
    padding: 0 5px;
  }
`;

function Input(props) {
    const {type, placeholder, value, onChange} = props;

    return (
        <StyleInput value={value}>
            <input type={type} value={value} onChange={onChange} required />
            <label>{placeholder}</label>
        </StyleInput>
    );
}

export default Input;
