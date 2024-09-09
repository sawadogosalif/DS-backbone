
# Data Scientist Infrastructures

This project sets up a data scientist workbench with :
+ MLFlow for experiment tracking and model asset management;
+ PostgreSQL for a SQL engine and to serve as a backend for MLFlow;
+ MinIO to mimic  S3 and act as an artifact and data store;
+ Jupyterlab as an EDA environment.
## Prerequisites

1. **Install and Configure WSL 2:**
   - Ensure that WSL 2 is installed and properly configured on your system.
   - You can follow the Microsoft instructions to install WSL 2 [here](https://docs.microsoft.com/en-us/windows/wsl/install).

2. **Install Docker Desktop for Windows:**
   - Download and install Docker Desktop from [the official Docker website](https://www.docker.com/products/docker-desktop).

3. **Configure Docker to Use WSL 2:**
   - Open Docker Desktop and go to the settings.
   - Under the "General" tab, ensure that "Use the WSL 2 based engine" is checked.
   - Under the "Resources" > "WSL Integration" tab, ensure that your WSL 2 distribution is checked.
   - Under the "General" tab, check "Expose daemon on tcp://localhost:2375 without TLS".


## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sawadogosalif/DS-backbone.git
   cd DS-backbone
   ```

2. **Configure Environment Variables**
   Update a `default.env` file in the root directory with the following variables as you want.

3. **Build and Run Services**
   ```bash
   docker-compose --env-file default.env up -d
   ```

## Usage if use reverse proxy NGINX 

- **JupyterLab:** `http://sawalle.ds.notebooks`
- **MLflow:** `http://sawalle.ds.mlflow`
- **MinIO:** `http://sawalle.ds.s3`

## Usage if use localhost 

- **JupyterLab:** `http:localhost:8888`
- **MLflow:** `http:localhost:5555`
- **MinIO:** `http:localhost:9000`
Additionally, in the file `notebooks/tracking_example.py`, we demonstrate how to use MLflow efficiently.


## Services

### PostgreSQL
- **Image:** postgres:11
- **Port:** `5432`

### MinIO (S3)
- **Image:** minio/minio:RELEASE.2020-12-18T03-27-42Z
- **Port:** `9000`

### MLflow
- **Port:** `5000`

### JupyterLab
- **Port:** `8888`
- **Image:** jupyter/datascience-notebook:latest


### Nginx
- **Port:** `80`
- **Image:** nginx:1.25.5
