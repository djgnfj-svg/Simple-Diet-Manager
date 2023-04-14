import React from "react";
import styled from "styled-components";
import MealCard from "./MealCard";

const Wrapper = styled.div`
    outline: 0px;
    display: flex;
    color: rgb(0, 0, 0);
    position: relative;
    overflow: hidden;
    background-color: rgb(255, 255, 255);
    box-shadow: rgba(8, 60, 130, 0.06) 0px 0px 0px 0.05rem, rgba(30, 34, 40, 0.04) 0rem 0rem 1.25rem;
    border-radius: 15px;
    padding: 16px;
    margin-top: 16px;
`;


function DietMealCard(props) {
    const { MealList } = props;
    return (
        <Wrapper>
            {MealList.map((meal, index) => {
                return (
                    <MealCard meal={meal} meal_name_index={index} />
                )
            })
            }
            
        </Wrapper>
    );
}

export default DietMealCard;