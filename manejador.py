import csv
from facultad import Facultad
from carrera import Carrera
class ManejaFacultades:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def LeerArchivo(self):
        contador=0
        archivo=open("Facultades.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            if(contador<int(fila[0])):
                contador=int(fila[0])
                facu=Facultad(contador,fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(facu)
            else:
                self.__lista[contador-1].CrearyAgregar(fila[1],fila[2],fila[3],fila[4],fila[5])
    def Busca(self,elemento):
        i=0
        while( i<len(self.__lista) and elemento!=self.__lista[i].getCodigo() ):
            i+=1
        return i
    def BuscarFacultad(self):
        codi=int(input('Ingrese codigo de Facultad:'))
        i=self.Busca(codi)
        if(i<len(self.__lista)):
            print('----------------Facultad----------------')
            print('nombre:{}'.format(self.__lista[i].getNombre()))
            print('----------------Carreras----------------')
            self.__lista[i].getCarrera()
    def BuscaCarrera(self):
        carre=input('Ingrese nombre de una carrera:')
        i=0

        band=True
        carrera=[]
        while(i<len(self.__lista) and band):
            carrera=self.__lista[i].getCarreras()
            j=0
            while(j<len(carrera) and carre!=carrera[j].getNombre()):
                j+=1
            if(j<len(carrera) and carre==carrera[j].getNombre()):
                band=False
            else: i+=1
        if i<len(self.__lista):
            print('codigo:{}.{}'.format(self.__lista[i].getCodigo(),self.__lista[i].getCarreras()[j].getCodigoC()))
            print('----------------Facultad----------------')
            print('nombre:{} || localidad:{}'.format(self.__lista[i].getNombre(), self.__lista[i].getLocalidad()))
        else: print('carrera no econtrada')
