# celery-flask-k8s
Flask api with multi-worker, asynchronous task queue. 

(add diagram here)

## install & run 
if you have kubectl installed run the 2 lines below to setup the project in your kubernetes cluster:
```
git clone git@github.com:nnethercott/celery-flask-k8s.git && cd celery-flask-k8s
kubectl apply -f k8s/ 
```
