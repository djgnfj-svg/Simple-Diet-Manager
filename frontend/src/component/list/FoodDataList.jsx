import React from 'react';
import styled from "styled-components";

const Wrapper = styled.div`
    outline: 0px;
    display: flex;
    -webkit-tap-highlight-color: transparent;
    text-decoration: none;
    color: rgb(0, 0, 0);
    box-sizing: border-box;
    position: relative;
    background-color: rgb(255, 255, 255);
    box-shadow: rgba(8, 60, 130, 0.06) 0px 0px 0px 0.05rem, rgba(30, 34, 40, 0.04) 0rem 0rem 1.25rem;
    border-radius: 15px;
    padding: 24px;
    margin-top: 16px;
    &:hover {
        background-color: #8AE52E;
    }
`;

const FoodListCard = styled.div`
    margin-left: 16px;
    max-width: 300px;
    text-align: center;

`;

const Styleimg = styled.img`
    width: 100px;
    height: 100px;
`;

const FoodDataString = styled.div`
    margin-bottom: 4px;
`;
function FoodDataList(props) {
    const { foods } = props;
    return (
        <>
            {foods.map((food, index) => {
                console.log(food);
                return (
                    <Wrapper>
                        <Styleimg src={process.env.REACT_APP_API + food.img} />
                        <FoodListCard>
                            <FoodDataString>이름 : {food.name}</FoodDataString>
                            <FoodDataString>칼로리 : {food.kcal}kcal</FoodDataString>
                            <FoodDataString>단백질 : {food.protein}g</FoodDataString>
                            <FoodDataString>지방 : {food.fat}g</FoodDataString>
                            <FoodDataString>탄수화물 : {food.carbs}g</FoodDataString>
                        </FoodListCard>
                    </Wrapper>
                )
            })}
        </>
    );
}

export default FoodDataList;