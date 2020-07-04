FROM node:lts-alpine

WORKDIR /frontend

COPY package*.json ./
RUN npm install --silent
CMD npm start

COPY . .
