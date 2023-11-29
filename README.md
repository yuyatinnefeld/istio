# Istio Guide

## Start Minikube Cluster
```bash
minikube start --memory=8192 --cpus=4 --driver=hyperkit
```

## Deploy Microservices
```bash
# deploy services with version 1
kubectl apply -f microservices/deploy/v1

# verfiy the backend apis with v1
kubectl port-forward svc/payment-service  8888
kubectl port-forward svc/review-service  9999
kubectl port-forward svc/frontend-service  5000

# update the backend apis with v3
kubectl delete -f microservices/deploy/v1
kubectl apply -f microservices/deploy/v3
kubectl port-forward svc/frontend-service  5000
```

## Step 1 - Initial Setup
`./step1`
- install Istio CTL
- install Istio

## Step 2 - Kiali
`./step2`

## Step 3 - Traffic Management
`./step3`
- gateway
- virtual services
- destination rules

## Step 4 - Security
`./step4`

## Step 5 - Observability
`./step5`