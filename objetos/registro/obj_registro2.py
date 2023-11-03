from objetos.funciones import base, sendPut

urlCrearPass = base + 'notification/registry/create-pass?password=Abcd.1234'

urlRecruiter = base + 'user/recruiter'
dataRecruite1 = data = [
	{
    	"op": "replace",
    	"path": "/stepsStatus",
    	"value": 0
	}
]

def reg2(headers):
	sendPut(urlCrearPass, headers, 200)
	print('reg2: se mando la contraseña')
