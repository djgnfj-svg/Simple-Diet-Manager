
import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
    padding: 16px;
`;

const Card = styled.div`
    outline: 0px;
    display: inline-block;
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

const StyleInfo = styled.div`
    display: flex;
    flex-direction: row;
    font-weight: 600;
    font-size: 1.25rem;
    letter-spacing: -0.025em;
    color: rgb(0, 0, 0);
    justify-content: space-between;
    margin-bottom: 1rem;
`;


function DietUserBodyInfoCard(props) {
    const {diet_status, min_nutrient, max_nutrient} = props
    return (
        <Wrapper>
            <Card>
                <StyleInfo>{diet_status === 1 ? "다이어트" : "유지"}를 위해서 먹어야 하는 양</StyleInfo>
                <StyleInfo>일요일은 드시고 싶은거 드세요</StyleInfo>
                <StyleInfo>일일 영양소</StyleInfo>
                <StyleInfo>칼로리 : {min_nutrient.kcal} ~ {max_nutrient.kcal}kcal</StyleInfo>
                <StyleInfo>탄수화물 : {min_nutrient.carbs} ~ {max_nutrient.carbs}g</StyleInfo>
                <StyleInfo>지방 : {min_nutrient.fat} ~ {max_nutrient.fat}g</StyleInfo>
                <StyleInfo>단백질 : {min_nutrient.protein} ~ {max_nutrient.protein}g</StyleInfo>
            </Card>
        </Wrapper>
    )
}

export default DietUserBodyInfoCard;