import React from "react";
import styled from "styled-components";
import axios from "axios";
import useNavigate from "react-router-dom";
import UserBodyInfoCard from "./UserBodyInfoCard";
import UserActivityInfoCard from "./UserActivityInfoCard";
import DietCustomInfoCard from "./DietCustomInfoCard";

const Wrapper = styled.div`
    padding: 16px;
    widht: calc(100% - 32px);
    height: 100%;
    border: 1px solid blue;
    display: flex;
    flex-direction: column;
`;

function UserInputCard(props) {
    const {} = props;
    const navigate = useNavigate();

    const [currentIndex, setCurrentIndex] = React.useState(0);

    const [age, setAge] = React.useState("");
    const [height, setHeight] = React.useState("");
    const [weight, setWeight] = React.useState("");
    const [gender, setGender] = React.useState("");
    const [generalActivities, setGeneralActivities] = React.useState("");
    const [exciseActivity, setExciseActivity] = React.useState("");

    const [mealsCount, setMealsCount] = React.useState("");

    const data = {
        age: age,
        height: height,
        weight: weight,
        gender : gender,
        general_activities: generalActivities,
        excise_activities: exciseActivity,
        meals_count: mealsCount
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        if (age === "" || height === "" || weight === "" || gender === "") {
            alert("모든 항목을 입력해주세요.");
            return;
        }
        setCurrentIndex(currentIndex + 1)
    };
    
    const handleActivitySubmit = (e) => {
        e.preventDefault();
        if (generalActivities === "" || exciseActivity === "") {
            alert("모든 항목을 입력해주세요.");
            return;
        }
        setCurrentIndex(currentIndex + 1)
    }

    const handleDietSubmit = (e) => {
        e.preventDefault();
        if (mealsCount === "") {
            alert("모든 항목을 입력해주세요.");
            return;
        }
        axios.post("http://localhost:8000/api/diet-custom/", {
            data : data})
            .then((res) => {
                navigate("/diet",res.data);
            })
            .catch((err) => {
                alert(err)
                navigate("/",);
            })
    }


    const handleBackSubmit = (e) => {
        e.preventDefault();
        setCurrentIndex(currentIndex - 1)
    }

        return (
        <Wrapper>
            {currentIndex === 0 
            ?
            <UserBodyInfoCard
                handleSubmit={handleSubmit}
                setAge={setAge}
                setHeight={setHeight}
                setWeight={setWeight}
                setGender={setGender}
            />
            :
            currentIndex === 1
                ?
                <UserActivityInfoCard
                    handleSubmit={handleActivitySubmit}
                    handleBackSubmit={handleBackSubmit}
                    setExciseActivity={setExciseActivity}
                    setGeneralActivities={setGeneralActivities}
                    />
                    :
                    <DietCustomInfoCard 
                    handleSubmit={handleDietSubmit}
                    setMealsCount={setMealsCount}
                    handleBackSubmit={handleBackSubmit}
                />
            }
        </Wrapper>
    );
}

export default UserInputCard;