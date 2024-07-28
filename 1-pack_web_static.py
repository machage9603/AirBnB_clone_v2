#!/usr/bin/python3
""" A Fabric script that generates a .tgz archive from contents
of the web_static folder"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    archives contents of web_static
    """
    local("mkdir -p versions")

    time_format = "%Y%m%d%H%M%S"
    date_time = datetime.now().strftime(time_format)
    archive_name = "versions/web_static_" + date_time + ".tgz"

    result = local("tar -cvzf {} web_static".format(archive_name))

    if result.failed:
        return None
    else:
        return archive_name


if __name__ == "__main__":
    do_pack()
