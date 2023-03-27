import React from "react";
import styled from "styled-components";
import Input from "../ui/Input";
import Button from "../ui/Button";
import RadioButton from "../ui/RadioButton";

const Wrapper = styled.div`
    padding: 16px;
    widht: calc(100% - 32px);
    height: 100%;
    border: 1px solid blue;
    display: flex;
    flex-direction: column;
`;

const Card = styled.div`
    padding: 16px;    
`;

const ButtonWrapper = styled.div`
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
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
            <form onSubmit={handleSubmit}>
                <label>나이</label>
                <Card>
                    <Input
                        type="text"
                        placeholder="나이(단위:만)"
                        onChange={onChangeAge}
                    />
                </Card>
                <label>키</label>
                <Card>
                    <Input
                        type="text"
                        placeholder="키(단위:cm)"
                        onChange={onChangeHeight}
                    />
                </Card>
                <label>몸무게</label>
                <Card>
                    <Input
                        type="text"
                        placeholder="몸무게(단위:kg)"
                        onChange={onChangeWeight} 
                    />
                </Card>
                <label>성별</label>
                <Card>
                    <StyleRadioWrapper>
                        <RadioButton placeholder="남자" name="gender" value="M" onChange={handleGender}/>
                        <RadioButton placeholder="여자" name="gender" value="W" onChange={handleGender}/>
                    </StyleRadioWrapper>
                </Card>
                <ButtonWrapper>
                    <Button title="<-" />
                    <Button title="->" />
                </ButtonWrapper>
            </form>
        </Wrapper>
    );
}

export default UserBodyInfoCard;