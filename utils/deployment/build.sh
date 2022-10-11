#!/bin/bash

cd ../..
docker build -t simple-migration -f ./utils/deployment/Dockerfile .
docker save simple-migration | gzip > ./utils/deployment/simple-migration.tar.gz
