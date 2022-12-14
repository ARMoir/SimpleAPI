import os
import datetime
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
        
        if output not in send.block():
            print('\n')
            print(str(datetime.datetime.now()))
            print(request)
            print(output)

if __name__ == '__main__':

    ip = '0.0.0.0'
    port = 1337
    timeout = 1
    database = 'values'
 
    config = []
    config.append(ip)
    config.append(port)
    config.append(timeout)
    config.append(database)

    run(config)
       
