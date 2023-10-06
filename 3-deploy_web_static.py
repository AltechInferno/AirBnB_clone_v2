#!/usr/bin/python3
"""fabric script for full deployment"""

from fabric.api import local, put, run, task, env
from datetime import datetime
import os

env.hosts = ['100.26.170.176', '100.24.72.207']

@task
def do_pack():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"
    try:
        local(f"mkdir -p versions")
        local(f"tar -cvzf {archive_name} web_static/")
        return archive_name
    except Exception as e:
        return None

@task
def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_name)[0]
        release_folder = f'/data/web_static/releases/{archive_no_ext}'
        tmp_archive_path = f'/tmp/{archive_name}'

        put(archive_path, tmp_archive_path)
        run(f'mkdir -p {release_folder}')
        run(f'tar -xzf {tmp_archive_path} -C {release_folder}')
        run(f'rm {tmp_archive_path}')
        run(f'mv {release_folder}/web_static/* {release_folder}/')
        run(f'rm -rf {release_folder}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {release_folder} /data/web_static/current')

        print("Deployment done")
        return True
    except Exception as e:
        return False

@task
def deploy():
    try:
        archive_path = do_pack()
        if archive_path:
            return do_deploy(archive_path)
        return False
    except Exception as e:
        return False

