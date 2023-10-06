#!/usr/bin/python3
"""Distributes an archive to web servers using Fabric."""

from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['100.26.170.176', '100.24.72.207']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web servers
        put(archive_path, '/tmp/')

        # Construct paths and filenames
        archive_filename = archive_path.split('/')[-1]
        archive_name_no_extension = archive_filename.split('.')[0]
        release_dir = f'/data/web_static/releases/{archive_name_no_extension}'

        # Create the release directory and extract the archive
        run(f'mkdir -p {release_dir}')
        run(f'tar -xzf /tmp/{archive_filename} -C {release_dir}')
        run(f'rm /tmp/{archive_filename}')

        # Move files to the appropriate location
        run(f'mv {release_dir}/web_static/* {release_dir}/')
        run(f'rm -rf {release_dir}/web_static')

        # Update the symbolic link
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {release_dir} /data/web_static/current')

        return True
    except Exception as e:
        print(e)
        return False

