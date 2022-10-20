#!/bin/bash

IMAGE_NAME="simple-migration"
DB_USER="postgres"
DB_PASSWORD="postgres"

echo "Loading images..."
docker load < ./$IMAGE_NAME.tar.gz
docker load < ./postgres.tar.gz

echo "Starting postgresql..."
EXISTING_ID=$(docker ps -af "name=postgres" -q)
if [ ! -z "$EXISTING_ID" ]; then
  docker rm -f $EXISTING_ID
fi
docker run -p 5432:5432 -d --shm-size 2g -e PGDATA=/data/postgres -e POSTGRES_USER=$DB_USER -e POSTGRES_PASSWORD=$DB_PASSWORD --name=postgres postgres
sleep 30

echo "Setup complete"
