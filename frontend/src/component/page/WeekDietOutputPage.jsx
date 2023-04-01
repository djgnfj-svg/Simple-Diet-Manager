import React from "react";
import styled from "styled-components";

import DietUserBodyInfoCard from "../card/DietUserBodyInfoCard";
import DietCardList from "../list/DietCardList";


const Wrapper = styled.div`
    padding: 16px;
    widht: calc(100% - 32px);
    height: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    border: 1px solid red;
`;

const test = styled.div`
    display: flex;
`;
function WeekDietOutputPage(props) {
    const { } = props;

    return (
        <Wrapper>
            <DietUserBodyInfoCard />
            <DietCardList />
        </Wrapper>
    );
}

export default WeekDietOutputPage;