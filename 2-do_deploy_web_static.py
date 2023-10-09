#!/usr/bin/python3
""" script to distribute an archive to web servers """

from fabric.api import *
from os.path import exists

env.hosts = ['100.26.170.176', '100.24.72.207']

def do_deploy(archive_path):
    """ Distribute an archive to web servers """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        filename = archive_path.split('/')[-1]
        no_extension = filename.split('.')[0]

        remote_dir = "/data/web_static/releases/"
        full_path = remote_dir + no_extension

        # Create necessary directories
        run("mkdir -p {}".format(full_path))

        # Uncompress the archive to the target directory
        run("tar -xzf /tmp/{} -C {}/".format(filename, full_path))

        # Delete the uploaded archive
        run("rm /tmp/{}".format(filename))

        # Move the contents to the desired location
        run("mv {}/web_static/* {}/".format(full_path, full_path))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(full_path))

        # Delete the existing /data/web_static/current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(full_path))

        return True
    except:
        return False

