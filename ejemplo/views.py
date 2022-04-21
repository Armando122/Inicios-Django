from django.http import HttpResponse
import datetime
from django.template import Template, Context

"""
Página que muestra un mensaje de bienvenida y despedida al
usuario
Acceso: http://localhost:8000/saludo/
o
http://localhost:8000/despedida/
"""
#Primera vista
def saludo(request):
    nombre = "Arm"
    #Uso de plantillas
    doc_ext = open("/home/armando/Documentos/Dev_armando/Semestre_20222/Interfaces/laboratorio/ejercicio/ejemplo/ejemplo/plantillas/plantillaUno.html")

    plt = Template(doc_ext.read())

    doc_ext.close()

    #Recibe un diccionario (clave,valor)
    contexto = Context({"nombre_persona":nombre})

    doc = plt.render(contexto)

    return HttpResponse(doc)

"""
Método que devuelve HttpResponse con la despedida
"""
def despedida(request):
    return HttpResponse("Usted sigue pasado de peso pero nos vemos")


"""
Método que nos la da fecha y hora actuales
"""
def fecha(request):
    fecha_actual = datetime.datetime.now()

    #Cadena con respuesta y html incrustado
    documento = """<html>
    <body>
    <h1>
    fecha y hora actual %s
    </h1>
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)

"""
Método que recibe en url request y año
"""
def edad(request,anio):

    edad_actual = 22
    periodo = anio - 2019
    edad_futura = edad_actual + periodo
    htm = """<html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2>
    </body>
    </html>""" %(anio, edad_futura)

    return HttpResponse(htm)
