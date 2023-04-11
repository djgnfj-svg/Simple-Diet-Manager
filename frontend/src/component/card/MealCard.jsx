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
    margin-top: 16px;
    margin-left: 16px;
`;

const StyleMealCard = styled.div`
    display: flex;

`;

const Styleimg = styled.img`
    width: 100px;
    height: 100px;
`;

const StyleMealInfo = styled.div`
    margin-left: 16px;
    margin-right: 16px;
    font-weight: bold;
    color: #000000;
`;

function MealCard(props) {
    const { meal, meal_name_index } = props;
    const meal_name = ["아침", "점심", "저녁"];
    return (
        <>
            {
                meal === null
                    ?
                    <></>
                    :
                    <Wrapper>
                        <test>
                            <h1>{meal_name[meal_name_index]}</h1>
                            <StyleMealCard>
                                <Styleimg src={process.env.REACT_APP_API + meal.meal_img} />
                                <StyleMealInfo>
                                    <div>{meal.name}</div>
                                    <div>칼로리  : {meal.meal_kcal}kcal</div>
                                    <div>탄수화물 : {meal.meal_carbs}g</div>
                                    <div>단백질 : {meal.meal_protein}g</div>
                                    <div>지방 : {meal.meal_fat}g</div>
                                </StyleMealInfo>
                            </StyleMealCard>
                        </test>
                    </Wrapper>
            }
        </>
    );
}

export default MealCard;