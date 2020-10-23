#!/bin/bash
if [ "$#" -eq 1 ]
then
  tag=$1
else
  tag="latest"
fi
echo "Building version: "$tag
#build back
cd src/back
docker build -t etangdesapplis/demo-site-back:$tag .
docker push etangdesapplis/demo-site-back:$tag
#build admin
cd ../front-admin
docker build -t etangdesapplis/demo-site-front-admin:$tag .
docker push etangdesapplis/demo-site-front-admin:$tag
#build client
cd ../front-client
docker build -t etangdesapplis/demo-site-front-client:$tag .
docker push etangdesapplis/demo-site-front-client:$tag
#clean up
yes|docker system prune -a
