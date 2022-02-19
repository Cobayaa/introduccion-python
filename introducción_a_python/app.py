from calendar import TUESDAY
from fcntl import F_SEAL_SEAL


nombre = "juan"
cantidadMas = 12.1

diasDeLaSemana = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
dynamicList = ['grapes', 12.5,[0, 1]]
diasDeLaSemana[2]

print(diasDeLaSemana[2])
print(dynamicList[2][1])

esMayorEdad = False

persona = {
    'nombre': 'jean',
    'apellido': 'zambrano',
    'edad': 'sisa',
    'materias': ['BASES DE DATOS II, LEANGUAJE DE CUATA GENERACION'],
}




personas = [

    {
        'nombre': 'jean',
        'apellido': 'zambrano',
        'edad': 'sisa',
        'materias': ['BASES DE DATOS II', 'LEANGUAJE DE CUATA GENERACION'],
    },

    {
        'nombre': 'juan',
        'apellido': 'arteaga',
        'edad': 'sa',
        'materias': ['BASES DE DATOS I', 'LEANGUAJE Orientado a Objetos'],
    },

    {
        'nombre': 'jorge',
        'apellido': 'mora',
        'edad': '12',
        'materias': ['  redes I', 'gta san andreas'],
    }
]



#--------------------------------------------------condiciones--------------------------------------------------

esMayorEdad = True

if esMayorEdad==True:
    print("Es mayor de edad")
    print("esto hace parte del if")
else:
    print("No es mayor de edad")
    print("esto hace parte del else")



for per in esMayorEdad:
    print(per["nombre"])

nombrePresona ="Roberto"





print(nombrePresona[2])



