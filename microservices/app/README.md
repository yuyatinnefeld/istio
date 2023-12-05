# Push Docker image into Docker Repo

## Build Payment App Image
```bash
cd microservices/app/payment

REPO_NAME=yuyatinnefeld
IMAGE_NAME=golang-payment-app:1.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker run -p 8888:8888 -t $REPO_NAME/$IMAGE_NAME
docker image push $REPO_NAME/$IMAGE_NAME

# create version 2
IMAGE_NAME=golang-payment-app:2.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker image push $REPO_NAME/$IMAGE_NAME

# create version 3
IMAGE_NAME=golang-payment-app:3.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker image push $REPO_NAME/$IMAGE_NAME
```

## Build Review App Image
```bash
cd microservices/app/review

REPO_NAME=yuyatinnefeld
IMAGE_NAME=golang-review-app:1.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker run -p 9999:9999 -t $REPO_NAME/$IMAGE_NAME
docker image push $REPO_NAME/$IMAGE_NAME
```


## Build Details App Image
```bash
cd microservices/app/details

REPO_NAME="yuyatinnefeld"
IMAGE_NAME="java-details-app:1.0.0"
docker build -t $REPO_NAME/$IMAGE_NAME .
docker run -it -p 8080:8080 $REPO_NAME/$IMAGE_NAME
docker image push $REPO_NAME/$IMAGE_NAME
```


## Build Frontend App Image
```bash
cd microservices/app/frontend

REPO_NAME="yuyatinnefeld"
IMAGE_NAME="python-frontend-app:3.0.0"
docker build -t $REPO_NAME/$IMAGE_NAME .
docker run -it -p 5000:5000 $REPO_NAME/$IMAGE_NAME
docker image push $REPO_NAME/$IMAGE_NAME
```
