# Stage 1: compile svelte -> build
FROM node:22 AS builder
WORKDIR /app
COPY . .
RUN npm install && npm run build 

# Stage 2: copy
FROM jonasal/nginx-certbot:latest
RUN mkdir -p /usr/share/nginx/html
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
