import os
import sys
import json
from pathlib import Path
from qm.db.db_class import DB
from pymongo import MongoClient
import psycopg2

SECRET_PATH = Path(__file__).resolve().parent
SECRET_FILE = SECRET_PATH / 'db.json'


def mongodb_connect(properties):
    db = DB(properties)
    db = MongoClient(db.host, db.port)

    return db


def postgres_connect(properties):
    db = DB(properties)
    pgdb = psycopg2.connect(host=db.host, dbname=db.dbname,
                            password=db.password, port=db.port)
    return pgdb
