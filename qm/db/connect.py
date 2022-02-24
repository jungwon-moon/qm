import os
import sys
import json
from pathlib import Path
from qm.db.DB import POSTGRESCRUD
from pymongo import MongoClient
import psycopg2

SECRET_PATH = Path(__file__).resolve().parent
SECRET_FILE = SECRET_PATH / 'db.json'
secrets = json.loads(open(SECRET_FILE).read())

def mongodb_connect(properties):
    pass


def postgres_connect(properties):
    db = POSTGRESCRUD(properties)
    return db