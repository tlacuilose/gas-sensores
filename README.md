# Steps

docker build -t reportes-service .

kubectl delete -f reportes-deployment.yml

kubectl apply -f reportes-deployment.yml

minikube service reportes-service 
