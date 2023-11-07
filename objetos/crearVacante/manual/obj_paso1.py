import random
from objetos.funciones import sendPostHeaders, base


def sueldoMin():
    sueldoMIN = random.randint(200, 25000)
    print(sueldoMIN)
    return sueldoMIN


def sueldoMax():
    sueldoMAX = random.randint(25001, 45000)
    print(sueldoMAX)
    return sueldoMAX


def puestos():
    apellido = ['abogado', 'desarrollador', 'medico', 'contador', 'Filósofo', 'Profesor', 'Periodista', 'Enfermero']
    aleatorio = random.choice(apellido)
    print(aleatorio)
    return aleatorio


puesto = puestos()

min: int = sueldoMin()

max: int = sueldoMax()

myBody = {
    "specialty": "automatización",
    "client": {
        "clientId": "ff8080818ab932ae018abee4d1f50039",
        "name": "involve",
        "logo": "https://s3.us-east-1.amazonaws.com/involve-resources-dev-pre/COMPANY/ff8080818ab932ae018abee4d1e10036/BUSSINES_LOGO_jpeg"
    },
    "typeSalary": {
        "catalogSystemId": "4028e4a986843df5018684517b460003",
        "name": "Bruto",
        "type": "typeSalary",
        "status": True,
        "keySystem": "MEX"
    },
    "periodicitySalary": {
        "catalogSystemId": "0000000088d5e9020188dfc7be19001d",
        "name": "Mes",
        "type": "periodicitySalary",
        "status": True,
        "keySystem": "MEX"
    },
    "commissions": False,
    "confidential": False,
    "salaryShow": True,
    "benefitsInvolve": [
        {
            "benefitId": "ff8081817b837f74017b838148a00000"
        }
    ],
    "vacancyOrigin": "MANUAL",
    "city": {
        "cityId": "2c9f936481969f0cccc996a00e090285",
        "name": "Miguel Hidalgo",
        "stateCode": "MX-CMX",
        "countryCode": "MX",
        "latitude": 19.40824,
        "longitude": -99.19212,
        "state": {
            "stateId": "2c9f936481969f0bbbb996a00e090009",
            "name": "Ciudad de México",
            "countryCode": "MX",
            "fipsCode": "9",
            "iso2": "MX-CMX",
            "latitude": 19.28333,
            "longitude": -99.13333,
            "country": {
                "countryId": "2c9f936481969f0aaaa996a00e090001",
                "capital": "Mexico City",
                "currency": "MXN",
                "currencySymbol": "$",
                "iso2": "MX",
                "iso3": "MEX",
                "latitude": 19.4284,
                "longitude": -99.1276,
                "name": "Mexico",
                "nameNative": "México",
                "phoneCode": "52",
                "region": "Americas",
                "subregion": "Central America",
                "timezones": "[{\"zoneName\":\"America/Bahia_Banderas\",\"gmtOffset\":-21600,\"gmtOffsetName\":\"UTC-06:00\",\"abbreviation\":\"CST\",\"tzName\":\"Central Standard Time (North America\"},{\"zoneName\":\"America/Cancun\",\"gmtOffset\":-18000,\"gmtOffsetName\":\"UTC-05:00\",\"abbreviation\":\"EST\",\"tzName\":\"Eastern Standard Time (North America\"},{\"zoneName\":\"America/Chihuahua\",\"gmtOffset\":-25200,\"gmtOffsetName\":\"UTC-07:00\",\"abbreviation\":\"MST\",\"tzName\":\"Mountain Standard Time (North America\"},{\"zoneName\":\"America/Hermosillo\",\"gmtOffset\":-25200,\"gmtOffsetName\":\"UTC-07:00\",\"abbreviation\":\"MST\",\"tzName\":\"Mountain Standard Time (North America\"},{\"zoneName\":\"America/Matamoros\",\"gmtOffset\":-21600,\"gmtOffsetName\":\"UTC-06:00\",\"abbreviation\":\"CST\",\"tzName\":\"Central Standard Time (North America\"},{\"zoneName\":\"America/Mazatlan\",\"gmtOffset\":-25200,\"gmtOffsetName\":\"UTC-07:00\",\"abbreviation\":\"MST\",\"tzName\":\"Mountain Standard Time (North America\"},{\"zoneName\":\"America/Merida\",\"gmtOffset\":-21600,\"gmtOffsetName\":\"UTC-06:00\",\"abbreviation\":\"CST\",\"tzName\":\"Central Standard Time (North America\"},{\"zoneName\":\"America/Mexico_City\",\"gmtOffset\":-21600,\"gmtOffsetName\":\"UTC-06:00\",\"abbreviation\":\"CST\",\"tzName\":\"Central Standard Time (North America\"},{\"zoneName\":\"America/Monterrey\",\"gmtOffset\":-21600,\"gmtOffsetName\":\"UTC-06:00\",\"abbreviation\":\"CST\",\"tzName\":\"Central Standard Time (North America\"},{\"zoneName\":\"America/Ojinaga\",\"gmtOffset\":-25200,\"gmtOffsetName\":\"UTC-07:00\",\"abbreviation\":\"MST\",\"tzName\":\"Mountain Standard Time (North America\"},{\"zoneName\":\"America/Tijuana\",\"gmtOffset\":-28800,\"gmtOffsetName\":\"UTC-08:00\",\"abbreviation\":\"PST\",\"tzName\":\"Pacific Standard Time (North America\"}]",
                "tld": ".mx",
                "translations": "{\"br\":\"México\",\"pt\":\"México\",\"nl\":\"Mexico\",\"hr\":\"Meksiko\",\"fa\":\"مکزیک\",\"de\":\"Mexiko\",\"es\":\"México\",\"fr\":\"Mexique\",\"ja\":\"メキシコ\",\"it\":\"Messico\"}",
                "flagCountry": "https://flagcdn.com/w20/mx.png"
            }
        }
    },
    "modality": {
        "catalogSystemId": "4028e4a986843df50186845177fa0000",
        "name": "Presencial",
        "type": "modalityWork",
        "status": True,
        "keySystem": "MEX"
    },
    "salaryMaximum": max,
    "salaryMinimum": min,
    "salaryExactly": None,
    "position": {
        "position": puesto
    }
}

def paso1(headers):
    url = base + 'vacancy/management'
    vacantId = sendPostHeaders(url, headers, myBody, 200)
    vacantId = vacantId['vacantId']
    return vacantId
