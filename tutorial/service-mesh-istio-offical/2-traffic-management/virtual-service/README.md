# Virtual Services

## Deploy Virutal Service
```bash
kubectl apply -f microservices/deploy/service-mesh-istio-official/traffic/destination-rule-all.yaml

kubectl apply -f microservices/deploy/service-mesh-istio-official/traffic/virtual-service.yaml

# check the Kiali UI
Kiali UI > Istio Config > Namespace: default > VirtualService > reviews-route

# only v1 and v2 are activated
Kiali UI > Graph
```

![Screenshot](/img/v1-v2.png)

## Update Virutal Service
```bash
# update routing
kubectl apply -f microservices/deploy/service-mesh-istio-official/traffic/virtual-service-update.yaml

```

![Screenshot](/img/v1-v2-v3.png)

## Personalization with Virtual Service
```bash
# update routing
kubectl apply -f microservices/deploy/service-mesh-istio-project/traffic/virtual-service-personalized.yaml
```
Login and check the review star color

![Screenshot](/img/personalization.png)
