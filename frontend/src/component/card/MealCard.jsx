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

const test = styled.div`
    display: flex;
`;  
function MealCard(props) {
    const { } = props;

    return (
        <Wrapper>
            <test>
            <h1>아침</h1>
            <StyleMealCard>
            <Styleimg></Styleimg>
                <StyleMealInfo>
                    <div>음식이름 : 햇살닭 이름을 써보장..외2개</div>
                    <div>칼로리  : 000kcal</div>
                    <div>탄수화물 : 000g</div>
                    <div>단백질 : 000g</div>
                    <div>지방 : 00g</div>
                </StyleMealInfo>
            </StyleMealCard>
            </test>
        </Wrapper>
    );
}

export default MealCard;