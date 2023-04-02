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
            <Container>
                <UserInputCard />
            </Container>
        </Wrapper>
    );
}

export default UserInputpage;