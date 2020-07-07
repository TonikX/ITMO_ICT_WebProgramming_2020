FROM node:12

WORKDIR /hotel-vue

COPY package*.json ./

RUN npm install --silent

COPY . .

RUN npm run build
