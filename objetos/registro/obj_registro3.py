from objetos.funciones import base, sendPatch

urlCrearPass = base + 'notification/registry/create-pass?password=Abcd.1234'

urlRecruiter = base + 'user/recruiter'
dataRecruite1 = data = [
	{
    	"op": "replace",
    	"path": "/stepsStatus",
    	"value": 0
	}
]

# se manda un PATCH con el recruiter y la dataRecruite1
def reg3(headers):
	sendPatch(urlRecruiter, headers, dataRecruite1, 200)
	print('reg3: se mando el recruiter1 del registro')

