class Carrera:
    __codigo=0
    __nombre=''
    __fechai=0
    __duracion=0
    __titulo=''
    def __init__(self,codigo,nombre,fechai,duracion,titulo):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__fechai=fechai
        self.__duracion=duracion
        self.__titulo=titulo
    def __str__(self):
        return ('{} {} {} {} {}').format(self.__codigo,self.__nombre,self.__fechai,self.__duracion,self.__titulo)
    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
    def getCodigoC(self):
        return self.__codigo
