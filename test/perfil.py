from objetos.funciones import sendPost, sendPutBody
from objetos.obj_Perfil import urlPerfil, body
from test.login import loginValido

respuesta, token, resultado = loginValido()
print('el token es:' + token)
headers = {
    'Authorization': f'Bearer {token}'
}

resultado = resultado
print('el recruiter es:' + resultado['recruiterId'])

urlPerfil = urlPerfil + resultado
print(str(urlPerfil))


