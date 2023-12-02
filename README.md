# Learning Istio

This repository offers two pathways to Istio mastery. Dive into my personal microservice project (`./tutorial/service-mesh`) or explore the official Istio microservice project (`./tutorial/service-mesh-istio-offical`).


## 01 Start Minikube Cluster
```bash
minikube start --memory=8192 --cpus=4 --driver=hyperkit
```

## 02 Deploy Microservices without Service Mesh
Comparing original kubernetes manifests with service mesh-adjusted manifests

`./microservice/deploy/no-service-mesh`

## 03 Deploy Microservices with Service Mesh
`./microservice/deploy/service-mesh`
- Install & Setup Istio

## 04 Istio Tutorials
`./tutorials`
- Kiali Dashboard
- Traffic Management
- Security
- Observability