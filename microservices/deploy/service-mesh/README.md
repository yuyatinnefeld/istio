# Deploy Microservices with Service Mesh

## Application Overview
- 1 x Frontend App (Python Flask)
- 1 x Review Backend App (Golang) with v1, v2, v3
- 1 x Payment Backend App (Golang) with v1, v2, v3

## Setup Istio
```bash
# my isto-ctl version
ISTIO_VERSION=$(ls | grep istio-1)
echo $ISTIO_VERSION

# setup working directory path
export PATH="$PATH:$(pwd)/$ISTIO_VERSION/bin"

# verify
istioctl version

# install istio profile
istioctl install --set profile=demo -y
istioctl verify-install

# verify all components
kubectl get all -n istio-system
```

## Deploy Microservices
```bash
# enable istio-injection
kubectl label namespace default istio-injection=enabled
kubectl get ns default --show-labels
kubectl get namespace -L istio-injection

# deploy microservices
kubectl apply -f microservices/deploy/service-mesh/apps

# check the side-car proxy
istioctl analyze

# check every pod has a sidecar proxy (envoy)
kubectl get pod

# verify frotnend
kubectl port-forward svc/frontend-service  5000
```