# Istio Guide

## Start Minikube Cluster
```bash
minikube start --memory=8192 --cpus=4 --driver=hyperkit
```

## Deploy Microservices
`./deploy`

## Step 1 - Initial Setup
`./step1`
- install Istio CTL
- install Istio
- inject sidecar proxy (envoy)

## Step 2 - Kiali
`./step2`

## Step 3 - Traffic Management
`./step3`
- gateway
- virtual services
- destination rules

## Step 4 - Security
`./step4`

## Step 5 - Observability
`./step5`