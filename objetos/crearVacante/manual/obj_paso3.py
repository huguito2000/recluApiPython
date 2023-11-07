from objetos.funciones import sendPostHeaders

myBody = {
    "academicTitle": "",
    "area": [
        {
            "exclud": False,
            "area": {
                "areaId": "40288087797b055a01797b12ab830007"
            },
            "yearExperience": 2
        }
    ],
    "hardSkill": [
        {
            "level": "INTERMEDIO",
            "skillId": "2c9f93647d0ba197017d14ef1b830061",
            "exclud": False
        }
    ],
    "idEducation": "402881cf79c889e50179c8902b470005",
    "levelEducationExclud": False,
    "idStatusEducation": "402880de79730a2c0179731b7c1b0003",
    "statusEducationExclud": False,
    "institution": [],
    "language": [],
    "softSkill": [
        {
            "skillId": "0000000088c520440188d618dc5b0148"
        }
    ],
    "speciality": [
        {
            "exclud": False,
            "speciality": {
                "specialtyId": "40288087797b055a01797b3703990021"
            },
            "yearExperience": 2
        }
    ]
}

def paso3(headers, vacantId):
    url = 'https://pre.micros.involverh.com.mx/vacancy/management/step3/' + vacantId
    print(url)
    sendPostHeaders(url, headers, myBody, 200)

