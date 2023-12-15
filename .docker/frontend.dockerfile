FROM node:18-alpine

WORKDIR /code

COPY . .
RUN yarn --frozen-lockfile

CMD ["yarn", "dev"]
