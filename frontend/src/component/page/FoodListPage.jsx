import React, { useState, useEffect } from "react";
import styled from "styled-components";
import axios from "axios";

const FoodCard = ({ img, name, carbs, protein, fat, calories }) => {
  return (
    <Card>
      <FoodImage src={img} alt={img} />
      <h3>{name}</h3>
      <p>탄수화물 : {carbs}g</p>
      <p>단백질 : {protein}g</p>
      <p>지방 : {fat}g</p>
      <p>칼로리 : {calories}kcal</p>
    </Card>
  );
};

const FoodListPage = () => {
  const [search, setSearch] = useState("");
  const [foods, setFoods] = useState([]);

  const fetchFoods = async (searchQuery) => {
    try {
      const response = await axios.get(
        `${process.env.REACT_APP_API}/api/foods/?search=${searchQuery}`
      );
      setFoods(response.data.results);
    } catch (error) {
      console.error("Error fetching foods:", error);
    }
  };

  useEffect(() => {
    fetchFoods("");
  }, []);

  const handleChange = (e) => {
    setSearch(e.target.value);
  };

  const handleSubmit = () => {
    fetchFoods(search);
  };

  return (
    <Container>
      <SearchContainer>
        <SearchBar
          type="text"
          placeholder="Search for food..."
          value={search}
          onChange={handleChange}
        />
        <ConfirmButton onClick={handleSubmit}>확인</ConfirmButton>
      </SearchContainer>
      <Cards>
        {foods.map((food, index) => (
          <FoodCard
            key={index}
            img={food.image}
            name={food.name}
            carbs={food.carbs}
            protein={food.protein}
            fat={food.fat}
            calories={food.carbs}
          />
        ))}
      </Cards>
    </Container>
  );
};

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px;
`;

const SearchContainer = styled.div`
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
`;

const SearchBar = styled.input`
  width: 100%;
  max-width: 500px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
`;

const ConfirmButton = styled.button`
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  border-radius: 4px;
  cursor: pointer;

  &:hover {
    background-color: #0056b3;
  }
`;

const Cards = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
`;

const Card = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid;
  border-radius: 4px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const FoodImage = styled.img`
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 50%;
  margin-bottom: 10px;
`;

export default FoodListPage;
