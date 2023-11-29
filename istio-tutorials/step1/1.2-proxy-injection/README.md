# Deploy microservices with Proxy Injection

## Clean Up (If the Microservices running)
```bash
# recreate services
kubectl delete -f microservices/deploy/no-service-mesh/v3

# delete if you are using ingress rule
kubectl delete -f microservices/deploy/ingress.yaml

# delete ingress controller
minikube addons disable ingress

```

## Install Istio CTL
```bash
curl -L https://istio.io/downloadIstio | sh -
```

## Setup Istio
```bash
# check the Istio ctl version
ls | grep istio
ISTIO_VERSION=istio-1.19.3

# setup working directory path
export PATH="$PATH:$(pwd)/$ISTIO_VERSION/bin"

# verify istio ctl
istioctl version

# check the side-car proxy
istioctl analyze

# enable istio-injection
kubectl label namespace default istio-injection=enabled
kubectl get ns default --show-labels
kubectl get namespace -L istio-injection
```

## create a profile
```bash
# Install istio
istioctl install --set profile=demo -y
istioctl verify-install

# Verify all components
kubectl get all -n istio-system
```

## Restart Microservices
```bash
# redeploy
kubectl apply -f microservices/deploy/service-mesh

# check the side-car proxy
istioctl analyze

# check every pod has a sidecar proxy (envoy)
kubectl get pod
```

## Check the Frontend App
```bash
kubectl port-forward svc/frontend-service  5000
```