#!/bin/bash

IMAGE_NAME="simple-migration"

DATA_IN="data_in"
DATA_OUT="data_out"

DB_HOST="postgres"
DB_PORT="5432"
DB_USER="postgres"
DB_PASSWORD="postgres"
DB_DATABASE="postgres"

docker run -v $(pwd)/$DATA_IN:/data_in -v $(pwd)/$DATA_OUT:/data_out -e DB_HOST=$DB_HOST -e DB_PORT=$DB_PORT -e DB_USER=$DB_USER -e DB_PASSWORD=$DB_PASSWORD -e DB_DATABASE=$DB_DATABASE --name=$IMAGE_NAME --link=postgres $IMAGE_NAME
