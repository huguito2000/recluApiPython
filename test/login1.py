from objetos.obj_login import HacerLogin

def login():
    try:
        resultado, headers = HacerLogin()
        print(resultado)
        recruiter = resultado['recruiterId']
        print(recruiter)
        print('paso el login')
        return ' Se hizo login correctamente', headers, recruiter
    except Exception as e:
        print('No se paso el login', str(e))
        return 'No se realizo el login'


