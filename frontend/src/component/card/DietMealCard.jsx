import React from "react";
import styled from "styled-components";
import MealCard from "./MealCard";

const Wrapper = styled.div`
    outline: 0px;
    display: flex;
    -webkit-tap-highlight-color: transparent;
    text-decoration: none;
    color: rgb(0, 0, 0);
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
    background-color: rgb(255, 255, 255);
    box-shadow: rgba(8, 60, 130, 0.06) 0px 0px 0px 0.05rem, rgba(30, 34, 40, 0.04) 0rem 0rem 1.25rem;
    border-radius: 15px;
    padding: 24px;
    margin-top: 16px;
`;


const test = styled.div`
    display: inline-block;
`;

function DietMealCard(props) {
    const { } = props;

    return (
        <Wrapper>
            <MealCard />
            <MealCard />
            <MealCard />
        </Wrapper>
    );
}

export default DietMealCard;