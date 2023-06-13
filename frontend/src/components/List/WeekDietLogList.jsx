import React from 'react';
import styled from "styled-components";

const Wrapper = styled.div`
    margin: 10px;
    padding: 16px;
    width: calc(100% - 32px);
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

    const handleClick = (id) => {
        window.location.href = `${process.env.REACT_APP_API}/weekdiets/${id}`;
    }
    
    return (
        <Wrapper>
            {weekdiets.map((weekdiet) => (
                <WeekDietLogText key={weekdiet.id} onClick={() => handleClick(weekdiet.id)}>
                    {weekdiet.title}
                </WeekDietLogText>
            ))}
        </Wrapper>
    );
}

export default WeekDietLogList;
