# Deployment mongodb for dev
```
apiVersion: v1
kind: Service
metadata:
  name: mongodb
  labels:
    app: mongodb
spec:
  type: NodePort
  ports:
  - port: 27017
    nodePort: 32017
    targetPort: 27017
    protocol: TCP
    name: http
  selector:
    app: mongodb
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongodb
spec:
  selector:
    matchLabels:
      app: mongodb
  replicas: 1
  template:
    metadata:
      labels:
        app: mongodb
    spec:
      containers:
      - name: mongodb
        image: mongo:4.4.1
        ports:
        - containerPort: 27017
```
# Test with mongo shell
https://mkyong.com/mongodb/mongodb-hello-world-example/
Basic commands are
```
mongo --host myk3s.com --port 32017
show dbs
show collection
use mydb
db.getName()
db.mycollection.insert({user:"name"})
db.mycollection.find()
```
# Test with python
Reference: https://api.mongodb.com/python/current/tutorial.html
To update record: https://www.w3schools.com/python/python_mongodb_update.asp
```
python seedDB.py
```

# Advanced topics
Ref: https://hub.docker.com/_/mongo
Make persistent data
```
docker run --name some-mongo -v /my/own/datadir:/data/db -d mongo
```
Dump database
```
docker exec some-mongo sh -c 'exec mongodump -d <database_name> --archive' > /some/path/on/your/host/all-collections.archive
```