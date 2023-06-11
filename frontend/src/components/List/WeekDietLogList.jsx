import React from 'react';
import styled from "styled-components";

const Wrapper = styled.div`
    margin: 10px;
    padding: 16px;
    widht: calc(100% - 32px);
    min-height: 300px;
    border: 1px solid;
`;

const WeekDietLogText = styled.div`
    padding: 8px;
    font-size: 32px;
    font-weight: bold;

    &:hover {
        color: #40a9ff;
        cursor: pointer;
        text-decoration: underline;
    }
`;

function WeekDietLogList(props) {
    const { weekdiets } = props;
    return (
        <>
            <Wrapper>
                {weekdiets.map((weekdiet, index) => (
                    <WeekDietLogText key={index}>{weekdiet.title}</WeekDietLogText>
                ))}
            </Wrapper>
        </>
    );
}


export default WeekDietLogList;