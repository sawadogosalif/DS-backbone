# Use the base image
ARG BASE_CONTAINER=jupyter/datascience-notebook:latest
FROM $BASE_CONTAINER

# Replace default user "jovyan" with custom user specified by NB_USER
RUN usermod -l ${NB_USER} jovyan && \
    usermod -d /home/${NB_USER} -m ${NB_USER}

# Switch back to the custom user
USER ${NB_USER}



# Install jupyterlab-s3-browser extension
RUN pip install jupyterlab-s3-browser && \
    pip install -r requirements.txt && \
    jupyter serverextension enable --py jupyterlab_s3_browser && \
    jupyter lab build && \
    jupyter lab clean
