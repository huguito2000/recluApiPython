from objetos.registro.obj_registro import reg1
from objetos.registro.obj_registro2 import reg2
from objetos.registro.obj_registro3 import reg3
from objetos.registro.obj_registro4 import reg4
from objetos.registro.obj_registro5 import reg5
from objetos.registro.obj_registro6 import reg6
from objetos.registro.obj_registro7 import reg7

# Paso1
# registry Se mandan los datos de registro y se obtiene el token
resultado, headers = reg1()
code = str(resultado['user']['checkCode'])
print('el codigo es: ' + code)
print('los headers son: ' + str(headers))
token = headers['token']
token = str(token.replace('Bearer ', ''))
print('el token es: ' + token)
headers = {
    'Authorization': f'Bearer {token}'
}

# se manda un put con losd atos de la creacion de la contraseña
reg2(headers)

# se manda un PATCH con el recruiter y la dataRecruite1
reg3(headers)

# paso2 envio de codigo
# se manda el check email
reg4(code)

# se manda recruiter PATCH
reg5(headers)

# paso3 formulario
# se manda PATCH del formulario de nombre
reg6(headers)

# se manda PATCH del formulario de compañia
reg7(headers)
