FROM node:latest

WORKDIR /app

COPY package.json /app
COPY package-lock.json /app
RUN npm install

COPY . /app

ENV NODE_OPTIONS=--openssl-legacy-provider

CMD ["npm", "start"]
