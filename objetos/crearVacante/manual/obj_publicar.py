from objetos.funciones import sendPut

def publicar(headers,vacantId):
    url = 'https://pre.micros.involverh.com.mx/vacancy/management/actived?vacantId=' + vacantId + '&approved=false'
    print(url)
    sendPut(url, headers, 200)