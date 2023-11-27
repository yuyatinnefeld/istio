# Push Docker image into Docker Repo

## Check the app
```bash
cd microservices/app
REPO_NAME=yuyatinnefeld
IMAGE_NAME=golang-app:1.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker run -p 8888:8888 -t $REPO_NAME/$IMAGE_NAME
open http://localhost:8888
``````

## Push into the docker hub
```bash
docker image push $REPO_NAME/$IMAGE_NAME
``````

## Create 2 versions
```bash
vi main.go
IMAGE_NAME=golang-app:2.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker image push $REPO_NAME/$IMAGE_NAME

vi main.go
IMAGE_NAME=golang-app:3.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker image push $REPO_NAME/$IMAGE_NAME
```
