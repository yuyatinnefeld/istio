# Setup Istio

## Install Istio CTL
```bash
# Download and extract ctl file
curl -L https://istio.io/downloadIstio | sh -

# Check the Istio ctl version
ls | grep istio
ISTIO_VERSION=istio-1.19.3

# Setup working directory path
export PATH="$PATH:$(pwd)/$ISTIO_VERSION/bin"

# Verify
istioctl version
```

## create a profile
```bash
# Install istio
istioctl install --set profile=demo -y
istioctl verify-install

# Verify all components
kubectl get all -n istio-system
```