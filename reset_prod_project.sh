#!/bin/sh

docker compose down
rm -Rf ./staticfiles
rm -Rf ./media
docker build -t django:latest .
docker compose up --detach