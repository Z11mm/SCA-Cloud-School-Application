# SCA-Cloud-School-Application

### Python/Flask application
Project structure:
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

### Build image


