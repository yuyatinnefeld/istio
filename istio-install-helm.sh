#!/bin/bash
#
# Author Yuya Tinnefeld
#

install_helm_istio() {
    export NS="istio-system"

    echo "############## ADD HELM REPO ##############"
    helm repo add istio https://istio-release.storage.googleapis.com/charts
    helm repo update

    echo "############## INSTALL ISTIO WITH HELM ##############"
    echo "create namespace istio-system..."
    kubectl create namespace $NS

    echo "############## INSTALL ISTIO BASE CHART ##############"
    helm install istio-base istio/base -n $NS --set defaultRevision=default
    helm ls -n istio-system

    echo "############## INSTALL ISTIOD CHART ##############"
    helm install istiod istio/istiod -n istio-system --wait
    helm ls -n istio-system
    kubectl get deployments -n istio-system --output wide

    echo "############## INSTALL ISTIO INGRESS CHART ##############"
    kubectl create namespace istio-ingress
    helm install istio-ingress istio/gateway -n istio-ingress --wait
    
    echo "############## ISTIO INJECTION ENABLED ##############"
    kubectl label namespace default istio-injection=enabled
}

# 1. Check if Minikube IP is available
if ! istioctl version >/dev/null 2>&1; then
    install_helm_istio
else
    echo "Istio alredy installed"
fi