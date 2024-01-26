cd istio/security/certs/

# Generate a Private Key, CSR, Certificate
make -f Makefile.selfsigned.mk root-ca
```

#### Generate Immediate Certificate and Key
```bash
make -f  Makefile.selfsigned.mk localcluster-cacerts
```

#### Clean Up Istio Env
```bash
# Clean Up
kubectl delete namespace istio-system
kubectl delete -f microservices/deploy/service-mesh/apps
```


#### Create A Secret Cacerts
```bash

# Create Namespace
kubectl create namespace istio-system

# Setup Certificate in Istio 
cd istio/security/certs/

kubectl create secret generic cacerts -n istio-system \
      --from-file=localcluster/ca-cert.pem \
      --from-file=localcluster/ca-key.pem \
      --from-file=localcluster/root-cert.pem \
      --from-file=localcluster/cert-chain.pem

# Verify
kubectl get secret -n istio-system cacerts -o yaml

# Reinstall Istio
bash ./istio-install.sh

# Deploy Microservices
kubectl apply -f microservices/deploy/service-mesh/apps
```

##### !Important: Troubleshooting Istio Installation
I faced issues a few times while trying to install the Istio profile using `istioctl install --set profile=demo -y` but Istio’s CA cannot read certificates and key from the secret-mount files. It proved helpful to inspect the logs of the `istiod` pod for troubleshooting.

```bash
kubectl get pod -n istio-system | grep istiod
kubectl logs -n istio-system istiod-xxx-xxx -c discovery
```

### Configuring Istio Basic Virtual Services
```bash
bash ./istio-setup.sh

# verify
export INGRESS_HOST=$(minikube ip)

export INGRESS_PORT=$(kubectl -n istio-system get svc istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')

echo http://$INGRESS_HOST:$INGRESS_PORT/
```

### Deploy Deny Authz Rules
```bash
kubectl apply -f istio/security/authz-allow-noting.yaml

curl http://$INGRESS_HOST:$INGRESS_PORT/

kubectl apply -f istio/security/authz-allow-frontend.yaml
kubectl apply -f istio/security/authz-allow-reviews.yaml

curl http://$INGRESS_HOST:$INGRESS_PORT/
```

### Setup local DSN
```bash
sudo vi /etc/hosts

curl http://microservices-yuya.com:$INGRESS_PORT/
```

### Check Certificate
now we will check if the workloads are signed with the exact same certificate

```bash
# List Frotnend Pods

kubectl get pod -l app=frontend-app

# Exec into the pod of the first service
kubectl exec -it frontend-app-deploy-74c9d5c6c7-q9x8v -- /bin/bash

# Inside the pod, use Python
import requests
x = requests.get('http://reviews-service:9999')
print(x.status_code)

# Check Connection
kubectl exec -it frontend-app-deploy-74c9d5c6c7-q9x8v -c istio-proxy -- openssl s_client -showcerts --connect reviews-service:9999
```