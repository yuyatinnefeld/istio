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