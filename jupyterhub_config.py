c = get_config()  # noqa
from dockerspawner import DockerSpawner
from datetime import datetime
import time


options_form_tpl = """
<label for="image">Image</label>
<input name="image" class="form-control" placeholder="the image to launch (default: {default_image})"></input>
"""


def get_options_form(spawner):
    return options_form_tpl.format(default_image=spawner.image)


c.JupyterHub.authenticator_class = 'dummy'


class NewContainerSpawner(DockerSpawner):
    def template_namespace(self):
        ns = super().template_namespace()
        ns['start_timestamp'] = int(time.time())
        return ns

c.JupyterHub.spawner_class = NewContainerSpawner

c.DockerSpawner.options_form = get_options_form
c.DockerSpawner.name_template = "{prefix}-{username}-{start_timestamp}"

# We need to explicitly set this now
c.DockerSpawner.cmd = ["jupyterhub-singleuser"]

# specify that DockerSpawner should accept any image from user input
c.DockerSpawner.allowed_images = "*"

# tell JupyterHub to use DockerSpawner
c.DockerSpawner.network_name = "jupyterhub"

# while using dummy auth, make the *public* (proxy) interface private
c.JupyterHub.ip = "0.0.0.0"

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = "0.0.0.0"

# pick a default image to use when none is specified
c.DockerSpawner.image = "jupyter/base-notebook"

# don't delete containers when they stop, so we can look at logs
c.DockerSpawner.remove = False

# Mount an empty volume on the home directory, to simulate $HOME in the built
# image not showing up when user launches on a hub.
c.DockerSpawner.mounts = [
    {"source": "homes", "target": "/home/jovyan"}
]

