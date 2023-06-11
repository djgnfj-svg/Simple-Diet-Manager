import React, { useEffect } from 'react';
import styled from 'styled-components';
import axios from 'axios';

import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';
import { useNavigate  } from 'react-router-dom';

import WeekDietLogList from '../../components/List/WeekDietLogList';

const Wrapper = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-top: 50px;
  padding: 16px;

    @media screen and (max-width: 768px) {
        flex-direction: column;
    }

`;

const ChartTitle = styled.h2`
  margin-bottom: 20px;
`;

const ChartWapper = styled.div`
    height: 500px;
    width: 500px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 32px
`;

const data = [
  { name: 'Jan', Weight: 70 },
  { name: 'Feb', Weight: 72 },
  { name: 'Mar', Weight: 71 },
  { name: 'Apr', Weight: 70 },
  { name: 'May', Weight: 69 },
  { name: 'Jun', Weight: 68 },
];

const data2 = [
    {title : "n월 주차 식단"},
    {title : "n월 주차 식단"},
    {title : "n월 주차 식단"},
];
const ProfilePage = () => {
  const navigate = useNavigate();
  const fetchProfile = async () => {
    try {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        const response = await axios.get(
          `${process.env.REACT_APP_API}/api/userprofile/`,
          {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          }
        );
        console.log(response.data);
         
        // Process the profile data
      } else {
        // If access token is not available, redirect to login
        alert("유효하지 않은 토큰입니다.")
        navigate('/login');
      }
    } catch (error) {
      console.error('Error fetching profile:', error);
      alert('');
      navigate('/login');
    }
  };
  useEffect(() => {
    fetchProfile();
  }, []);

  return (
    <Wrapper>
    <ChartWapper>
        <ChartTitle>몸무게 변화일지</ChartTitle>
        <LineChart width={500} height={300} data={data}>
            <Line type="monotone" dataKey="Weight" stroke="#8884d8" />
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
        </LineChart>
    </ChartWapper>
    <ChartWapper>
        <h1>식단 기록</h1>
        <WeekDietLogList weekdiets={data2}/>
    </ChartWapper>
    </Wrapper>
  );
};

export default ProfilePage;
