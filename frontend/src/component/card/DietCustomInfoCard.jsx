import React from "react";
import styled from "styled-components";
import RadioButton from "../ui/RadioButton";
import Button from "../ui/Button";

const Wrapper = styled.div`
    padding: 16px;
    widht: calc(100% - 32px);
    height: 100%;
    border: 1px solid blue;
    display: flex;
    flex-direction: column;
`;
const StyleCard = styled.div`
    padding: 16px;    
`;

const StyleRadioWrapper = styled.div`
    display: inline-flex;
    background: #fff;
    height: 100px;
    width: 400px;
    align-items: center;
    justify-content: space-evenly;
    border-radius: 5px;
    padding: 20px 15px;
    box-shadow: 5px 5px 30px rgba(0,0,0,0.2);
`;
const ButtonWrapper = styled.div`
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
`;
function DietCustomInfoCard(props) {
    const { handleSubmit, handleBackSubmit, setMealCount, setDietStatus } = props;
    const onChangeMealsCount = (e) => {
        setMealCount(e.target.value);
    };
    const onChangeDietStatus = (e) => {
        setDietStatus(e.target.value);
    };
    return (
        <Wrapper>
            <form onSubmit={handleSubmit}>
                <label>끼니</label>
                <StyleCard>
                    <StyleRadioWrapper>
                        <RadioButton placeholder="1끼" name="MealCount" value={1} onChange={onChangeMealsCount} />
                        <RadioButton placeholder="2끼" name="MealCount" value={2} onChange={onChangeMealsCount} />
                        <RadioButton placeholder="3끼" name="MealCount" value={3} onChange={onChangeMealsCount} />
                    </StyleRadioWrapper>
                </StyleCard>
                <label>다이어트 여부</label>
                <StyleCard>
                    <StyleRadioWrapper>
                        <RadioButton placeholder="다이어트" name="DietStatus" value={1} onChange={onChangeDietStatus} />
                        <RadioButton placeholder="유지" name="DietStatus" value={0} onChange={onChangeDietStatus} />
                    </StyleRadioWrapper>
                </StyleCard>
                <ButtonWrapper>
                    <Button title="<-" onClick={handleBackSubmit}/>
                    <Button title="->"/>
                </ButtonWrapper>
            </form>
        </Wrapper>
    )
}

export default DietCustomInfoCard;