# Istio Gateway
![Screenshot](/img/istio-gateway.png)

## Access product page with Port-Forwarding

Here you can just forward and call the application
```bash
kubectl port-forward svc/frontend-service 5000
curl http://127.0.0.1:5000
```

## Activate Ingress and Gateway
Traffic -> Gateway -> Ingress -> Application

```bash
# check svc
kubectl get svc -n istio-system | grep istio-ingressgateway

# deploy ingress
kubectl apply -f microservices/deploy/service-mesh/istio/gateway/istio-ingress.yaml

# verify
kubectl get ingress -A

# deploy gateway
kubectl apply -f microservices/deploy/service-mesh/istio/gateway/istio-gateway.yaml

# verify
kubectl get gateway -A
```

# Access product page via Istio Gateway
```bash
export INGRESS_HOST=$(minikube ip)

export INGRESS_PORT=$(kubectl -n istio-system get svc istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')

echo http://$INGRESS_HOST:$INGRESS_PORT/

curl http://$INGRESS_HOST:$INGRESS_PORT/

# open the website (example)
http://192.168.64.50:32074

# update local DNS
echo -e "$(minikube ip)\ttesting-yuya.com" | sudo tee -a /etc/hosts

curl http://testing-yuya.com:32074 
```