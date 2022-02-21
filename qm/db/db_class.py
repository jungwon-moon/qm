class DB:
    def __init__(self, param):
        for key, value in param.items():
            if key == 'host':
                self.host = value
            if key == 'dbname':
                self.dbname = value
            if key == 'user':
                self.user = value
            if key == 'password':
                self.password = value
