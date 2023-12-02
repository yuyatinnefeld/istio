# Kubernetes Ingress Controller

```bash
# enable minikube ingress controller to use ./k8s-ingress/ingress.yaml
minikube addons enable ingress

# verify the ingress controller
kubectl get pods -n ingress-nginx | grep ingress-nginx-controller

# deploy ingress rules
kubectl apply -f microservices/k8s-ingress/ingress.yaml

# wait and verify the ingress received the cluster IP
kubectl get ingress --watch

# update DNS for Local Domain Access
echo -e "$(minikube ip)\testing-yuya.com" | sudo tee -a /etc/hosts

curl -X GET 'http://testing-yuya.com/review' -H 'Content-Type: application/json'
curl -X GET 'http://testing-yuya.com/payment' -H 'Content-Type: application/json'
curl  'http://testing-yuya.com'
```