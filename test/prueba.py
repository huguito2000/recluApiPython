import requests
def post(url, myObj, codeHTTP):
    req = requests.post(url, json=myObj)
    print('Post status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHTTP
    resultado = req.json()
    headers = req.headers
    return resultado, headers


