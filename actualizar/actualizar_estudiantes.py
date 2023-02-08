cliente = MongoClient('localhost:27017')

db = Estudiantes.TiendaInformatica

def update():
    try:
        criteria = input ("\n Ingrese los datos para actualizar actualizar \n")

        id = input("Ingrese su id:")
        nombres = input("Ingrese sus nombres correctos:")
        apellidos = input("Ingrese sus apellidos correctos")
        cedula = input("Ingrese la cedula")
        correo_institucional = input("Ingrese su correo institucional")
        direccion = input("Ingrese su direccion")
        telefono =  input("Ingrese su telefono")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento")

        db.Estudiantes.update.one(
           {"_id":criteria },
           {
             "$set":{"id" : id,
                 "nombres": nombres,
                 "apellidos" : apellidos,
                 "cedula" : cedula,
                 "correo_institucional": correo_institucional,
                 "direccion" : direccion,
                 "telefono" : telefono,
                 "fecha_nacimiento" : fecha_nacimiento,
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
