
# Model Deployment Template

This repo contains:
- A dummy Scikit-learn model
- A FastAPI app exposing a `/predict` endpoint
- Dockerfile for containerization
- GitHub Actions CI/CD workflow

## Run locally
```
uvicorn app.main:app --reload
```

## Docker
```
docker build -t model-api .
docker run -p 80:80 model-api
```
