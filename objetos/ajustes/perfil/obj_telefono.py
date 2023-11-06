from objetos.funciones import base, sendPatch

url = base + 'user/recruiter'

myBody = [
    {
        "op": "replace",
        "path": "/user/phone",
        "value": "+525569777077"
    }
]
def telefono(headers):
    sendPatch(url, headers, myBody, 200)
    print('se cambio el telefono')