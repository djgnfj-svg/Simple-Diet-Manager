import React from "react";
import styled from "styled-components";
import axios from "axios";
import { useNavigate } from 'react-router';
import UserBodyInfoCard from "./UserBodyInfoCard";
import UserActivityInfoCard from "./UserActivityInfoCard";
import DietCustomInfoCard from "./DietCustomInfoCard";

const Wrapper = styled.div`
    padding: 16px;
    widht: 100%;
    height: 100%;
    border: 1px solid blue;
    display: flex;
    flex-direction: column;
`;

function UserInputCard(props) {
    const { } = props;
    const navigate = useNavigate();

    const [currentIndex, setCurrentIndex] = React.useState(0);
    //유저 정보
    const [age, setAge] = React.useState("");
    const [height, setHeight] = React.useState("");
    const [weight, setWeight] = React.useState("");
    const [gender, setGender] = React.useState("");
    const [generalActivity, setGeneralActivity] = React.useState("");
    const [exciseActivity, setExciseActivity] = React.useState("");

    //옵션값
    const [mealCount, setMealCount] = React.useState("");
    const [dietstatus, setDietStatus] = React.useState("");


    const handleSubmit = (e) => {
        e.preventDefault();
        if (age === "" || height === "" || weight === "" || gender === "") {
            alert("모든 항목을 입력해주세요.");
            return;
        }
        if (age < 0 || height < 0 || weight < 0) {
            alert("0보다 작은 수는 입력할 수 없습니다.");
            return;
        }
        if (age >100 || age < 20){
            alert("20세 이상, 100세 이하만 입력 가능합니다.");
            return;
        }
        if (height > 230 || height < 145){
            alert("145cm 이상, 230cm 이하만 입력 가능합니다.");
            return;
        }
        if (weight > 230 || weight < 50){
            alert("50kg 이상, 230kg 이하만 입력 가능합니다.");
            return;
        }

        setCurrentIndex(currentIndex + 1)
    };

    const handleActivitySubmit = (e) => {
        e.preventDefault();
        if (generalActivity === "" || exciseActivity === "") {
            alert("모든 항목을 입력해주세요.");
            return;
        }
        setCurrentIndex(currentIndex + 1)
    }

    const handleDietSubmit = (e) => {
        e.preventDefault();
        if (mealCount === "") {
            alert("모든 항목을 입력해주세요.");
            return;
        }
        const data = {
            age: age,
            height: height,
            weight: weight,
            gender: gender,
            general_activity: generalActivity,
            excise_activity: exciseActivity,
            meal_count: mealCount,
            diet_status : dietstatus
        }
        axios.post("http://localhost:8000/api/week-diets/", data)
            .then((res) => {
                alert("성공")
                navigate("/diets", { state: res.data });
        })
        .catch((err) => {
            alert(err)
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
                    setGeneralActivity={setGeneralActivity}
                />
                :
                <DietCustomInfoCard
                    handleSubmit={handleDietSubmit}
                    handleBackSubmit={handleBackSubmit}
                    setMealCount={setMealCount}
                    setDietStatus={setDietStatus}
                />
        }
    </Wrapper>
);
}

export default UserInputCard;