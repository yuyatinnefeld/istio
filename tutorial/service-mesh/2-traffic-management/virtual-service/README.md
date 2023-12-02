# Virutal Service and Destination Rule
Istio Virtual Services and Destination Rules are crucial components for traffic management within the Istio service mesh. They work together to define how incoming traffic is routed to specific versions of a service and how that traffic is handled by the service instances.

## Virtual Service
A Virtual Service acts as the traffic routing engine, defining rules that map incoming requests to specific destinations within the mesh. Think of it as a traffic cop directing vehicles to their designated destinations based on certain criteria.

## Destination Rule
A Destination Rule defines settings for how traffic is handled by the service instances after it has been routed by a Virtual Service. It essentially configures the "destination" side of the traffic flow.

## Setup

```bash
# deploy vitutal service
kubectl apply -f microservices/deploy/service-mesh/istio/traffic/virtual-service.yaml

# deploy destination rules
kubectl apply -f microservices/deploy/service-mesh/istio/traffic/destination-rules.yaml

# Verify that 80% of traffic is allocated to review v1 and 20% to review v3.
kubectl port-forward svc/frontend-service  5000

# change the virutal service
kubectl apply -f microservices/deploy/service-mesh/istio/traffic/virtual-service-update.yaml
```