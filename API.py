import os
import server
import configuration
import endpoints
import send

def run(data):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    while True:
        config = configuration.set(data)
        buffer = server.connect(config)
        response = server.response(config, buffer)
        request = endpoints.get(response)
        output = endpoints.check(config, response, request)      
        send.output(config, output)        

if __name__ == '__main__':

    port = 1337
    timeout = 1
    database = 'values'
 
    config = []
    config.append(port)
    config.append(timeout)
    config.append(database)

    run(config)
       
