

class set:
    
    def __init__(self, config):

        self.port = config[0]
        self.timeout = config[1]       

        self.data = {}
        self.connection = ''
