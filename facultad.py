from carrera import Carrera
class Facultad:
    __codigo=0
    __nombre=''
    __direccion=''
    __localidad=''
    __telefono=0
    __carrera=[]
    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__carrera=[]
    def __str__(self):
        return('{} {} {} {} {}').format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono)
    def CrearyAgregar(self,codi,nom,fechai,duracion,titulo):
        c=Carrera(codi,nom,fechai,duracion,titulo)
        self.__carrera.append(c)
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getCarrera(self):
        for p in self.__carrera:
            print('nombre:{} || duracion:{}'.format(p.getNombre(),p.getDuracion()))
    def getCarreras(self):
        return self.__carrera
    def getLocalidad(self):
        return self.__localidad
