from datetime import datetime
from objetos.funciones import sendPostHeaders, base

now = datetime.now()
correo = 'cand' + str(now.day) + str(now.month) + str(now.minute) + str(now.second) + '@yopmail.com'
print(correo)

url = base + 'user/recruitment-team/invitation'
myBody = [
    {
        "email": correo,
        "rol": "RECRUITER"
    }
]

def invitacion(headers):
    sendPostHeaders(url, headers, myBody, 200)