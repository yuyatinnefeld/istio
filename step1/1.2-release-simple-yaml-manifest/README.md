# Deploy Microservice with Manifest
- Source: https://github.com/GoogleCloudPlatform/microservices-demo

```bash
# copy the kubernetes-manifest.yaml from github.com/GoogleCloudPlatform/microservices-demo/release

# deploy services
kubectl apply -f release/kubernetes-manifest.yaml

# wait until the all pods deployed 
kubectl get pod

# check the side-car proxy
istioctl analyze

# enable istio-injection
kubectl label namespace default istio-injection=enabled
kubectl get ns default --show-labels

# recreate services
kubectl delete -f release/kubernetes-manifest.yaml
kubectl apply -f release/kubernetes-manifest.yaml

# check the side-car proxy
istioctl analyze

# check every pod has a sidecar proxy (envoy)
kubectl get pod
```

## Check the deployed web application
```bash
kubectl port-forward svc/frontend 80
open http://127.0.0.1/
```