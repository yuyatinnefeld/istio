# Istio HelmCart

```bash
kubectl create namespace istio-system
```

## Install Istio-base
```bash
helm install istio-base helm/base -n istio-system --set defaultRevision=default
helm ls -n istio-system
```

## Install Istio Discovery
```bash
helm install istiod helm/istiod -n istio-system
helm ls -n istio-system
```

## Install Istio Egress
```bash
helm install istio-egress helm/istio-egress -n istio-system
helm ls -n istio-system
```

## Install Istio Ingress
```bash
helm install istio-ingress helm/istio-ingress -n istio-system
helm ls -n istio-system
```

## ArgoCD
```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
kubectl create namespace argocd
helm install argocd argo/argo-cd --namespace argocd

# username: admin | password:
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

kubectl port-forward svc/argocd-server -n argocd 8080:443

# create ns
kubectl create namespace istio-system

# deploy istio-base
kubectl apply -f argocd-app-istio-base.yaml

# deploy istiod
kubectl apply -f argocd-app-istiod.yaml

# deploy istio-ingress
kubectl apply -f argocd-app-istio-ingress.yaml
```