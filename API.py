import server
import configuration
import endpoints
import send


def run(data):

    while True:
        config = configuration.set(data)
        buffer = server.connect(config)
        response = server.response(config, buffer)
        request = endpoints.get(response)
        out = endpoints.check(config, response, request)      
        send.output(config, out)        

if __name__ == '__main__':

    port = 1337
    timeout = 1
 
    config = []
    config.append(port)
    config.append(timeout)

    run(config)
       
