import React from "react";
import styled from "styled-components";
import UserInputCard from "../card/UserInputCard";

const Wrapper = styled.div`
    padding: 16px;
    widht: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 1px solid green;
`;

const Container = styled.div`
    width: 100%;
    max-width: 720px;
    height: 100%;
    border: 1px solid red;

    & > * {
        :not(:last-child) {
            margin-bottom: 16px;
        }
    }
`;

function UserInputpage(props) {
    const {} = props;

    return (
        <Wrapper>
            <h1>간단식단</h1>
            <h3 style={{color:"gray"}}>당신에게 맞는 식단을 구성해 보세요</h3>
            <Container>
                <UserInputCard />
            </Container>
        </Wrapper>
    );
}

export default UserInputpage;