# NOTE

## Install Multi Chart

```bash
export ISTIO_CHART=istio-multichart
helm install --debug --dry-run $ISTIO_CHART istio/istio-helm
helm install $ISTIO_CHART istio/istio-helm
```

## Install Single Chart
```bash
# IMPORTANT !install istiod at first!
# if helm-deployment not successful => install istio with istioctl and delete deployments and retry

# setup env variables
export ISTIOD_CHART=istiod
export EGRESS_CHART=istio-egress-gw
export INGRESS_CHART=istio-ingress-gw

# debug
helm install --debug --dry-run $ISTIOD istio/istio-helm/$ISTIOD
helm install --debug --dry-run $EGRESS_CHART istio/istio-helm/$EGRESS_CHART
helm install --debug --dry-run $INGRESS_CHART istio/istio-helm/$INGRESS_CHART

# create chart
helm install $ISTIOD_CHART istio/istio-helm/$ISTIOD_CHART
helm install $EGRESS_CHART istio/istio-helm/$EGRESS_CHART
helm install $INGRESS_CHART istio/istio-helm/$INGRESS_CHART

# verify
helm list
kubectl get deployment -n istio-system
``` 