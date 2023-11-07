from objetos.funciones import sendPut, base

def publicar(headers,vacantId):
    url = base + 'vacancy/management/actived?vacantId=' + vacantId + '&approved=false'
    print(url)
    sendPut(url, headers, 200)