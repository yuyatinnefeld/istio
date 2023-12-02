# Learning Istio

## 01 Start Minikube Cluster
```bash
minikube start --memory=8192 --cpus=4 --driver=hyperkit
```

## 02 Deploy Microservices without Service Mesh
Comparing original kubernetes manifests with service mesh-adjusted manifests

`./microservice/deploy/no-service-mesh`

## 03 Deploy Microservices with Service Mesh
`./microservice/deploy/service-mesh`

## 04 Istio Tutorials
`./istio-tutorials`

- Install & Setup
- Kiali Dashboard
- Traffic Management
- Security
- Observability