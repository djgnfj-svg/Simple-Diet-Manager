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

const test = styled.div`
    display: flex;
`;
function WeekDietOutputPage(props) {
    const location = useLocation();
    const {state} = location;
    const DietMaledata = [
        {
          DietKcal: state.mon.total_kcal,
          DietProtein: state.mon.total_protein,
          DietFat: state.mon.total_fat,
          DietCarbs: state.mon.total_carbs,
        },
        {
          DietKcal: state.tue.total_kcal,
          DietProtein: state.tue.total_protein,
          DietFat: state.tue.total_fat,
          DietCarbs: state.tue.total_carbs,
        },
        {
            DietKcal : state.wed.total_kcal,
            DietProtein : state.wed.total_protein,
            DietFat : state.wed.total_fat,
            DietCarbs : state.wed.total_carbs,
        },
        {
            DietKcal : state.thu.total_kcal,
            DietProtein : state.thu.total_protein,
            DietFat : state.thu.total_fat,
            DietCarbs : state.thu.total_carbs,
        },
        {
            DietKcal : state.fri.total_kcal,
            DietProtein : state.fri.total_protein,
            DietFat : state.fri.total_fat,
            DietCarbs : state.fri.total_carbs,
        },
        {
            DietKcal : state.sat.total_kcal,
            DietProtein : state.sat.total_protein,
            DietFat : state.sat.total_fat,
            DietCarbs : state.sat.total_carbs,
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
            <DietUserBodyInfoCard metabolic={state.metabolic} />
            <DietCardList DietMaledata={DietMaledata} DietList={DietList}/>
        </Wrapper>
    );
}

export default WeekDietOutputPage;