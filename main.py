from menu import Menu
from manejador import ManejaFacultades
if __name__=='__main__':
    menu=Menu()
    manejador=ManejaFacultades()
    salir=False
    band=0
    while not salir:
        print('------------------------------------------')
        print('1.Ingrese codigo de una facultad y mostrar nombre y carreras')
        print('2.Ingrese nombre de una carrera y muestra codigo, nombre y localidad de la facultad')
        print('3.Salir')
        op=input('->')
        print('------------------------------------------')
        if band != -1:
                manejador.LeerArchivo()
                print('archivo leido')
                band=-1
        menu.opcion(op,manejador)
        salir = op =='3'
