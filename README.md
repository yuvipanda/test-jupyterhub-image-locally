Simple config to test if an image you want to use with your JupyterHub works

## Pre-requisites

On your local machine, you need the following tools installed:

1. An installation of [Docker](https://www.docker.com/)
2. An installation of [the Docker compose plugin](https://docs.docker.com/compose/install/#scenario-two-install-the-compose-plugin)

## Set-up

1. Clone this git repository

   ```bash
   git clone https://github.com/yuvipanda/test-jupyterhub-image-locally.git
   cd test-jupyterhub-image-locally
   ```

2. Start up the configured JupyterHub via `docker compose`.

   ```bash
   docker compose up --build
   ```

3. Go to https://localhost:8000, you should see a JupyterHub running!

4. Login with any username, and any password.

5. You should see a text box that allows you to specify any docker image to start. Enter the
   name of the image you wanna try.

   Note that if you are pulling from a remote registry, large images may take a while to pull.
   The default configuration waits upto 5 minutes for an image to start. You can speed this up
   by manually doing a `docker pull <image>` before trying.

6. If it starts up successfully, then success!

7. If the image fails to start, you can use regular `docker` commands to look at its logs.

   First, find the id of the container that failed.

   ```bash
   docker ps -a
   ```

   The container *name* should look like `jupyter-<username>-<unix-timestamp>`. For example, if your
   username was `test`, and you tried to start the server somemtime on May 27, 2024, the name of the
   container may look like `jupyter-test-1715981236`

   Once you have find the name of the container, you can look at container logs with:

   ```bash
   docker logs <container-name>
   ```

## Useful resources

[This discourse topic](https://discourse.jupyter.org/t/simplest-possible-dockerfile-that-runs-with-jupyterhub/25810)
has some examples of what a 'minimal working `Dockerfile` for use with a JupyterHub` looks like,
and you may find it useful!

## Common issues

### "404 : Not Found"

Your server starts, but you get a '404: Not Found' message on your browser.

[![Jupyter Server: 404](images/404.png)]

This *most likely* means that you don't have the `jupyterhub` package installed
inside the container image. Make sure that you have one of:

1. The [`jupyterhub`](http://pypi.org/project/jupyterhub) package installed from PyPI
2. `jupyterhub` or `jupyterhub-singleuser` package installed from `conda-forge`

You only need one of these, not both.
