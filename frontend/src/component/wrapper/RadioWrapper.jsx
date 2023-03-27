import React from "react";
import styled from "styled-components";


const StyleRadioWrapper = styled.div`
    display: inline-flex;
    background: #fff;
    height: 100px;
    width: 400px;
    align-items: center;
    justify-content: space-evenly;
    border-radius: 5px;
    padding: 20px 15px;
    box-shadow: 5px 5px 30px rgba(0,0,0,0.2);
`;

function RadioWrapper(props) {
    return (
        <StyleRadioWrapper />
    )
}
export default RadioWrapper;