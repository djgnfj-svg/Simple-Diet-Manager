import { React, useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import styled from "styled-components";
import axios from "axios";
import DietDetailCard from "../card/DietDetailCard";

const Wrapper = styled.div`
    padding: 16px;
    widht: calc(100% - 32px);
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    border: 1px solid red;
`;

function DietDetailPage() {
    const { id } = useParams();
    const [mealData, setMealData] = useState([]);
    useEffect(() => {
        axios.get(`http://localhost:8000/api/diets/${id}/`)
        .then(res => {
            const data = res.data;
            setMealData([data.meals]);
        })
        .catch(err => {
            console.log(err);
        })
    }, [id]);
    return (
        <>
        <h1>간단식단</h1>
        <Wrapper>
            {mealData.map((meals, index) => {
                return (
                    <>
                        <DietDetailCard meals={meals} />
                    </>
                )
            })}
        </Wrapper>
            </>
    );
}

export default DietDetailPage;