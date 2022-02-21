import os
import sys
import json
from pathlib import Path
from qm.db.db_class import DB
from pymongo import MongoClient
import psycopg2

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


def postgres_connect(host=None, port=5432):

    if os.path.isfile(SECRET_FILE) is True:
        secrets = json.loads(open(SECRET_FILE).read())
        for key, value in secrets.items():
            if key == 'gcp':
                info = DB(value)

    db = psycopg2.connect(host=info.host, dbname=info.dbname,
                          password=info.password, port=port)

    return db
