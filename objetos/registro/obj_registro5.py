from objetos.funciones import base, sendPatch
urlRecruiter = base + 'user/recruiter'

dataCheckEmail = [
    {
        "op": "replace",
        "path": "/stepsStatus",
        "value": 1
    }
]

#se manda recruiter PATCH
def reg5(headers):
    sendPatch(urlRecruiter, headers, dataCheckEmail, 200)
    print('reg5: se mando recruiter check email')