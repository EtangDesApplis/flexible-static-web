FROM node:alpine3.12
# serve is used to serve static web
RUN npm install -g -y serve
#
WORKDIR /app
#
COPY build /app/build
#script to update URL of backend on the fly from ENV
COPY replaceURL.sh /app/replaceURL.sh
#
RUN echo "sh replaceURL.sh" > start.sh && \
    echo "serve -s build -l tcp://0.0.0.0:3000" >> start.sh
#
EXPOSE 3000
#
CMD ["sh", "start.sh"]