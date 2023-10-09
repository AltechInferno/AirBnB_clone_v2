#!/usr/bin/python3
"""the function do_deploy: """
from fabric.api import *
from datetime import datetime
from os.path import exists

# my ips
env.hosts = ['100.26.170.176', '100.24.72.207']


def do_deploy(archive_path):
    """archive to my web servers
    """

    if exists(archive_path) is False:
        return False

    fn = archive_path.split('/')[-1]
    
    no_tgz_dir = '/data/web_static/releases/' + "{}".format(fn.split('.')[0])
    tmp_dir = "/tmp/" + fn

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz_dir))
        run("tar -xzf {} -C {}/".format(tmp_dir, no_tgz_dir))
        run("rm {}".format(tmp_dir))
        run("mv {}/web_static/* {}/".format(no_tgz_dir, no_tgz_dir))
        run("rm -rf {}/web_static".format(no_tgz_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz_dir))
        
        return True
    except:
        return False
