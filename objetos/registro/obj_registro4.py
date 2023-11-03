from objetos.funciones import base, sendPostSinBody
from objetos.registro.obj_registro import correo
urlEmailCheck: str = str(base + 'notification/session-aux/check-email?email=' + correo + '&code=')

#paso2 envio de codigo
#se manda el check email
def reg4(code):
    sendPostSinBody(urlEmailCheck + code, 200)
    print('reg4: se manda el check email')