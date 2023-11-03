from objetos.funciones import base, sendPut
from test.login import login


urlPass = base + 'notification/login/change-password?newPassword=Abcd.1234'

def cambioPass(headers):
    sendPut(urlPass, headers, 200)
    print('se cambia la pass')

