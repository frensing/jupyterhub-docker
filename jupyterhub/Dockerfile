FROM jupyterhub/jupyterhub:2.2.2

RUN pip install \
    dockerspawner \
    oauthenticator

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

COPY templates/ /etc/jupyterhub/templates
COPY static/ /usr/local/share/jupyterhub/static/external
