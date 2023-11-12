# Deploy Microservice from Istio Sample Project
```bash

# enable istio-injection
kubectl label namespace default istio-injection=enabled
kubectl get ns default --show-labels

# deploy microservices
kubectl apply -f ./istio-1.19.3/samples/bookinfo/platform/kube/bookinfo.yaml

# verify
kubectl get pods -n default
istioctl analyze
```