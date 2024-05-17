c = get_config()  # noqa


options_form_tpl = """
<label for="image">Image</label>
<input name="image" class="form-control" placeholder="the image to launch (default: {default_image})"></input>
"""


def get_options_form(spawner):
    return options_form_tpl.format(default_image=spawner.image)


c.JupyterHub.authenticator_class = 'tmp'
c.JupyterHub.spawner_class = 'docker'

c.DockerSpawner.options_form = get_options_form

# specify that DockerSpawner should accept any image from user input
c.DockerSpawner.allowed_images = "*"

# tell JupyterHub to use DockerSpawner
c.JupyterHub.spawner_class = "docker"
c.DockerSpawner.network_name = "jupyterhub"

# while using dummy auth, make the *public* (proxy) interface private
c.JupyterHub.ip = "0.0.0.0"

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = "0.0.0.0"

# pick a default image to use when none is specified
c.DockerSpawner.image = "jupyter/base-notebook"

# don't delete containers when they stop, so we can look at logs
c.DockerSpawner.remove = False

c.Spawner.start_timeout = 60 * 10
