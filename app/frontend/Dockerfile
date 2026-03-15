# Stage 1: kompiliert
FROM node:20 AS builder
WORKDIR /app
COPY . .
RUN npm install && npm run build 

# Stage 2: nur kopieren
FROM jonasal/nginx-certbot:latest
RUN mkdir -p /usr/share/nginx/html
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
