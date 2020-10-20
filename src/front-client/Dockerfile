FROM node:alpine3.12
#
RUN npm install -g -y serve
#
WORKDIR /app
COPY build /app/build
#
EXPOSE 3000
#
RUN echo "serve -s build -l tcp://0.0.0.0:3000" > start.sh
CMD ["sh", "start.sh"]