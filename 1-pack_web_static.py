#!/usr/bin/python3
"""generate a .tgz archive from the contents of web_static folder.
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive"""
    try:
        # Create the versions directory if it doesn't exist
        os.makedirs("versions", exist_ok=True)

        # Generate the timestamp for the archive filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create the archive filename
        archive_name = "versions/web_static_{}.tgz".format(timestamp)

        # Compress the web_static folder into the archive
        local("tar -cvzf {} web_static".format(archive_name))

        return archive_name
    except Exception:
        return None

if __name__ == "__main__":
    result = do_pack()
    if result:
        print("Web static packed: {}".format(result))
    else:
        print("Web static packing failed.")

