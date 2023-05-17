import { React} from "react";
import styled from "styled-components";
import RadioButton from "../ui/RadioButton";
import Button from "../ui/Button";

const Wrapper = styled.div`
    padding: 16px;
    widht: calc(100% - 32px);
    height: 100%;
    border: 1px solid;
    display: flex;
    flex-direction: column;
`;
const StyleCard = styled.div`
    padding: 16px;    
`;

const StyleRadioWrapper = styled.div`
    display: flex;
    background: #fff;
    align-items: center;
    
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
    // 오른쪽 정렬
    & > * {
        margin-left: auto;
    }
`;
function DietCustomInfoCard(props) {
    const { handleSubmit, setMealCount, setDietStatus } = props;
    const onChangeMealsCount = (e) => {
        setMealCount(e.target.value);
    };
    const onChangeDietStatus = (e) => {
        setDietStatus(e.target.value);
    };
    return (
        <Wrapper>
            <h1>식단정보</h1>
            <form onSubmit={handleSubmit}>
                <label>끼니</label>
                <StyleCard>
                    <StyleRadioWrapper>
                        {/* <RadioButton placeholder="1끼" id="meal_1" name="MealCount" value={1} onChange={onChangeMealsCount} disabled={true} /> */}
                        <RadioButton placeholder="2끼" id="meal_2" name="MealCount" value={2} onChange={onChangeMealsCount} />
                        <RadioButton placeholder="3끼" id="meal_3" name="MealCount" value={3} onChange={onChangeMealsCount} />
                    </StyleRadioWrapper>
                </StyleCard>
                <label>다이어트 여부</label>
                <StyleCard>
                    <StyleRadioWrapper>
                        <RadioButton placeholder="다이어트" id="diet" name="DietStatus" value={0} onChange={onChangeDietStatus} />
                        <RadioButton placeholder="유지" id="Maintenance"name="DietStatus" value={1} onChange={onChangeDietStatus} />
                        {/* <RadioButton placeholder="증량" id="up"name="DietStatus" value={2} onChange={onChangeDietStatus} /> */}
                    </StyleRadioWrapper>
                </StyleCard>
                    <Button title="finish" />
            </form>
        </Wrapper>
    )
}

export default DietCustomInfoCard;