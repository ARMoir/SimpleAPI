import datetime
import database
import json

def get(reponse):

    try:
        get = reponse[0]         
        get = get.split('HTTP')
        get = get[0].replace('GET','').strip()

    except Exception:
        get = ''
    
    finally:
        return get

def urls():
    endpoint = []
    endpoint.append('time')
    endpoint.append('insert')
    endpoint.append('query')

    return endpoint

def check(config, response, request):
    output = request

    try:

        if '/' in request:
            items = request.split('/')

            if items[1] == '':
                output = default(config, urls(), response)

            if items[1] == 'time':
                output = time(items) 

            if items[1] == 'insert':
                output = insert(config, items) 

            if items[1] == 'query':
                output = query(config, items) 

    except Exception as error:
        output = str(error)

    finally:
      return output

def default(config, api, response):
    output = '<a href="https://github.com/ARMoir/SimpleAPI">SimpleAPI</a><br>'
    output += 'Created by: Alex Moir <br>'
    output += 'Email: Alex@Moir.pw<br>'
    output += '<br>'

    for endpoint in api:
        output += '<a href="http://{0}/{1}">http://{0}/{1}</a><br>'.format(config.data['Host'], endpoint)
    
    output += '<br>'
    output += '{0} <br>'.format(response)

    return output

def time(items):   
    values = {}
    values[items[1]] = str(datetime.datetime.now())
    output = json.dumps(values)

    return output

def insert(config, items):
    items = database.sanitize(items)
    output = database.create(config)
    values = {}

    if len(items) < 4 or '' is items[2] or '' is items[3]:
        values['error'] = 'missing key and value to insert'
        values['format'] = 'http://{0}/insert/{{key}}/{{value}}'.format(config.data['Host'])

    else:
        timestamp = datetime.datetime.now() 
        time = timestamp.strftime('%Y%m%d%H%M%S%f')
        values['inserted'] = database.set(config.database, "INSERT INTO [{0}] VALUES ('{1}','{2}','{3}')".format('values', time, items[2], items[3]))

    output = json.dumps(values)

    return output

def query(config, items):
    items = database.sanitize(items)
    output = database.create(config)
    values = {}

    if len(items) < 3 or '' is items[2]:
        values['error'] = 'missing key value to query'
        values['format'] = 'http://{0}/query/{{key}}'.format(config.data['Host'])

    else:
        output = database.get(config.database, "SELECT [{0}] FROM [{1}] WHERE [{2}] = '{3}' ORDER BY [{4}] DESC LIMIT 1".format('value', 'values', 'key', items[2], 'time'))       
        values[items[2]] = output[0][0].replace('%20', ' ')
    
    output = json.dumps(values)

    return output