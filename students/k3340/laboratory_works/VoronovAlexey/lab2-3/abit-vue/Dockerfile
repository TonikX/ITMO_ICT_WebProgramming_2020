FROM node:12

WORKDIR /abit-vue

COPY package*.json ./
RUN npm install --silent
CMD ["npm", "start"]

COPY . .
