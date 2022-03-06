import mysql.connector
from mysql.connector import Error

class DAO():
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='recfacial'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
            
           
    def registrarUser(self, user):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO `registro` (`documento_user`, `fecha_user`) VALUES ('{0}', '{1}');"
                cursor.execute(sql.format(user[0], user[1]))
                self.conexion.commit()
                print("¡Login guardado con exito! \n")
                print(f"¡Bienvenido usuario! {user[0]} \n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
            
      