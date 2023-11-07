from objetos.funciones import sendPostHeaders

myBody = {
    "newQuestions": [
        {
            "question": "hola mundo",
            "type": "AREA_SPECIALTY",
            "typeQuestion": "CERRADA",
            "isArmed": False,
            "exclud": False,
            "typeAnswer": True
        },
        {
            "question": "hola mundo 2",
            "type": "HARD_SKILL",
            "typeQuestion": "EXPERIENCIA",
            "isArmed": False,
            "exclud": False,
            "yearsExperience": 2
        },
        {
            "question": "hola mundo 3",
            "type": "SOFT_SKILL",
            "typeQuestion": "CERRADA",
            "isArmed": False,
            "exclud": False,
            "typeAnswer": True
        }
    ]
}
def paso4(headers, vacantId):
    url = 'https://pre.micros.involverh.com.mx/vacancy/management/step4/' + vacantId
    print(url)
    sendPostHeaders(url, headers, myBody, 200)