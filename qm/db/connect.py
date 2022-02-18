import os
import sys
import json
from pathlib import Path
from pymongo import MongoClient

SECRET_PATH = Path(__file__).resolve().parent
SECRET_FILE = SECRET_PATH / 'db.json'


def mongodb_connect(host=None, port=27017):

    if host is not None:
        pass

    elif os.path.isfile(SECRET_FILE) is True:
        secrets = json.loads(open(SECRET_FILE).read())
        for key, value in secrets.items():
            if key == 'host':
                host = value

    db = MongoClient(host, port)

    return db
