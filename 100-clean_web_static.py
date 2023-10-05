#!/usr/bin/python3
""" deployment """
from fabric.api import *


env.hosts = ['127.0.01']
env.user = "ubuntu"

def do_clean(number=0):
    number = int(number)

    if number <= 1:
        number_to_keep = 1
    else:
        number_to_keep = number

    try:
        # Clean local versions folder
        local('ls -t versions | tail -n +{} | xargs rm -rf'.format(number_to_keep))

        # Clean remote versions folder on both web servers
        path = '/data/web_static/releases'
        run('ls -t {} | tail -n +{} | xargs rm -rf'.format(path, number_to_keep))
    except Exception as e:
        print(e)
