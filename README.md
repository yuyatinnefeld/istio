# Istio Guide

## Start Minikube Cluster
```bash
minikube start --memory=8192 --cpus=4 --driver=hyperkit
```

## Deploy Microservices
```bash
# verify version 1
kubectl apply -f microservices/deploy/deploy-v1.yaml

# verify version 2
kubectl apply -f microservices/deploy/deploy-v2.yaml

# verify version 3
kubectl apply -f microservices/deploy/deploy-v3.yaml

# verfiy the http results
kubectl port-forward svc/http-golang-service 8888
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