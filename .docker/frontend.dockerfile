FROM node:18-alpine

WORKDIR /code

COPY package.json .
COPY yarn.lock .
RUN yarn --frozen-lockfile

CMD ["yarn", "dev"]
