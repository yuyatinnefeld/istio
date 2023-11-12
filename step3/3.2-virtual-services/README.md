# Virtual Services

## Deploy Virutal Service
```bash
kubectl apply -f istio-1.19.3/samples/bookinfo/networking/destination-rule-all.yaml

kubectl apply -f step3/3.2-virtual-services/virtual-service.yml

# check the Kiali UI
Kiali UI > Istio Config > Namespace: default > VirtualService > reviews-route

# only v1 and v2 are activated
Kiali UI > Graph
```

![Screenshot](/img/v1-v2.png)

## Update Virutal Service
```bash
# update routing
kubectl apply -f step3/3.2-virtual-services/virtual-service-update.yml

```

![Screenshot](/img/v1-v2-v3.png)

## Personalization with Virtual Service
```bash
# update routing
kubectl apply -f step3/3.2-virtual-services/virtual-service-personal.yml
```
Login and check the review star color

![Screenshot](/img/personalization.png)
