import React from "react";
import styled from "styled-components";


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
`;

function DietNutrientCard(props) {
    const {DietMealdata} = props;
    return (
        <Wrapper>
            <div> 칼로리 : {DietMealdata.DietKcal}kcal, 단백질 : {DietMealdata.DietProtein}g, 지방 : {DietMealdata.DietFat}g, 탄수화물 {DietMealdata.DietCarbs}g </div>
        </Wrapper>
    );
}

export default DietNutrientCard;