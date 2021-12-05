# About

Microservice architecture

A gas company requires retrieving the information from its tank sensors and
creating a report.

Two microservices

- sensores-service: A flask API that using a proxy retrieves the information of
all tanks gas contents. /data
- reportes-service: A flask API that using a builder pattern, generates a report
that requires fetching the sensores-serivice through http, retrieving previous 
data from a db, generating the report and sending it. /reporte

# Built using

- Flask: for both API
- minikube: for simulating a local kubernetes cluster
- kubectl: for managing services and pods
- docker: for creating images

Repository includes .yml k8s deployement files and Dockerfiles for the images

# Steps

For reportes-service/sensores-connection.py, set environment variable
SENSORES_SERVICE_URL=http://localhost:8000/data

in secrets.yml encode all values to base64
```bash
echo -n <url> | base64
```


*Before building images always run eval, otherwise images from minikube will not be affected.*

```bash
eval $(minikube docker-env)
```

```bash
docker build -t reportes-service reportes-service/.
```

```bash
docker build -t sensores-service sensores-service/.
```

```bash
kubectl delete -f reportes-deployment.yml
```

```bash
kubectl apply -f secrets.yml
```

```bash
kubectl apply -f reportes-deployment.yml
```

```bash
kubectl apply -f sensores-deployment.yml
```

```bash
minikube service reportes-service 
```

# Info de kubernetes

Obtener la ip publica del servicio

```bash
kubectl get svc
```

Todos los servicios en k8s

```bash
kubectl get all
```

Describir un servicio

```bash
kubectl describe svc <nombre>
```

Revisar los pods activos

```bash
kubectl get pods -o wide
```

Abrir un pod en bash
```bash
kubectl exec --stdin --tty <nombre-del-pod> -- /bin/bash
```

Eliminar un pod revisar orchestration, se crea un pod con ip diferente

```bash
kubectl delete pod <nombre>
```

# Monitoring

View all installed and available metrics

```bash
minikube addons list
```

Enable metrics-server for monitoring pods resources. 

```bash
minikube addons enable metrics-server
```

View in dashboard with

```bash
minikube dashboard --url
```

View in command line

```bash
kubectl top pods
```

Install logviewer

```bash
minikube addons enable logviewer
```





# info 
CNI - agente que corre en cada nodo, vpn entre los nodos. pods entre los nodos.
calico??
node port
