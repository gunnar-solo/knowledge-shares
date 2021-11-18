kind create cluster

docker build -t hackable ./hackable
docker build -t flip-flop ./flip-flop

kind load docker-image hackable
kind load docker-image flip-flop

kubectl apply -f ./hackable/manifests.yaml
kubectl apply -f ./flip-flop/manifests.yaml
