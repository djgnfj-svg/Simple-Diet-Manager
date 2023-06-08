# pull official base image
FROM node:15.8.0-alpine

# set work directory
WORKDIR /app

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm ci --silent

# add app
COPY . ./

# start app
CMD ["npm", "start"]