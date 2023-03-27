import React from "react";
import styled from "styled-components";

const StyleLabel = styled.label`

`;

const StyleRadio = styled.input`

`;

function RadioButton(props) {
    const { value, name, defaultChecked, disabled, placeholder, onChange } = props;
    return (
        <>
            <StyleRadio type="radio"
                value={value}
                name={name}
                defaultChecked={defaultChecked}
                disabled={disabled}
                onChange={onChange}
            />
            <StyleLabel>
                <span>{placeholder}</span>
            </StyleLabel>
        </>
    )
}

export default RadioButton;

