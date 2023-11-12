# Istio Kiali
![Screenshot](/img/kiali-architecture.png)


## Run Kiali
```bash
# check the installation tools
ls ./istio-1.19.3/samples/addons

# deploy a monitoring tool (you need to install prometheus for kiali api backend)
kubectl apply -f ./istio-1.19.3/samples/addons/prometheus.yaml
kubectl get pod -n istio-system | grep prometheus
kubectl get svc -n istio-system  | grep prometheus

# check prometheus server
kubectl port-forward svc/prometheus -n istio-system 9090
open http://localhost:9090

# deploy an service mesh dashboard
kubectl apply -f istio-1.19.3/samples/addons/kiali.yaml

# verify
kubectl rollout status deployment/kiali -n istio-system
kubectl get svc -n istio-system | grep kiali

# start kiali
## option 1
istioctl dashboard kiali

## option 2
kubectl port-forward svc/kiali -n istio-system 20001
open http://localhost:20001
```

## Create Traffic
```bash
SERVICE_NAME="productpage"
kubectl get svc -n default | grep productpage
SERVICE_PORT="9080"

kubectl port-forward svc/$SERVICE_NAME $SERVICE_PORT

curl "http://127.0.0.1:$SERVICE_PORT/productpage"
```