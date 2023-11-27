# Redeploy microservices


```bash
# check the side-car proxy
istioctl analyze

# enable istio-injection
kubectl label namespace default istio-injection=enabled
kubectl get ns default --show-labels

# recreate services
kubectl delete -f microservices/deploy/
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