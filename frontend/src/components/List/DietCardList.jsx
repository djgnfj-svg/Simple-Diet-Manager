import React from "react";
import styled from "styled-components";

import DietNutrientCard from "../Card/DietNutrientCard";
import DietMealCard from "../Card/DietMealCard";
import Button from '../Button/Button'

import { useNavigate } from "react-router-dom";

const Wrapper = styled.div`
    outline: 0px;
    display: inline-block;
    -webkit-tap-highlight-color: transparent;
    text-decoration: none;
    color: rgb(0, 0, 0);
    position: relative;
    overflow: hidden;
    background-color: rgb(255, 255, 255);
    box-shadow: rgba(8, 60, 130, 0.06) 0px 0px 0px 0.05rem, rgba(30, 34, 40, 0.04) 0rem 0rem 1.25rem;
    border-radius: 15px;

`;

const Card = styled.div`
    background-color: rgb(255, 255, 255);
    border-radius: 15px;
    padding: 24px;
    margin: 24px;
    &:hover {
        box-shadow: rgba(8, 60, 130, 0.06) 0px 0px 0px 0.05rem, rgba(30, 34, 40, 0.04) 0rem 0rem 1.25rem;
        transform: translateY(-5px);
        transition: all 0.3s ease-in-out;
        background-color: #4BBDDC;

    }
`;



function DietCardList(props) {
    const {DietMealdata, MealList} = props;
    const days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일"];
    const navigate = useNavigate();
    const onClick = (id) => {
        navigate(`/diets/${id}`)
    }
    return (
            <Wrapper>
                {days.map((day, index) => {
                    return(
                    <Card>
                        <h1>{day}</h1>
                        <DietNutrientCard DietMealdata={DietMealdata[index]}/>
                        <DietMealCard MealList={MealList[index]}/>
                        <Button onClick={() => onClick(DietMealdata[index].Id)}  title={`${day}식단 자세히 보기`}/>
                    </Card>
                    )
            })}
            </Wrapper>
    );
}

export default DietCardList;