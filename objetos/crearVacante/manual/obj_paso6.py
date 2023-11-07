from objetos.funciones import sendPostHeaders

myBody = {
    "recruiters": [
        {
            "Notifications": True,
            "type": "AUXILIAR",
            "recruiterId": "ff8080818ab932ae018abee4d1ea0037"
        }
    ]
}

def paso6(headers, vacantId):
    url = 'https://pre.micros.involverh.com.mx/vacancy/management/step6/' + vacantId
    print(url)
    sendPostHeaders(url, headers, myBody, 200)

