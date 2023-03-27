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
    const { handleSubmit, handleBackSubmit, setMealsCount } = props;
    const onChangeMealsCount = (e) => {
        setMealsCount(e.target.value);
    };
    return (
        <Wrapper>
            <form onSubmit={handleSubmit}>
                <label>활동량</label>
                <StyleCard>
                    <StyleRadioWrapper>
                        <RadioButton placeholder="1끼" name="DietCustom" value={1.2} onChange={onChangeMealsCount} />
                        <RadioButton placeholder="2끼" name="DietCustom" value={1.4} onChange={onChangeMealsCount} />
                        <RadioButton placeholder="3끼" name="DietCustom" value={1.6} onChange={onChangeMealsCount} />
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