import React from "react";
import styled from "styled-components";

const StyleGroup = styled.div`
  display: inline-flex;
  height: 100px;
  width: 100%;
  border-radius: 5px;
`;

const StyleCheckbox = styled.input`
  display: none;
  text-align: center;
  &:checked + label {
    background: #4BBDDC;
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
  border: 2px solid;
  transition: all 0.3s ease;

  & > span {
    font-size: 1.5rem;
    font-weight: 600;
  }
`;

function Checkbox(props) {
  const { value, name, defaultChecked, disabled, placeholder, onChange, id } = props;
  return (
    <StyleGroup>
      <StyleCheckbox
        type="checkbox"
        value={value}
        name={name}
        defaultChecked={defaultChecked}
        disabled={disabled}
        onChange={onChange}
        id={id}
      />
      <StyleLabel htmlFor={id}>
        <span>{placeholder}</span>
      </StyleLabel>
    </StyleGroup>
  );
}

export default Checkbox;
