import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import axios from 'axios';

import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';
import { useNavigate } from 'react-router-dom';

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
  margin: 32px;
`;

const ProfilePage = () => {
  const navigate = useNavigate();
  const [data, setData] = useState([]); // 데이터 상태 추가
  const [weekdiets, setWeekdiets] = useState([]); // 식단 기록 상태 추가
  
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
        const responseData = response.data;

        // 데이터 상태 업데이트
        const updatedData = responseData.map((item) => ({
          name: item.created_at,
          Weight: item.weight,
        }));
        setData(updatedData);

        // 식단 기록 상태 업데이트
        const weekdiets = responseData.map((item) => ({
          id: item.id,
          title: item.title,
        }));
        setWeekdiets(weekdiets);
      } else {
        // If access token is not available, redirect to login
        alert('유효하지 않은 토큰입니다.');
        localStorage.removeItem('access_token');
        navigate('/login');
      }
    } catch (error) {
      console.error('Error fetching profile:', error);
      localStorage.removeItem('access_token');
      navigate('/login');
    }
  };

  useEffect(() => {
    fetchProfile();
  }, []);

  return (
    <Wrapper>
      {/* 그래프 */}
      <ChartWapper>
        <ChartTitle>몸무게 변화일지</ChartTitle>
        {data.length > 0 ? ( // 데이터가 있을 때에만 그래프 렌더링
          <LineChart width={500} height={300} data={data}>
            <Line type="monotone" dataKey="Weight" stroke="#8884d8" />
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
          </LineChart>
        ) : (
          <p>Loading...</p> // 데이터가 없을 때 로딩 메시지 렌더링
        )}
      </ChartWapper>

      {/* 이전식단 기록 */}
      <ChartWapper>
        <h1>식단 기록</h1>
        <WeekDietLogList weekdiets={weekdiets} />
      </ChartWapper>
    </Wrapper>
  );
};

export default ProfilePage;
