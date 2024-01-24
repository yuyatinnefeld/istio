#!/bin/bash
#
# Author Yuya Tinnefeld
#

# Function to start Minikube cluster
start_minikube_cluster() {
    echo "############## START MINIKUBE CLUSTER ##############"

    # Start Minikube with your desired configurations
    minikube start --memory=8192 --cpus=4 --driver=hyperkit 
    
    # Check if Minikube started successfully
    if [ $? -eq 0 ]; then
        echo "Minikube cluster started successfully."
    else
        echo "Error: Minikube failed to start."
        exit 1
    fi
}

# Function to set up Istio environment
setup_istio_environment() {
    echo "############## SETUP ISTIO ENV ##############"
    # Get current directory
    export SCRIPTDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

    # Verify the Istioctl version
    export ISTIO_DIR=$(ls | grep istio-1)

    # Set up the working directory path
    export PATH="$PATH:$SCRIPTDIR/$ISTIO_DIR/bin"

    # Install Istio profile
    echo "Istio profile installing..."
    istioctl install --set profile=demo -y

    # Enable Istio injection for the default namespace
    echo "Istio injection enabling..."
    kubectl label namespace default istio-injection=enabled
    kubectl get ns default --show-labels
    kubectl get namespace -L istio-injection
}

# Function to deploy microservices
deploy_microservices() {
    echo "############## DEPLOY MICROSERVICES ##############"
    kubectl apply -f microservices/deploy/service-mesh/apps
}

# 1. Check if Minikube IP is available
if ! minikube ip >/dev/null 2>&1; then
    start_minikube_cluster
else
    echo "Minikube IP is already available."
fi

# 2. Check if ISTIO ENV is available
if ! istioctl version >/dev/null 2>&1; then
    setup_istio_environment
else
    echo "ISTIO CTL is already available."
fi

# Continue with Istio setup and microservices deployment
deploy_microservices
