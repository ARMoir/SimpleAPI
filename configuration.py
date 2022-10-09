import sqlite3

class set:
    
    def __init__(self, config):

        self.ip = config[0]
        self.port = config[1]
        self.timeout = config[2]
        self.database = sqlite3.connect('{0}.db'.format(config[3]))

        self.data = {}
        self.connection = ''
