import React from "react";
import styled from "styled-components";
import {useLocation } from "react-router-dom";

import DietUserBodyInfoCard from "../card/DietUserBodyInfoCard";
import DietCardList from "../list/DietCardList";


const Wrapper = styled.div`
    padding: 16px;
    widht: calc(100% - 32px);
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    border: 1px solid red;
`;

function WeekDietOutputPage(props) {
    const location = useLocation();
    const {state} = location;
    const DietMaledata = [
        {
          DietKcal: state.mon.diet_kcal,
          DietProtein: state.mon.diet_protein,
          DietFat: state.mon.diet_fat,
          DietCarbs: state.mon.diet_carbs,
        },
        {
          DietKcal: state.tue.diet_kcal,
          DietProtein: state.tue.diet_protein,
          DietFat: state.tue.diet_fat,
          DietCarbs: state.tue.diet_carbs,
        },
        {
            DietKcal : state.wed.diet_kcal,
            DietProtein : state.wed.diet_protein,
            DietFat : state.wed.diet_fat,
            DietCarbs : state.wed.diet_carbs,
        },
        {
            DietKcal : state.thu.diet_kcal,
            DietProtein : state.thu.diet_protein,
            DietFat : state.thu.diet_fat,
            DietCarbs : state.thu.diet_carbs,
        },
        {
            DietKcal : state.fri.diet_kcal,
            DietProtein : state.fri.diet_protein,
            DietFat : state.fri.diet_fat,
            DietCarbs : state.fri.diet_carbs,
        },
        {
            DietKcal : state.sat.diet_kcal,
            DietProtein : state.sat.diet_protein,
            DietFat : state.sat.diet_fat,
            DietCarbs : state.sat.diet_carbs,
        },
    ];
    const DietList = [
        [
          state.mon.breakfast,
          state.mon.lunch || null,
          state.mon.dinner || null,
        ],
        [
          state.tue.breakfast,
          state.tue.lunch || null,
          state.tue.dinner || null,
        ],
        [
          state.wed.breakfast,
          state.wed.lunch || null,
          state.wed.dinner || null,
        ],
        [
          state.thu.breakfast,
          state.thu.lunch || null,
          state.thu.dinner || null,
        ],
        [
          state.fri.breakfast,
          state.fri.lunch || null,
          state.fri.dinner || null,
        ],
        [
          state.sat.breakfast,
          state.sat.lunch || null,
          state.sat.dinner || null,
        ],
      ];
      
    return (
        <Wrapper>
            <DietUserBodyInfoCard diet_status={state.diet_status} min_nutrient={state.min_nutrient} max_nutrient={state.max_nutrient} />
            <DietCardList DietMaledata={DietMaledata} DietList={DietList}/>
        </Wrapper>
    );
}

export default WeekDietOutputPage;