from pathlib import Path
from qm.db.DB import POSTGRESCRUD
from pymongo import MongoClient


def mongodb_connect(properties):
    pass


def postgres_connect(properties):
    db = POSTGRESCRUD(properties)
    return db
