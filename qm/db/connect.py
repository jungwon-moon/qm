from qm.db.DB import POSTGRESCRUD


def postgres_connect(properties):
    db = POSTGRESCRUD(properties)
    return db
