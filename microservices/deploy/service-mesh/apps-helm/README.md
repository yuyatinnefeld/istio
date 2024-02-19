# Install Helm Chart

```bash
# install dev app
helm install microservices-release-dev apps-helm/ --values apps-helm/values-dev.yaml -f apps-helm/values-dev.yaml --namespace dev

# install prod app
helm install microservices-release-dev apps-helm/ --values apps-helm/values.yaml -f apps-helm/values-prod.yaml --namespace prod

# install default app
helm install microservices-release-dev apps-helm/ --values apps-helm/values.yaml --namespace default

```