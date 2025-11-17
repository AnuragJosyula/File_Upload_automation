#!/usr/bin/env bash

set -e
IMAGE_NAME="file-scan-service:latest"
CONTAINER_NAME="file-scan-service"

docker-compose -f /path/to/your/docker-compose.deploy.yml pull || true
docker stop ${CONTAINER_NAME} || true
docker rm ${CONTAINER_NAME} || true
docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}