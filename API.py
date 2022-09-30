import io
import socket
import datetime
import json

port = 1337
timeout = 1
data = {}

while True:

    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind(('0.0.0.0', port))
        serversocket.listen(-1)
        connection, address = serversocket.accept()
        connection.settimeout(timeout)
        buffer = connection.recv(io.DEFAULT_BUFFER_SIZE)
    except Exception as error:
        error = str(error)
        buffer = ''
        if 'timed out' not in error:
            print(error)
            break

    if len(buffer) > 0:
        reponse = buffer.decode('utf-8', errors='ignore')
        reponse = reponse.split('\r\n')  

        for item in reponse:
            name = item.split(':')
            name = name[0]
            data[name] = item.replace('{0}:'.format(name), '').strip() 
            
        get = reponse[0]
        get = get.split('HTTP')
        get = get[0].replace('GET','').strip()

        if '/api/' in get:
            get = get.replace('/api/','')
            items = get.split('/')

            for item in items:
                print(item)

                if item == 'time':
                    now = str(datetime.datetime.now())
                    get = now
                    print(now)

        else:
            get = 'Created by: Alex Moir <br>'
            get += 'Email: Alex@Moir.pw <br>'
            get += 'API: http://{0}/api/ <br>'.format(data['Host'])
            get += '<br>'
            get += '{0} <br>'.format(reponse)

        output = 'HTTP/1.0 200 OK\r\n'
        output += 'Content-Length: {0}\r\n'.format(len(str(get)))
        output += 'Content-Type: text/html; charset=UTF-8\r\n'
        output += '\r\n{0}\r\n'.format(str(get))

        connection.sendall(str.encode(output))


       
