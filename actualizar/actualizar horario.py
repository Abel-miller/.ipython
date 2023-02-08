cliente = MongoClient('localhost:27017')

db = Horario.TiendaInformatica

def update():
    try:
        criteria = input ("\n Ingrese los datos para actualizar actualizar \n")

        id = input("Ingrese su id:")
        fecha = input("Ingrese su fecha:")
        hora_inicio = input("Ingrese su hora de inicio")
        hora_salida = input("Ingrese su horario de salida")
        detalle_actividad = input("Ingrese su detalle de actividad")
        

        db.Estudiantes.update.one(
           {"_id":criteria },
           {
             "$set":{"id" : id,
                 "fecha" : fecha,
                 "hora_inicio" : hora_inicio,
                 "hora_salida" : hora_salida,
                 "detalle_actividad": detalle_actividad, 
                }
            }
        )

        print("""¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡
                Registro actualizado correctamente
                ???????????????????????????????????
             """)

    except ImportError:
     platform_specific_module = None
    print(str(e))
