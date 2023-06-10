import React, { useState } from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';
import styled from 'styled-components';

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const Button = styled.button`
  margin-top: 20px;
`;

const data = [
  { name: 'Jan', Weight: 70 },
  { name: 'Feb', Weight: 72 },
  { name: 'Mar', Weight: 71 },
  { name: 'Apr', Weight: 70 },
  { name: 'May', Weight: 69 },
  { name: 'Jun', Weight: 68 },
];

const ProfilePage = () => {
  const [showChart, setShowChart] = useState(true);

  return (
    <Wrapper>
      {showChart && (
        <LineChart width={500} height={300} data={data}>
          <Line type="monotone" dataKey="Weight" stroke="#8884d8" />
          <CartesianGrid stroke="#ccc" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
        </LineChart>
      )}
      <Button onClick={() => setShowChart(!showChart)}>
        {showChart ? 'Hide Chart' : 'Show Chart'}
      </Button>
    </Wrapper>
  );
};

export default ProfilePage;
