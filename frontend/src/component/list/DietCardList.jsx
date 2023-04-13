import React from "react";
import styled from "styled-components";
import DietNutrientCard from "../card/DietNutrientCard";
import DietMealCard from "../card/DietMealCard";

const Wrapper = styled.div`
    outline: 0px;
    display: inline-block;
    min-width: 80%;
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
`;

function DietCardList(props) {
    const {DietMealdata, MealList} = props;
    const days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일"];
    const meals = ["breakfast", "lunch", "dinner"]
    return (
        <>
            <Wrapper>
                {days.map((day, index) => {
                    return(
                    <>
                        <h1>{day}</h1>
                        <DietNutrientCard DietMealdata={DietMealdata[index]}/>
                        <DietMealCard MealList={MealList[index]}/>
                    </>
                    )
            })}
            </Wrapper>
        </>
    );
}

export default DietCardList;