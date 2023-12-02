# Deploy Microservices

## Application Overview
- 1 x Frontend App (Python Flask)
- 1 x Review Backend App (Golang) with v1, v2, v3
- 1 x Payment Backend App (Golang) with v1, v2, v3

## Quick Test
```bash
# deploy microservices with version 1
kubectl apply -f microservices/deploy/no-service-mesh/apps-v1

# verfiy the services with v1
kubectl port-forward svc/frontend-service  5000

# update the services with v3
kubectl delete -f microservices/deploy/no-service-mesh/apps-v1
kubectl apply -f microservices/deploy/no-service-mesh/apps-v3
kubectl port-forward svc/frontend-service  5000
```

## Deploy Kubernetes Ingress Controller (Nginx) & Ingress rules

`microservices/no-service-mesh/k8s-ingress`