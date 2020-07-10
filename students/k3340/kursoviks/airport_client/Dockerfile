FROM node:12

WORKDIR /airport_client

COPY package*.json ./

RUN npm install --silent

CMD ["npm", "start"]

COPY . .
