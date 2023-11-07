from objetos.funciones import sendPatch

myBody = [
    {
        "op": "replace",
        "path": "/mission",
        "value": "Informar de manera objetiva y veraz los acontecimientos relevantes para mantener a la sociedad informada y promover la libertad de expresión."
    },
    {
        "op": "replace",
        "path": "/functions",
        "value": "* Investigar y recopilar información para la creación de noticias y reportajes. \n*  Entrevistar a fuentes relevantes para obtener declaraciones y opiniones. \n*  Redactar y editar contenido de calidad, incluyendo artículos, informes y notas de prensa. \n*  Seguir y cubrir eventos y noticias en tiempo real, aplicando los principios del periodismo ético y cumpliendo con los plazos establecidos."
    },
    {
        "op": "replace",
        "path": "/typePositionId",
        "value": "40288086796be11e01796c18e66f0064"
    },
    {
        "op": "replace",
        "path": "/contractId",
        "value": "40288088798adb5701798b18e4fb0000"
    },
    {
        "op": "replace",
        "path": "/peopleCharge",
        "value": "1"
    },
    {
        "op": "replace",
        "path": "/schedule",
        "value": "todos los dias"
    },
    {
        "op": "replace",
        "path": "/allNationality",
        "value": "true"
    },
    {
        "op": "replace",
        "path": "/workingDay",
        "value": {
            "catalogSystemId": "0000000088d5e9020188da01e8630000",
            "name": "Tiempo completo",
            "type": "workingDay",
            "status": True,
            "keySystem": "MEX"
        }
    },
    {
        "op": "replace",
        "path": "/steps",
        "value": "2"
    }
]
def paso2(headers, vacantId):
    url = 'https://pre.micros.involverh.com.mx/vacancy/management/' + vacantId
    print(url)
    sendPatch(url, headers, myBody, 200)