import React from "react";
import {useNavigate} from "react-router-dom";
import styled from "styled-components";
import UserInputCard from "../card/UserInputCard";

const Wrapper = styled.div`
    padding: 16px;
    widht: calc(100% - 32px);
    height: 100%;
    max-height: 720px;
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
    max-height: 420px;
    border: 1px solid red;

    & > * {
        :not(:last-child) {
            margin-bottom: 16px;
        }
    }
`;

function UserInputpage(props) {
    const {} = props;

    const navigate = useNavigate();

    return (
        <Wrapper>
            <Container>
                <UserInputCard />
            </Container>
        </Wrapper>
    );
}

export default UserInputpage;