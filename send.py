def format(get):
    output = 'HTTP/1.0 200 OK\r\n'
    output += 'Content-Length: {0}\r\n'.format(len(str(get)))
    output += 'Content-Type: text/html; charset=UTF-8\r\n'
    output += '\r\n{0}\r\n'.format(str(get))

    return output

def output(config, out):
    out = format(out)
    config.connection.sendall(str.encode(out))

def block():
    item = []
    item.append(None)
    item.append('')
    item.append('/favicon.ico')

    return item