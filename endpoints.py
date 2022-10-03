import datetime

def get(reponse):

    try:
        get = reponse[0]         
        get = get.split('HTTP')
        get = get[0].replace('GET','').strip()

    except Exception as error:
        get = str(error)
    
    finally:
        return get

def list():
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
            print(items)

        if items[1] == '':
            output = default(config, list(), response)

        if items[1] == 'time':
            output = time(request) 

    except Exception as error:
        output = str(error)

    finally:
      return output

def default(config, api, response):

    output = 'Created by: Alex Moir <br>'
    output += 'Email: Alex@Moir.pw <br>'
    output += '<br>'

    for endpoint in api:
        output += '<a href="http://{0}/{1}">http://{0}/{1}<a><br>'.format(config.data['Host'], endpoint)
    
    output += '<br>'
    output += '{0} <br>'.format(response)

    return output

def time(request):
    now = str(datetime.datetime.now())
    print(now)

    return now