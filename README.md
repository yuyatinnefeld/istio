# Istio Guide

## Start Minikube Cluster
```bash
minikube start --memory=8192 --cpus=4 --driver=hyperkit
```

## Deploy Microservices with version 1
```bash
# deploy services
kubectl apply -f microservices/deploy/v3

# verfiy the http results
kubectl port-forward svc/payment-service  8888
kubectl port-forward svc/review-service  9999
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