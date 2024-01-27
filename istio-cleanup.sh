#!/bin/bash
#
# Author Yuya Tinnefeld
#

delete_apps() {
    echo "############## DELETE MS APPLICATION ##############"
    kubectl delete -f microservices/deploy/service-mesh/apps
    kubectl delete -f microservices/deploy/service-mesh/sample
}

delete_istio_traffic_management() {
    echo "############## DEPLOY ISTIO INGRESS ##############"
    kubectl delete -f istio/traffic-management/istio-ingress.yaml
    kubectl delete -f istio/traffic-management/istio-gateway.yaml
    kubectl delete -f istio/traffic-management/virtual-service.yaml
    kubectl delete -f istio/traffic-management/destination-rules.yaml
}

uninstall_istio() {
    echo "############## UNINSTALL ISTIO ##############"
    istioctl uninstall --purge -y
}

delete_namespace() {
    echo "############## DELETE NAMESPACE ##############"
    kubectl delete ns foo istio-system
}

# Delete Applications
delete_apps

# Delete Istio Traffic Management Config
delete_istio_traffic_management

# Uninstall Istio
uninstall_istio

# Delete Namespace
delete_namespace



