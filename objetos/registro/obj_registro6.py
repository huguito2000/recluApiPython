from objetos.funciones import base, sendPatch

urlRecruiter = base + 'user/recruiter'
nombres = [
    {
        "op": "replace",
        "path": "/user/name",
        "value": "hugo "
    },
    {
        "op": "replace",
        "path": "/user/lastName",
        "value": "rodriguez"
    },
    {
        "op": "replace",
        "path": "/user/secondLastName",
        "value": ""
    },
    {
        "op": "replace",
        "path": "/stepsStatus",
        "value": 8
    }
]

#paso3 formulario
#se manda PATCH del formulario de nombre
def reg6(headers):
    sendPatch(urlRecruiter, headers, nombres, 200)
    print('reg6: se manda formulario nombre')
