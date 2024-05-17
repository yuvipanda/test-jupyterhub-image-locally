FROM quay.io/jupyterhub/jupyterhub:4

RUN python3 -m pip install dockerspawner jupyterhub-tmpauthenticator

COPY jupyterhub_config.py jupyterhub_config.py