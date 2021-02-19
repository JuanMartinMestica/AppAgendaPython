import re


class Validar:

    """Clase Validar donde se realizan todas las validaciones de los campos
    de la App, para asegurar la consistencia de los datos"""

    def __init__(self):

        """Inicializador de la clase Validar, se crean los patrones que se deben respetar"""

        self.patron_numero = re.compile("^[0-9]{6,12}$")
        self.patron_nombre = re.compile("^[a-zA-z áéíóú]{2,20}$")
        self.patron_mail = re.compile(
            "^[a-zA-Z0-9_-]+@[a-zA-Z]+\.[a-z]{2,6}(\.[a-z]{2,6})*$"
        )

    def verificar_vacio(self, numero, nombre, mail):

        """En este método, se verifica si algún campo esta vacío y se retorna
        verdadero o falso según corresponda"""

        campo_vacio = False

        # Si existe algún campo vacío entonces retornará verdadero.
        if not numero or not nombre or not mail:
            campo_vacio = True

        return campo_vacio

    def validar_numero(self, numero):

        """En este metodo se verifica que el numero tenga el formato correspondiente,
        es decir, que solo contenga números y una longitud entre 6 y 12 caracteres"""

        numero_string = str(numero)

        esValido = False

        resultado = self.patron_numero.match(numero_string)

        if resultado:
            esValido = True

        return esValido

    def validar_nombre(self, nombre):

        """En este metodo se verifica que el nombre tenga el formato correspondiente,
        es decir que solo contenga letras sin numeros ni caracteres especiales y una
        longitud entre 2 y 20 caracteres"""

        esValido = False

        resultado = self.patron_nombre.match(nombre)

        if resultado:
            esValido = True
        return esValido

    def validar_mail(self, mail):

        """En este metodo se valida el mail para verificar que tenga el formato correspondiente,
        puede estar compuesto por numeros, letras y caracteres especiales, luego un "@" obligatoriamente
        un dominio solo compuesto por letras y luego un punto seguido de la terminacion del dominio"""

        esValido = False

        resultado = self.patron_mail.match(mail)

        if resultado:
            esValido = True

        return esValido