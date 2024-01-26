#!/bin/bash
#
# Author Yuya Tinnefeld
#

deploy_istio_ingress() {
    echo "############## DEPLOY ISTIO INGRESS ##############"
    kubectl apply -f istio/traffic-management/istio-ingress.yaml
}

deploy_istio_gateway() {
    echo "############## DEPLOY ISTIO GATEWAY ##############"
    kubectl apply -f istio/traffic-management/istio-gateway.yaml
}

deploy_virtual_service() {
    echo "############## DEPLOY ISTIO VIRTUAL SERVICE ##############"
    kubectl apply -f istio/traffic-management/virtual-service.yaml
}

deploy_destination_rules() {
    echo "############## DEPLOY ISTIO VIRTUAL SERVICE ##############"
    kubectl apply -f istio/traffic-management/destination-rules.yaml
}

# Deploy Ingress
deploy_istio_ingress

# Deploy gateway
deploy_istio_gateway

# Deploy virtual service
deploy_virtual_service

# Deploy destination rules
deploy_destination_rules
