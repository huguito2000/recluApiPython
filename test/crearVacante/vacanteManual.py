from test.login1 import login
from objetos.crearVacante.manual.obj_paso1 import paso1
from objetos.crearVacante.manual.obj_paso2 import paso2
from objetos.crearVacante.manual.obj_paso3 import paso3
from objetos.crearVacante.manual.obj_paso4 import paso4
from objetos.crearVacante.manual.obj_paso5 import paso5
from objetos.crearVacante.manual.obj_paso6 import paso6
from objetos.crearVacante.manual.obj_publicar import publicar

headers, recruiter = login()

vacantId = paso1(headers)

paso2(headers, vacantId)

paso3(headers, vacantId)

paso4(headers, vacantId)

paso5(headers, vacantId)

paso6(headers, vacantId)

publicar(headers, vacantId)

