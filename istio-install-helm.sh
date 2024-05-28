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
    echo "create namespace $NS..."
    kubectl create namespace $NS

    echo "############## INSTALL ISTIO BASE CHART ##############"
    helm install istio-base istio/base -n $NS --set defaultRevision=default
    helm ls -n $NS

    echo "############## INSTALL ISTIOD CHART ##############"
    helm install istiod istio/istiod -n $NS --wait
    helm ls -n $NS
    kubectl get deployments -n $NS --output wide

    echo "############## INSTALL ISTIO INGRESS CHART ##############"
    kubectl create namespace istio-ingress
    helm install istio-ingressgateway istio/gateway -n $NS --wait
    
    echo "############## ISTIO INJECTION ENABLED ##############"
    kubectl label namespace default istio-injection=enabled
    kubectl get namespace -L istio-injection

    echo "############## DONE ! ##############"

}

# 1. Check if Minikube IP is available
if ! istioctl version >/dev/null 2>&1; then
    install_helm_istio
else
    echo "Istio alredy installed"
fi
