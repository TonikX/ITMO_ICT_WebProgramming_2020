FROM node:12

WORKDIR /client

COPY package*.json ./

RUN npm install --silent

CMD ["npm", "start"]

COPY . .