import React from "react";
import styled from "styled-components";
import { useLocation } from "react-router-dom";

import DietUserBodyInfoCard from "../card/DietUserBodyInfoCard";
import DietCardList from "../list/DietCardList";


const Wrapper = styled.div`
    padding: 16px;
    widht: calc(100% - 32px);
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    border: 1px solid;
`;

function WeekDietOutputPage(props) {
  const location = useLocation();
  const { state } = location;
  const DietMealdata = [
    {
      Id : state.diets.mon.id,
      DietKcal: state.diets.mon.kcal,
      DietProtein: state.diets.mon.protein,
      DietFat: state.diets.mon.fat,
      DietCarbs: state.diets.mon.carbs,
    },
    {
      Id : state.diets.tue.id,
      DietKcal: state.diets.tue.kcal,
      DietProtein: state.diets.tue.protein,
      DietFat: state.diets.tue.fat,
      DietCarbs: state.diets.tue.carbs,
    },
    {
      Id : state.diets.wed.id,
      DietKcal: state.diets.wed.kcal,
      DietProtein: state.diets.wed.protein,
      DietFat: state.diets.wed.fat,
      DietCarbs: state.diets.wed.carbs,
    },
    {
      Id : state.diets.thu.id,
      DietKcal: state.diets.thu.kcal,
      DietProtein: state.diets.thu.protein,
      DietFat: state.diets.thu.fat,
      DietCarbs: state.diets.thu.carbs,
    },
    {
      Id : state.diets.fri.id,
      DietKcal: state.diets.fri.kcal,
      DietProtein: state.diets.fri.protein,
      DietFat: state.diets.fri.fat,
      DietCarbs: state.diets.fri.carbs,
    },
    {
      Id : state.diets.sat.id,
      DietKcal: state.diets.sat.kcal,
      DietProtein: state.diets.sat.protein,
      DietFat: state.diets.sat.fat,
      DietCarbs: state.diets.sat.carbs,
    },
  ];
  const MealList = [
    [
      state.diets.mon.meals.breakfast,
      state.diets.mon.meals.lunch || null,
      state.diets.mon.meals.dinner || null,
    ],
    [
      state.diets.tue.meals.breakfast,
      state.diets.tue.meals.lunch || null,
      state.diets.tue.meals.dinner || null,
    ],
    [
      state.diets.wed.meals.breakfast,
      state.diets.wed.meals.lunch || null,
      state.diets.wed.meals.dinner || null,
    ],
    [
      state.diets.thu.meals.breakfast,
      state.diets.thu.meals.lunch || null,
      state.diets.thu.meals.dinner || null,
    ],
    [
      state.diets.fri.meals.breakfast,
      state.diets.fri.meals.lunch || null,
      state.diets.fri.meals.dinner || null,
    ],
    [
      state.diets.sat.meals.breakfast,
      state.diets.sat.meals.lunch || null,
      state.diets.sat.meals.dinner || null,
    ],
  ];

  return (
    <Wrapper>
      <DietUserBodyInfoCard id={state.id} diet_status={state.diet_status} min_nutrient={state.min_nutrient} max_nutrient={state.max_nutrient} />
      <DietCardList DietMealdata={DietMealdata} MealList={MealList} />
    </Wrapper>
  );
}

export default WeekDietOutputPage;