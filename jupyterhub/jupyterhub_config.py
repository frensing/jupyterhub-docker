# JupyterHub configuration
#
## If you update this file, do not forget to delete the `jupyterhub_data` volume before restarting the jupyterhub service:
##
##     docker volume rm jupyterhub_jupyterhub_data
##
## or, if you changed the COMPOSE_PROJECT_NAME to <name>:
##
##    docker volume rm <name>_jupyterhub_data
##

c = get_config()

import os
# pjoin = os.path.join

# runtime_dir = os.path.join('/srv/jupyterhub')


# ## Generic
# c.JupyterHub.admin_access = True
# c.Spawner.default_url = '/lab'

c.JupyterHub.port = 80

# ## Cookie secret and state db
# c.JupyterHub.cookie_secret_file = pjoin(runtime_dir, 'cookie_secret')
# c.JupyterHub.db_url = pjoin(runtime_dir, 'jupyterhub.sqlite')

## Authenticator
from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.GitHubOAuthenticator.oauth_callback_url = 'http://ai-marketplace-1.cs.upb.de/hub/oauth_callback'
c.GitHubOAuthenticator.client_id = ''
c.GitHubOAuthenticator.client_secret = ''

# c.Authenticator.allowed_users = {'frensing'}
c.Authenticator.admin_users = {'frensing'}

## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# # Other stuff
# c.Spawner.cpu_limit = 1
# c.Spawner.mem_limit = '10G'


# ## Services
# c.JupyterHub.services = [
#     {
#         'name': 'cull_idle',
#         'admin': True,
#         'command': 'python3 /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
#     },
# ]
