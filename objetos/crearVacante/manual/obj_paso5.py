from objetos. funciones import sendPostHeaders, base

myBody = {
    "listVacantPsychometricTestInvolve": [],
    "newQuestions": [
        {
            "exclud": False,
            "type": "VIDEO",
            "question": "pregunta 1",
            "typeQuestion": "CERRADA",
            "isArmed": False
        },
        {
            "exclud": False,
            "type": "VIDEO_S",
            "question": "pregunta 2",
            "typeQuestion": "CERRADA",
            "isArmed": False
        }
    ]
}
def paso5(headers, vacantId):
    url = base + 'vacancy/management/step5/' + vacantId
    print(url)
    sendPostHeaders(url, headers, myBody, 200)
