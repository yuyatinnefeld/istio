
# Istio Gateway
![Screenshot](/img/gateway.png)

## Access product page with Port-Forwarding

Here you can just forward and call the application
```bash
kubectl port-forward svc/productpage 9080
open http://127.0.0.1:9080/productpage
```

## Activate Ingress and Gateway
Traffic -> Gateway -> Ingress -> Application

```bash
# check svc
kubectl get svc -n istio-system | grep istio-ingressgateway

# deploy ingress
kubectl apply -f istio-1.19.3/samples/bookinfo/platform/kube/bookinfo-ingress.yaml

# verify
kubectl get ingress -A

# deploy gateway
kubectl apply -f step3/3.1-gateway/bookinfo-gateway.yaml

# verify
kubectl get gateway -A
```

# Access product page via Istio Gateway
```bash
export INGRESS_HOST=$(minikube ip)

export INGRESS_PORT=$(kubectl -n istio-system get svc istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')

echo http://$INGRESS_HOST:$INGRESS_PORT/productpage

curl http://$INGRESS_HOST:$INGRESS_PORT/productpage

# open the website
http://192.168.64.50:32074/productpage
```