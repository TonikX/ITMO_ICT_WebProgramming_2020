FROM node:12

WORKDIR /library-client

COPY package*.json ./

RUN npm install --silent

CMD ["npm", "start"]

COPY . .
