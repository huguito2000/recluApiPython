from objetos.funciones import sendPost
from objetos.obj_login import url, myObj
def login():
    try:
        resultado, headers = sendPost(url,  myObj, 200)
        token = headers['token']
        print(token)
        print('paso el login')
        return ' Se hizo login correctamente', token
    except Exception as e:
        print('No se paso el login', str(e))
        return 'No se realizo el login'

