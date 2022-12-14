import io
import socket

def connect(config):

    try:

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind((config.ip, config.port))
        serversocket.listen(0)

        connection, address = serversocket.accept()
        connection.settimeout(config.timeout)

        buffer = connection.recv(io.DEFAULT_BUFFER_SIZE)

    except Exception as error:

        buffer = ''
        error = str(error)

        if 'timed out' not in error:
            print(error)

    finally:
        config.data['address'] = address
        config.connection = connection

        return buffer
            
def response(config, buffer):

    if buffer:
        response = buffer.decode('utf-8', errors='ignore')
        response = response.split('\r\n')  

        for item in response:
            name = item.split(':')
            name = name[0]
            config.data[name] = item.replace('{0}:'.format(name), '').strip()
    else:
        response = ''

    return response