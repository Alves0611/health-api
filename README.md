# Health API

A simple health-check API built with Python and Flask, containerized using Docker.

## Requirements

- Docker installed

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/health-api.git
cd health-api
docker build -t health-api .
docker run -d -p 8080:8080 health-api
curl http://localhost:8080/health


## the message should be {"status":"ok"}
