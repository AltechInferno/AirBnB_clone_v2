#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy: 
"""

from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['34.229.55.2', '100.26.178.240']

def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    if not exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split('/')[-1]
        archive_name_no_extension = archive_filename.split('.')[0]
        release_dir = f'/data/web_static/releases/{archive_name_no_extension}'
        tmp_archive_path = f'/tmp/{archive_filename}'

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, tmp_archive_path)

        # Create release directory and extract archive
        run(f'mkdir -p {release_dir}')
        run(f'tar -xzf {tmp_archive_path} -C {release_dir}')
        run(f'rm {tmp_archive_path}')

        # Move files to appropriate location
        run(f'mv {release_dir}/web_static/* {release_dir}/')
        run(f'rm -rf {release_dir}/web_static')

        # Update the symbolic link
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {release_dir} /data/web_static/current')

        return True
    except Exception as e:
        print(e)
        return False

