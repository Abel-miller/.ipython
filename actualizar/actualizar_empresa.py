cliente = MongoClient('localhost:27017')

db = Empresa.TiendaInformatica

def update():
    try:
        criteria = input ("\n Ingrese los datos para actualizar actualizar \n")

        id = input("Ingrese su id:")
        nombres = input("Ingrese sus nombres correctos:")
        direccion = input("Ingrese su direccion")
        telefono =  input("Ingrese su telefono")
        correo_electronico = input("Ingrese su correo electronico")
        

        db.Estudiantes.update.one(
           {"_id":criteria },
           {
             "$set":{"id" : id,
                 "nombres": nombres,
                 "direccion" : direccion,
                 "telefono" : telefono,               
                 "correo_electronico": correo_electronico,
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
