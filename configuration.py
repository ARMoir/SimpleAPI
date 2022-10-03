import sqlite3

class set:
    
    def __init__(self, config):

        self.port = config[0]
        self.timeout = config[1]
        self.database = sqlite3.connect('{0}.db'.format(config[2]))

        self.data = {}
        self.connection = ''
