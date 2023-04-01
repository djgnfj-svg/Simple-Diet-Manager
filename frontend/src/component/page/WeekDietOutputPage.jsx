import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
    padding: 16px;
    widht: calc(100% - 32px);
    height: 100%;
    max-height: 720px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 1px solid green;
`;

function WeekDietOutputPage(props) {
    const {} = props;

    return (
        <Wrapper>
        </Wrapper>
    );
}

export default WeekDietOutputPage;