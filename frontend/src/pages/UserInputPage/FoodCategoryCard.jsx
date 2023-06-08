import React, { useState, useEffect } from "react";
import styled from "styled-components";
import axios from "axios";
import Checkbox from "../../components/Checkbox/Checkbox";
import Button from "../../components/Button/Button";

const Wrapper = styled.form`
    padding: 16px;
    widht: 100%;
    height: 100%;
    border: 1px solid blue;
    display: flex;
    flex-direction: column;
`;

const StyleRadioWrapper = styled.div`
    display: flex;
    background: #fff;
    align-items: center;
    
    border-radius: 5px;
    padding: 20px 15px;
    box-shadow: 5px 5px 30px rgba(0,0,0,0.2);
`;

function FoodCategoryCard(props) {
    const { handleSubmit } = props;
    const [Categorys, setCategorys] = useState([]);
    const [checkedValues, setCheckedValues] = useState([]);
    
    const fetchFoods = async (searchQuery) => {
        try {
            const response = await axios.get(
                `${process.env.REACT_APP_API}/api/food-category/`
            );
            setCategorys(response.data.results);
        } catch (error) {
            console.error("Error fetching foods:", error);
        }
    }
    useEffect(() => {
        fetchFoods("");
    }, []);

    return (
        <>
            <Wrapper onSubmit={handleSubmit} >
                <h1>3가지를 선택하세요</h1>
                <StyleRadioWrapper>
                    {Categorys.map((food, index) => (
                        <Checkbox
                            id={index}
                            key={index}
                            name="FoodCategory"
                            placeholder={food.name}
                            value={food.id}
                            onChange={(event) => {
                                const { checked, value } = event.target;
                                if (checked) {
                                    setCheckedValues((prevValues) => [...prevValues, value]);
                                } else {
                                    setCheckedValues((prevValues) =>
                                        prevValues.filter((val) => val !== value)
                                    );
                                }
                            }}
                        />
                    ))}
                </StyleRadioWrapper>
                    <Button title="마지막!" />
            </Wrapper>
        </>
    );
}

export default FoodCategoryCard;