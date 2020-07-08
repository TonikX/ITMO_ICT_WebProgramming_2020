FROM node:12

WORKDIR /hotel-frontend

COPY package*.json ./

RUN npm install --silent

CMD ["npm", "start"]

COPY . .
