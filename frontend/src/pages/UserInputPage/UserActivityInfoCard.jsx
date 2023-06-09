import React from "react";
import styled from "styled-components";
import RadioButton from "../../components/RadioButton/RadioButton";
import Button from "../../components/Button/Button";

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

function UserActivityInfoCard(props) {
    const { handleSubmit, setExciseActivity, setGeneralActivity } = props;

    const onChangeGeneralActivity = (e) => {
        setGeneralActivity(e.target.value);
    };
    const onChangeActivitynextSubmit = (e) => {
        setExciseActivity(e.target.value);
    };
    return (
        <Wrapper>
            <h1>활동정보</h1>
            <form onSubmit={handleSubmit}>
                <label>활동량</label>
                <StyleCard>
                    <StyleRadioWrapper>
                        <RadioButton id="low" placeholder="집이최고다" name="general_activity" value={1.2} onChange={onChangeGeneralActivity} />
                        <RadioButton id="medium" placeholder="평범하다" name="general_activity" value={1.4} onChange={onChangeGeneralActivity} />
                        <RadioButton id="high" placeholder="활동적이다" name="general_activity" value={1.6} onChange={onChangeGeneralActivity} />
                    </StyleRadioWrapper>
                </StyleCard>
                <label>운동량(주)</label>
                <StyleCard>
                    <StyleRadioWrapper>
                        <RadioButton id="0" placeholder="0회" name="excise_activity" value={0} onChange={onChangeActivitynextSubmit} />
                        <RadioButton id="3" placeholder="1~3회" name="excise_activity" value={0.1} onChange={onChangeActivitynextSubmit} />
                        <RadioButton id="6" placeholder="3~6회" name="excise_activity" value={0.2} onChange={onChangeActivitynextSubmit} />
                        <RadioButton id="7" placeholder="7+회" name="excise_activity" value={0.3} onChange={onChangeActivitynextSubmit} />
                    </StyleRadioWrapper>
                </StyleCard>
                    <Button title="식단정보" />
            </form>
        </Wrapper>
    );
}

export default UserActivityInfoCard;