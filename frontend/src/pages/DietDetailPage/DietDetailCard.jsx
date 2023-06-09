
import React from 'react';
import styled from "styled-components";

import FoodDataList from "../../components/List/FoodDataList";

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
    margin-left: 16px;
`;

function DietDetailCard(props) {
    const { meals } = props;
    const meal_name = ["아침", "점심", "저녁"]
    return (
        <>
            {Object.entries(meals).map((meal, index) => {
                return (
                    <Wrapper>
                        <div>
                            <h1>{meal_name[index]}</h1>
                            <div>이름 : {meal[1].name}</div>
                            <div>칼로리 : {meal[1].kcal}kcal</div>
                            <div>단백질 : {meal[1].protein}g</div>
                            <div>지방 : {meal[1].fat}g</div>
                            <div>탄수화물 : {meal[1].carbs}g</div>
                        <FoodDataList foods={meal[1].foods} />
                        </div>
                    </Wrapper>
                )
            })
            }
        </>
    );
}

export default DietDetailCard;