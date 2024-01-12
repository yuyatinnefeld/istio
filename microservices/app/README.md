# Push Docker image into Docker Repo

## Payment App
```bash
cd microservices/app/payment

REPO_NAME=yuyatinnefeld
IMAGE_NAME=microservice-payment-app:1.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker run -p 8888:8888 -t $REPO_NAME/$IMAGE_NAME
docker image push $REPO_NAME/$IMAGE_NAME

# update the version num of application and create version 2
IMAGE_NAME=microservice-payment-app:2.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker image push $REPO_NAME/$IMAGE_NAME

# update the version num of application and create version 3
IMAGE_NAME=microservice-payment-app:3.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker image push $REPO_NAME/$IMAGE_NAME
```

## Reviews App
```bash
cd microservices/app/reviews

REPO_NAME=yuyatinnefeld
IMAGE_NAME=microservice-reviews-app:1.0.0
docker build -t $REPO_NAME/$IMAGE_NAME .
docker run -p 9999:9999 -t $REPO_NAME/$IMAGE_NAME
docker image push $REPO_NAME/$IMAGE_NAME
```

## Details App
```bash
cd microservices/app/details

REPO_NAME="yuyatinnefeld"
IMAGE_NAME="microservice-details-app:1.0.0"
docker build -t $REPO_NAME/$IMAGE_NAME .
docker run -it -p 7777:7777 $REPO_NAME/$IMAGE_NAME
docker image push $REPO_NAME/$IMAGE_NAME
```

## Frontend App
```bash
cd microservices/app/frontend

REPO_NAME="yuyatinnefeld"
IMAGE_NAME="microservice-frontend-app:1.0.0"
docker build -t $REPO_NAME/$IMAGE_NAME .
docker run -it -p 5000:5000 $REPO_NAME/$IMAGE_NAME
docker image push $REPO_NAME/$IMAGE_NAME
```
