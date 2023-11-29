# Istio Guide

## Start Minikube Cluster
```bash
minikube start --memory=8192 --cpus=4 --driver=hyperkit
```

## Deploy Microservices
- 1 x Frontend App (Python Flask)
- 1 x Review Backend App (Golang)
- 1 x Payment Backend App (Golang)

```bash
# deploy microservices with version 1
kubectl apply -f microservices/deploy/v1

# verfiy the services with v1
kubectl port-forward svc/frontend-service  5000

# update the services with v3
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