import React from "react";
import styled from "styled-components";
import Input from "../../components/Input/Input";
import Button from "../../components/Button/Button";
import RadioButton from "../../components/RadioButton/RadioButton";

const Wrapper = styled.div`
    padding: 16px;
    widht: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    background: #fff;
`;

const Card = styled.div`
    padding: 8px;
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
const StyleRadioWrapper = styled.div`
    display: flex;
    background: #fff;
    align-items: center;
    
    border-radius: 5px;
    padding: 20px 15px;
    box-shadow: 5px 5px 30px rgba(0,0,0,0.2);
`;

function UserBodyInfoCard(props) {
    const { handleSubmit, setAge, setHeight, setWeight, setGender } = props;

    const onChangeAge = (e) => {
        setAge(e.target.value);
    };

    const onChangeHeight = (e) => {
        setHeight(e.target.value);
    };

    const onChangeWeight = (e) => {
        setWeight(e.target.value);
    };

    const handleGender = (e) => {
        setGender(e.target.value);
    };

    return (
        <Wrapper>
            <h1>신체정보</h1>
            <form onSubmit={handleSubmit}>
                <Card>
                    <Input
                        type="text"
                        placeholder="나이(만)"
                        onChange={onChangeAge}
                    />
                </Card>
                <Card>
                    <Input
                        type="text"
                        placeholder="키(단위:cm)"
                        onChange={onChangeHeight}
                    />
                </Card>
                <Card>
                    <Input
                        type="text"
                        placeholder="몸무게(단위:kg)"
                        onChange={onChangeWeight} 
                    />
                </Card>
                <Card>
                    <StyleRadioWrapper>
                        <RadioButton id="M" placeholder="남자" name="gender" value="M" onChange={handleGender}/>
                        <RadioButton id="G" placeholder="여자" name="gender" value="W" onChange={handleGender}/>
                    </StyleRadioWrapper>
                </Card>
                <Button title="활동정보" />
            </form>
        </Wrapper>
    );
}

export default UserBodyInfoCard;