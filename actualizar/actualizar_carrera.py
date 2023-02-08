cliente = MongoClient('localhost:27017')

db = Carrera.TiendaInformatica

def update():

    try:
        criteria = input ("\n Ingrese los datos para actualizar actualizar \n")

        id = input("Ingrese su id:")
        nombres = input("Ingrese sus nombres correctos:")
        descripcion = input("Ingrese su descripcion")

        db.Estudiantes.update.one(
           {"_id":criteria },
           {
             "$set":{"id" : id,
                 "nombres": nombres,
                 "descripcion" : descripcion,
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
