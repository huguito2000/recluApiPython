from objetos.funciones import sendPost
from objetos.obj_login import HacerLogin
def loginValido():
    try:
        resultado, headers = HacerLogin()
        token = headers['token']
        print(resultado)
        print(token)
        print('paso el login')
        return ' Se hizo login correctamente', token, resultado
    except Exception as e:
        print('No se paso el login', str(e))
        return 'No se realizo el login'


