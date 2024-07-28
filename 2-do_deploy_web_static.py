#!/usr/bin/python3
""" The Fabric script distributes an archive to my servers"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['54.165.3.212', '100.24.235.18']
env.user = "ubuntu"


def do_pack():
    """
    archives contents of web_static
    """
    local("mkdir -p versions")

    time_format = "%Y%m%d%H%M%S"
    date_time = datetime.now().strftime(time_format)
    archive_path = "versions/web_static_" + date_time + ".tgz"

    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path


def do_deploy(archive_path):
    """
    Distributes an archive to my web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename = os.path.basename(archive_path)
        archive_folder = "/data/web_static/releases/{}".format(
                                                        filename.split(".")[0])
        run('mkdir -p {}'.format(archive_folder))
        run('tar -xzf /tmp/{} -C {}'.format(filename, archive_folder))
        run('rm /tmp/{}'.format(filename))
        run('mv {}/web_static/* {}/'.format(archive_folder, archive_folder))
        run('rm -rf {}/web_static'.format(archive_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(archive_folder))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
