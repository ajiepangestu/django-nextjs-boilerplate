FROM node:18-alpine

WORKDIR /code

COPY ./webapp/package.json .
COPY ./webapp/yarn.lock .
COPY .env .

RUN yarn --frozen-lockfile

CMD ["yarn", "dev"]
