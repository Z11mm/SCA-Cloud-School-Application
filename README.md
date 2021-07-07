# SCA-Cloud-School-Application
Hi there! 

This is my SCA Cloud School application assessment submission. Below is a description of a basic Python Flask web application, with instructions on how to build an image and deploy the application in a Docker container using Dockerfile.
## Python/Flask application
---
Directory structure:
```
├── docker
    ├── Dockerfile
    ├── .gitignore
    ├── requirements.txt
    └── app.py
```
*Dockerfile*
```
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
```

## Build image
---
`docker build --tag sca-cloud-school-application .`

```
[+] Building 10.3s (14/14) FINISHED
 => [internal] load build definition from Dockerfile 
 => => transferring dockerfile: 521B  
 => [internal] load .dockerignore
 => => transferring context: 2B                        
 => resolve image config for docker.io/docker dockerfile:1
 => [auth] docker/dockerfile:pull token for registry-1.docker.io
 ...
 ...
 => exporting to image
 => => exporting layers
 => => writing image sha256:eba5e4fde2d3ba716f67332b47c2bb491886fddcaab5d201946e37547b14bfb7
 => => naming to docker.io/library/sca-cloud-school-application
```

## Expected 
---
### Run image in container
```
$ docker run -dp 5000:5000 sca-cloud-school-application
e940762365a0dc584bb6513923f19ce0fbe5804292fe730fed33a6f03be431c8
```
### View running containers
```
$ docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED         STATUS         PORTS                                       NAMES
e940762365a0   sca-cloud-school-application   "python3 -m flask ru…"   7 seconds ago   Up 5 seconds  ...
```

### Check that application is running
Navigate to `http://localhost:5000` on your browser or run:
```
$ curl http://localhost:5000
Welcome to SCA Cloud School Application, this is my first assessment.
```

Here is a link to [my DockerHub repository](https://hub.docker.com/repository/docker/masterziii/sca-cloud-school-application)