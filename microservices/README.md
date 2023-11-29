# Deploy Microservices

## Application Overview
- 1 x Frontend App (Python Flask)
- 1 x Review Backend App (Golang)
- 1 x Payment Backend App (Golang)

## Quick Test
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

## Push Docker image into Docker Repo

`microservices/app`

## Deploy microservices 

`microservices/deploy`

## Deploy Kubernetes Ingress Controller (Nginx) & Ingress rules

`microservices/k8s-ingress`