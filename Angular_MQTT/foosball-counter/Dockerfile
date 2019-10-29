FROM node:10.16.3-alpine AS builder
COPY . ./foosball-counter
WORKDIR /foosball-counter
RUN npm i
RUN $(npm bin)/ng build --prod

FROM nginx:1.17.4-alpine
COPY --from=builder /foosball-counter/dist/foosball-counter/ /usr/share/nginx/html
