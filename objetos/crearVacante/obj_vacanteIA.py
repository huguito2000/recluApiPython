from objetos.funciones import sendPostHeaders
url = 'https://assistant.qa.ia.involverh.com.mx/api/v1/vacancy/'

myBody = {
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
    "peopleCharge": 0,
    "salaryMaximum": 24000,
    "salaryMinimum": 12000,
    "salaryExactly": None,
    "positionId": "000000008878999b01888c7bb658000e"
}

def crearVacanteIA(headers):
    sendPostHeaders(url, headers, myBody, 200)


