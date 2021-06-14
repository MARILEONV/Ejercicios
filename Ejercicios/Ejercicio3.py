class Datos:
    instancia = 0
    def __init__(self, texto ='Comienzo'):
        self.palabras = texto

    def Detalles(self):
        nombres = 'María León'
        edad, peso = 19, 50
        sexo = 'F'
        civil = True
        # TUPLAS
        usuario = ()
        usuario = ('María', 1234, 'marileon.melv@gmail.com', True)
        # usuario[3] = 'Milagro'
        # lISTAS
        materias = []
        materias = ['Programacion', 'POO']
        materias[1] = 'Python'
        materias.append('Go')
        # DICCIONARIOS
        docente = {}
        docente = {'nombre':'Daniel', 'edad':50, 'fac':'faci'}
        docente['carrera'] = 'cs'
        # presentacion con format
        print('Mi nombre es{} y tengo{} años'.format(nombres, edad))
        print(usuario, materias, docente)
        print(usuario,usuario[0], usuario[0:2],usuario[-1])
        print(materias,materias[2:],materias[:1],materias[::],materias[-2:])
        print(docente,docente['nombre'])

info = Datos()
info.Detalles()
print(info.palabras)
