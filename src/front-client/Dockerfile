FROM node:alpine3.12
#
WORKDIR /app
#copy sources
COPY public /app/public
COPY src /app/src
COPY package.json /app/package.json
#install react deps
RUN npm install -y create-react-app
#install dependencies
RUN npm install -y
# serve is used to serve static web
RUN npm install -g -y serve

# build static resource
#RUN npm run build
#clean up sources & free up temporary modules needed for compilation
#RUN rm -rf public src package.json package-lock.json node_modules

#script to update URL of backend on the fly from ENV
COPY updateURL.sh /app/updateURL.sh
#
EXPOSE 3000
#
RUN echo "sh updateURL.sh" > start.sh && \
    echo "npm run build" >> start.sh && \
    echo "rm -rf public src package.json package-lock.json node_modules" >> start.sh && \
    echo "serve -s build -l tcp://0.0.0.0:3000" >> start.sh
CMD ["sh", "start.sh"]