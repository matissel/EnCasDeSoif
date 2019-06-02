#!/bin/sh
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin &&\
docker build . -t loicrosso/en-cas-de-soif:latest &&\
docker push loicrosso/en-cas-de-soif:latest &&\
curl --request POST https://hooks.microbadger.com/images/loicrosso/en-cas-de-soif/$MICROBADGER_ID