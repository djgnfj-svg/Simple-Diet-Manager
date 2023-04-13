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
    border: 1px solid red;
`;

function WeekDietOutputPage(props) {
  const location = useLocation();
  const { state } = location;
  const DietMealdata = [
    {
      DietKcal: state.diets.mon.diet_kcal,
      DietProtein: state.diets.mon.diet_protein,
      DietFat: state.diets.mon.diet_fat,
      DietCarbs: state.diets.mon.diet_carbs,
    },
    {
      DietKcal: state.diets.tue.diet_kcal,
      DietProtein: state.diets.tue.diet_protein,
      DietFat: state.diets.tue.diet_fat,
      DietCarbs: state.diets.tue.diet_carbs,
    },
    {
      DietKcal: state.diets.wed.diet_kcal,
      DietProtein: state.diets.wed.diet_protein,
      DietFat: state.diets.wed.diet_fat,
      DietCarbs: state.diets.wed.diet_carbs,
    },
    {
      DietKcal: state.diets.thu.diet_kcal,
      DietProtein: state.diets.thu.diet_protein,
      DietFat: state.diets.thu.diet_fat,
      DietCarbs: state.diets.thu.diet_carbs,
    },
    {
      DietKcal: state.diets.fri.diet_kcal,
      DietProtein: state.diets.fri.diet_protein,
      DietFat: state.diets.fri.diet_fat,
      DietCarbs: state.diets.fri.diet_carbs,
    },
    {
      DietKcal: state.diets.sat.diet_kcal,
      DietProtein: state.diets.sat.diet_protein,
      DietFat: state.diets.sat.diet_fat,
      DietCarbs: state.diets.sat.diet_carbs,
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
  console.log(MealList);

  return (
    <Wrapper>
      <DietUserBodyInfoCard diet_status={state.diet_status} min_nutrient={state.min_nutrient} max_nutrient={state.max_nutrient} />
      <DietCardList DietMealdata={DietMealdata} MealList={MealList} />
    </Wrapper>
  );
}

export default WeekDietOutputPage;