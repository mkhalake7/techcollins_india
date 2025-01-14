import logging
import os
import urllib

DEBUG = True
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "")
HOST = os.getenv("APPLICATION_HOST", "0.0.0.0")
PORT = int(os.getenv("APPLICATION_PORT", "8000"))
SQLALCHEMY_TRACK_MODIFICATIONS = False



DB_URI = 'sqlite:///j&j.db'




logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
