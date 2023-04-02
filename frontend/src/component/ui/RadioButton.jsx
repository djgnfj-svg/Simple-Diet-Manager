import React from "react";
import styled from "styled-components";

const StyleGroup = styled.div`
  display: inline-flex;
  // 가로 정렬
  
  height: 100px;
  width: 100%;
  border-radius: 5px;
  `;

const StyleRadio = styled.input`
    display: none;
    &:checked + label {
        background: #ff5722;
    }
  `;

const StyleLabel = styled.label`
    background: #fff;
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    margin: 0 10px;
    border-radius: 5px;
    cursor: pointer;
    padding: 0 10px;
    border: 2px solid lightgrey;
    transition: all 0.3s ease;
`;

function RadioButton(props) {
    const { value, name, defaultChecked, disabled, placeholder, onChange, id } = props;
    return (
        <StyleGroup>
            <StyleRadio type="radio"
                value={value}
                name={name}
                defaultChecked={defaultChecked}
                disabled={disabled}
                onChange={onChange}
                id={id}
            />
            <StyleLabel for={id}>
                <span>{placeholder}</span>
            </StyleLabel>
        </StyleGroup>
    )
}

export default RadioButton;

