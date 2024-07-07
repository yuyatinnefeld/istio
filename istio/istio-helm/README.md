export EGRESS_CHART=istio-egress-gw
export INGRESS_CHART=istio-ingress-gw
export ISTIOD_CHART=istiod

# debug
helm install --debug --dry-run $EGRESS_CHART istio/istio-helm/$EGRESS_CHART
helm install --debug --dry-run $INGRESS_CHART istio/istio-helm/$INGRESS_CHART
helm install --debug --dry-run $ISTIOD istio/istio-helm/$ISTIOD

# create chart
helm install $EGRESS_CHART istio/istio-helm/$EGRESS_CHART
helm install $INGRESS_CHART istio/istio-helm/$INGRESS_CHART
helm install $ISTIOD_CHART istio/istio-helm/$ISTIOD_CHART

# verify
helm list
kubectl get deployment -n istio-system