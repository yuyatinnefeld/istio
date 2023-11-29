# Push Docker image into Docker Repo

`microservices/app`

# Deploy microservices 

`microservices/deploy`

# Deploy Ingress
```bash
# enable minikube ingress controller to use ./deploy/ingress.yaml
minikube addons enable ingress

# verify the ingress controller
kubectl get pods -n ingress-nginx | grep ingress-nginx-controller

# deploy ingress rules
kubectl apply -f microservices/deploy/ingress.yaml

# wait and verify the ingress received the cluster IP
kubectl get ingress --watch

# update DNS for Local Domain Access
echo -e "$(minikube ip)\testing-yuya.com" | sudo tee -a /etc/hosts

curl -X GET 'http://testing-yuya.com/review' -H 'Content-Type: application/json'
curl -X GET 'http://testing-yuya.com/payment' -H 'Content-Type: application/json'
curl  'http://testing-yuya.com'
```