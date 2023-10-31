#pip3 install requests
import requests

base = 'https://pre.micros.involverh.com.mx/'
def sendGet(url,codeHttp: int):
    req = requests.get(url)
    resultado = str(req.status_code)
    print('Get status: ' + resultado)
    assert req.status_code == codeHttp


def sendPost(url, myBody, codeHttp):
    req = requests.post(url, json=myBody)
    print('Post status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHttp
    resultado = req.json()
    headers = req.headers
    return resultado, headers

def sendPatch(url, headers, myBody, codeHttp):
    req = requests.patch(url, headers=headers, json=myBody)
    print('Patch status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHttp


def sendPut(url, headers, codeHttp):
    try:
        req = requests.put(url, headers=headers)
        print('PUT status: ' + str(req.status_code))
        assert req.status_code == codeHttp
    except Exception as e:
        print(e)

def sendPostSinBody(url, codeHttp):
    req = requests.post(url)
    print('Post Sin body status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHttp

def sendPostHeaders(url, headers, myBody, codeHttp):
    req = requests.post(url, headers=headers, json=myBody)
    print('Patch status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHttp
