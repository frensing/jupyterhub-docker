FROM jupyterhub/jupyterhub:2.2.2

RUN pip install \
    dockerspawner \
    oauthenticator

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py
