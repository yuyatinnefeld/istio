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

## Check the deployed web application
```bash
kubectl get svc -A
kubectl port-forward svc/productpage 9080
open http://127.0.0.1/
```
