#!/bin/bash

IMAGE_NAME="simple-migration"

cd ../..
docker build -t $IMAGE_NAME -f ./utils/deployment/Dockerfile .

cd ./utils/deployment
docker save $IMAGE_NAME | gzip > ./$IMAGE_NAME.tar.gz

docker pull postgres
docker save postgres | gzip > ./postgres.tar.gz

zip ./$IMAGE_NAME.zip ./$IMAGE_NAME.tar.gz ./postgres.tar.gz ./setup.sh ./start.sh
