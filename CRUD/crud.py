import conexion

#acceder a la funcion conectar 
connect = conexion.conectar()

database = connect[0]
cursor = connect[1]

#************** Mostrar registros ***************
def mostrar():
    cursor.execute("Select * From Usuario")
    mostrar_todos = cursor.fetchall()

    for i in mostrar_todos:
        print(i)

#************** Insertar registros ***************
def insertar():
    sql = "insert into Usuario (email,username,edad) values (%s,%s,%s)"

    print("\n********Registro Usuario**********")
    email = input('Ingrese su email: ')
    username = input('Ingree su username: ')
    age =  int(input('Ingrese su edad: '))
    values =(email,username,age)

    cursor.execute(sql,values)

    database.commit()
    #print(cursor.rowcount)
    if cursor.rowcount == 1:
        print("Registro ingresado exitosamente")
    else:
        print("Ocurrio un error al ingresar")

#************** Actualizar registros ***************
def actualizar():
    sql = "update Usuario set email = %s where id =%s"

    email = input("Ingrese su nuevo email: ")
    id = int(input("Ingrese el id del usuario: "))
    values = (email,id)
    cursor.execute(sql, values)
    if cursor.rowcount == 1:
        print("Registro ingresado exitosamente")
        database.commit()
    else:
        print("Ocurrio un error al ingresar")


#************** Eliminar registros ***************
def eliminar():
    sql = "delete from Usuario where id = %s"
    id = int(input("Ingrese el id del usuario: "))
    values = (id, )
    cursor.execute(sql, values)
    if cursor.rowcount == 1:
        print("Registro ingresado exitosamente")
        database.commit()
    else:
        print("Ocurrio un error al ingresar")

#************** Buscar registros ***************
def buscarPorId():
    sql = "select * from Usuario where id = %s"
    id = int(input("Ingrese el id del usuario: "))
    values =(id, )
    cursor.execute(sql,values)
    registro = cursor.fetchone()

    #Validar si encuentra el registro
    if registro != None:
        print("\nUsuario encontrado:")
        print(registro)
    else:
        print("No encontrado")
    

def buscarPorNombre():
    sql = "select * from Usuario where username = %s"
    nombreUsuario = input("Ingrese el username del usuario: ")
    values =(nombreUsuario, )

    cursor.execute(sql,values)

    registro = cursor.fetchone()

    if registro != None:
        print("\nUsuario encontrado:")
        print(registro)
    else:
        print("No encontrado")
    
def buscarPorLetra():
    #param = "m"
    nombreUsuario = input("Ingrese la inicial del nombre a buscar: ")
    cursor.execute("SELECT username,edad FROM Usuario WHERE username LIKE %s ", ("%" + nombreUsuario + "%",))
    print("Resultado")
    resultado = cursor.fetchall()

    for j in resultado:
        print("Nombre:...",j[0])
        print("Edad:.....",j[1])
    
    

 