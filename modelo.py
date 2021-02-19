from validaciones import Validar
import sqlite3


class Abmc:

    """Clase ABMC donde se produce la creacion y conexión a la base de datos, junto con
    la logica de las consultas, altas, bajas y modificaciones."""

    def __init__(self):

        """Inicializador de la clase Abmc, se crea la conexión y el cursor de la base de datos,
        además se instancia el objeto encargado de las validaciones de los campos de la app"""

        self.validaciones = Validar()
        # Conexión y creación de base de datos.
        self.conexion = sqlite3.connect("mis_contactos.db")
        self.cursor = self.conexion.cursor()

    def crear_estructura(self):
        """Se crea la tabla de la base de datos"""
        self.cursor.execute(
            """ CREATE TABLE IF NOT EXISTS contactos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre VARCHAR(20) NOT NULL,
                            telefono VARCHAR(14) NOT NULL,
                            mail VARCHAR(36) NOT NULL)"""
        )

    def obtener_contactos(self):
        """En este metodo se obtienen todos los contactos guardados en la base de datos"""
        consulta_contactos = self.cursor.execute("SELECT * FROM contactos")
        tuplas_contactos = self.cursor.fetchall()
        return tuplas_contactos

    def obtener_contacto(self, id):
        """En este metodo se obtiene el contacto con la id recibida como parametro."""
        sql = f"SELECT * FROM contactos WHERE id={id}"
        self.cursor.execute(sql)
        contacto = self.cursor.fetchall()
        return contacto

    def insertar_contacto(self, nombre, mail, numero):

        """En este metodo se inserta un nuevo contacto en la base de datos que tendra
        el nombre, mail y numero recibidos como parametros. Ademas, se verifica que los
        datos recibidos cumplan con el formato correspondiente."""

        registro_exitoso = True

        # Se verifica si algun campo está vacío
        if self.validaciones.verificar_vacio(nombre, mail, numero):
            registro_exitoso = False
        # Si ningun campo está vacío se valida mediante RegEx
        elif (
            not self.validaciones.validar_nombre(nombre)
            or not self.validaciones.validar_numero(numero)
            or not self.validaciones.validar_mail(mail)
        ):
            # Si alguno de los tres campos no es validado correctamente, entonces falla el registro
            registro_exitoso = False
        else:
            sql = (
                f"INSERT INTO contactos VALUES (null, '{nombre}', '{numero}', '{mail}')"
            )
            self.cursor.execute(sql)
            self.conexion.commit()

        return registro_exitoso

    def verificar_existencia(self, id):

        """En este metodo se verifica si existe en la base de datos el contacto con id recibida
        como parametro"""

        existe = False
        sql = f"SELECT COUNT(1) FROM contactos WHERE id={id}"

        try:
            self.cursor.execute(sql)
        except sqlite3.OperationalError:
            print("¡ADVERTENCIA!")
            existe = None
        else:
            resultado = self.cursor.fetchall()
            if resultado[0][0] == 1:
                existe = True

        return existe

    def borrar_contacto(self, id):

        """En este metodo se borra el contacto con id recibida por parametro de la base de datos"""

        sql = f"DELETE FROM contactos WHERE id={id}"
        self.cursor.execute(sql)
        self.conexion.commit()

    def modificar_contacto(self, nombre, numero, mail, id):

        """En este metodo se modifican los datos del contacto con id recibida por parametro."""

        modificacion_exitosa = True

        # Verificacion para saber si están vacíos
        if self.validaciones.verificar_vacio(numero, nombre, mail):
            modificacion_exitosa = False
        # Primero verifica que no estén vacios los campos para validarlos
        elif (
            not self.validaciones.validar_mail(mail)
            or not self.validaciones.validar_numero(numero)
            or not self.validaciones.validar_nombre(nombre)
        ):
            modificacion_exitosa = False
        else:
            sql = f"UPDATE contactos SET nombre='{nombre}', telefono='{numero}', mail='{mail}' WHERE id={id}"
            self.cursor.execute(sql)
            self.conexion.commit()

        return modificacion_exitosa
