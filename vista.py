from tkinter import StringVar
from tkinter import IntVar
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Frame
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Tk
from tkinter import Toplevel
from modelo import Abmc


class Vista:

    """ Clase Vista que administra la interfaz grafica modelada con Tkinter"""

    def __init__(self, ventana):
        """Se crea el objeto de la clase Abmc que administrara las altas, bajas, modificaciones y consultas
        Ademas, se establece la vista de la ventana principal de la app"""
        self.modelo = Abmc()
        self.modelo.crear_estructura()

        # Ventana madre
        self.root = ventana
        self.root.title("Agenda")

        # Variables de tkinter
        self.nombre = StringVar()
        self.mail = StringVar()
        self.numero = StringVar()
        self.id_contacto = IntVar()

        # Frames para lograr la transición entre ventanas
        self.ventana_inicio = Frame(self.root)
        self.lista_contactos = Frame(self.root)

        # Widgets de la ventana de ventana_inicio
        self.cabecera = Label(
            self.ventana_inicio, text="AGENDA", bg="black", fg="white"
        )

        self.cabecera.grid(row=0, column=0, columnspan=3, padx=1, sticky="nsew")

        self.ingreso = Label(
            self.ventana_inicio,
            text="Ingrese los datos de su contacto",
            bg="purple",
            fg="white",
        )

        self.ingreso.grid(row=1, column=0, columnspan=3, padx=1, sticky="nsew")

        # Formulario de ingreso de contactos
        self.etiqueta_nombre = Label(self.ventana_inicio, text="Nombre: ")

        self.etiqueta_nombre.grid(row=2, column=0, pady=5, sticky="nsew")

        self.entrada_nombre = Entry(self.ventana_inicio, textvariable=self.nombre)

        self.entrada_nombre.grid(row=2, column=1, pady=5, sticky="nsew")

        self.etiqueta_numero = Label(self.ventana_inicio, text="Numero de teléfono: ")

        self.etiqueta_numero.grid(row=3, column=0, pady=5, sticky="nsew")

        self.entrada_numero = Entry(self.ventana_inicio, textvariable=self.numero)

        self.entrada_numero.grid(row=3, column=1, pady=5, sticky="nsew")

        self.etiqueta_mail = Label(self.ventana_inicio, text="Mail: ")

        self.etiqueta_mail.grid(row=4, column=0, pady=5, sticky="nsew")

        self.entrada_mail = Entry(self.ventana_inicio, textvariable=self.mail)

        self.entrada_mail.grid(row=4, column=1, pady=5, sticky="nsew")

        self.boton_ingresar = Button(
            self.ventana_inicio,
            text="Guardar contacto",
            bg="black",
            fg="white",
            borderwidth=0,
            padx=15,
            command=lambda: self.alta(
                self.nombre.get(),
                self.mail.get(),
                self.numero.get(),
            ),
        )

        self.boton_ingresar.grid(row=5, column=1, pady=5)

        self.boton_contactos = Button(
            self.ventana_inicio,
            text="Mis contactos",
            bg="black",
            fg="white",
            borderwidth=0,
            padx=15,
            command=self.mostrar_contactos,
        )

        self.boton_contactos.grid(row=5, column=0, pady=5)

        # Por defecto, la aplicacion, mostrará la ventana de inicio
        self.ventana_inicio.pack()

        # Función encargada de "cargar" y posicionar los widgets de la pantalla de contactos
        self.configurar_lista_contactos()

    def configurar_lista_contactos(self):

        """Se establece la ventana donde se mostará la lista de contactos, junto con los botones de atrás,
        modificar y eliminar contacto"""

        self.lista_contactos.config(bg="maroon4")
        self.botones_laterales = Frame(self.lista_contactos, bg="maroon4")
        self.contenedor_contactos = Frame(self.lista_contactos)
        self.columnas = Frame(self.contenedor_contactos)
        self.tabla_contactos = Frame(self.contenedor_contactos)

        cabecera_lista = Label(
            self.columnas, text="Lista de contactos", bg="black", fg="white"
        )

        cabecera_lista.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Etiquetas de columnas
        col_id = Label(self.columnas, text=" Id ", bg="purple", fg="white", width=22)

        col_id.grid(row=1, column=0, sticky="nsew")

        col_nombre = Label(
            self.columnas, text=" Nombre ", bg="purple", fg="white", width=22
        )

        col_nombre.grid(row=1, column=1, sticky="nsew")

        col_numero = Label(
            self.columnas,
            text=" Numero de teléfono ",
            bg="purple",
            fg="white",
            width=22,
        )

        col_numero.grid(row=1, column=2, sticky="nsew")

        col_mail = Label(
            self.columnas,
            text=" Dirección de e-mail ",
            bg="purple",
            fg="white",
            width=23,
        )

        col_mail.grid(row=1, column=3, sticky="nsew")

        self.actualizar_contactos()

        atras = Button(
            self.botones_laterales,
            text="Atrás",
            bg="black",
            fg="white",
            command=self.mostrar_inicio,
            height=2,
        )

        atras.grid(row=0, column=0, sticky="nsew", pady=5)

        eliminar = Button(
            self.botones_laterales,
            text="Eliminar contacto",
            bg="red",
            fg="white",
            height=2,
            command=self.borrar_contacto,
        )

        eliminar.grid(row=1, column=0, sticky="nsew", pady=5)

        modificar = Button(
            self.botones_laterales,
            text="Editar un contacto",
            bg="blue",
            fg="white",
            command=self.modificar_contacto,
        )
        modificar.grid(row=2, column=0, sticky="nsew", pady=5)

        self.columnas.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.tabla_contactos.grid(row=1, column=1, sticky="nsew")

        self.contenedor_contactos.grid(row=0, column=0)

        self.botones_laterales.grid(row=0, column=1, padx=10)

    def mostrar_contactos(self):

        """En este metodo se realiza la transicion de la ventana de inicio a la
        pantalla de la lista de contactos"""

        # Se deja de mostrar la ventana de inicio
        self.ventana_inicio.pack_forget()
        # Se muestra la lista de contactos
        self.lista_contactos.pack()

    def mostrar_inicio(self):

        """En este metodo se realiza la transicion de la pantalla de la lista de contactos a
        la ventana de inicio"""

        # Se deja de mostrar la lista de contactos
        self.lista_contactos.pack_forget()
        # Se muestra la ventana de inicio
        self.ventana_inicio.pack()

    def borrar_contacto(self):

        """En este metodo se lanza una ventana emergente para solicitar la ID del
        contacto que se desea eliminar, y posteriormente se elimina si es posible"""

        # Cartel emergente para solicitar el id del contacto a eliminar
        self.id_contacto = simpledialog.askstring(
            "Eliminar contacto", "Ingrese el ID del contacto que desea eliminar: "
        )

        # Se utiliza el modulo de la base de datos para saber si existe el contacto en la bdd
        try:
            existe = self.modelo.verificar_existencia(self.id_contacto)
        except:
            messagebox.showerror("Excepción: ID nula", "No se ha introducido ningún ID")
        else:
            if existe:
                # Se elimina momentaneamente la tabla
                self.tabla_contactos.grid_forget()

                for fila in self.tabla_contactos.winfo_children():
                    fila.destroy()

                # Se le dice al modulo de la bdd que elimine el contacto con el id
                self.modelo.borrar_contacto(self.id_contacto)
                print("Contacto eliminado correctamente")
                # Se vuelve a mostrar pero actualizada
                self.actualizar_contactos()

                self.columnas.grid(row=0, column=0, columnspan=4, sticky="nsew")

                self.tabla_contactos.grid(row=1, column=1, sticky="nsew")

                self.contenedor_contactos.grid(row=0, column=0)
            elif existe == False:
                # Si no existe el contacto se muestra el error
                messagebox.showerror(
                    "Contacto inexistente",
                    "El contacto con el ID ingresado no existe, ingreselo nuevamente",
                )
            else:
                print("Se ha cerrado la ventana sin introducir ninguna ID")

    def alta(self, nombre, mail, numero):

        """  En este metodo se le solicita un alta de un contacto al modelo"""

        if self.modelo.insertar_contacto(nombre, mail, numero):

            print("Se registro exitosamente un contacto.")
            self.actualizar_contactos()

            # "Limpia" los inputs
            self.nombre.set("")
            self.numero.set("")
            self.mail.set("")

        else:
            messagebox.showerror(
                "Error",
                "No se pudo registrar el contacto, verifique que el formato de los campos sean correctos y que no estén vacíos",
            )

    def actualizar_contactos(self):

        """En este metodo se actualiza la lista de contactos para ver reflejadas los cambios que se hagan
        en la interfaz grafica"""

        # Posición inicial de fila/columna
        fila = 2
        columna = 0

        # Recupero todos los contactos
        tuplas_contactos = self.modelo.obtener_contactos()

        # Para cada contacto de la tupla recuperada
        for contacto in tuplas_contactos:
            # Para cada valor de la tupla recuperada
            for elemento in contacto:
                # Se crea una etiqueta
                self.etiqueta_elemento = Label(
                    self.tabla_contactos,
                    text=f"{elemento}",
                    bg="grey",
                    width=20,
                    padx=10,
                )
                # Se posiciona
                self.etiqueta_elemento.grid(row=fila, column=columna, sticky="nsew")

                columna += 1
            fila += 1
            columna = 0

    def modificar_contacto(self):

        """En este metodo se lanza una ventana emergente para solicitar el ID de un contacto
        para el que se desee modificar uno o todos sus datos"""

        # Se crea una nueva ventana emergente para tomar los datos
        nuevaVentana = Toplevel(self.root)
        nuevaVentana.title("Modificar contacto")
        nuevaVentana.geometry("320x380")
        nuevaVentana.config(bg="maroon4")

        e_id = Label(
            nuevaVentana,
            text="Ingrese el ID del contacto que quiere modificar: ",
            bg="black",
            fg="white",
        )

        e_id.grid(row=0, column=0)

        # Entry para solicitar el ID
        entrada_id = Entry(nuevaVentana, textvariable=self.id_contacto)

        entrada_id.grid(row=1, column=0, pady=5)

        boton_buscar = Button(
            nuevaVentana,
            bg="black",
            text="Buscar",
            fg="white",
            padx=10,
            command=lambda: self.mostrar_contacto(entrada_id.get(), nuevaVentana),
        )

        boton_buscar.grid(row=2, column=0, pady=5)

    def mostrar_contacto(self, id, ventana):

        """En este metodo se muestran los datos del contacto que se desea modificar en
        campos de texto editables para que se puedan modificar"""

        # Se pregunta a la base de datos si existe el contacto
        existe = self.modelo.verificar_existencia(id)

        if existe:
            contacto = self.modelo.obtener_contacto(id)

            # Se recuperan los dato de la tupla obtenida
            nombre_contacto = contacto[0][1]
            numero_contacto = contacto[0][2]
            mail_contacto = contacto[0][3]

            # Se muestra los campos para editar el contacto
            entrada_nombre = Entry(ventana, textvariable=self.nombre)
            entrada_numero = Entry(ventana, textvariable=self.numero)
            entrada_mail = Entry(ventana, textvariable=self.mail)

            self.nombre.set(nombre_contacto)
            self.numero.set(numero_contacto)
            self.mail.set(mail_contacto)

            entrada_nombre.grid(row=3, column=0, pady=5)

            entrada_numero.grid(row=4, column=0, pady=5)

            entrada_mail.grid(row=5, column=0, pady=5)

            modificar = Button(
                ventana,
                text="Modificar contacto",
                padx=10,
                command=lambda: self.modificar_bdd(
                    id,
                    entrada_nombre.get(),
                    entrada_numero.get(),
                    entrada_mail.get(),
                ),
                bg="black",
                fg="white",
            )

            modificar.grid(row=6, column=0, pady=5)

        # Si no existe se muestra un cartel de error
        elif existe == False:
            messagebox.showerror(
                "Contacto inexistente",
                "El contacto con el ID ingresado no existe, ingreselo nuevamente",
            )
        # En caso de que se capture una excepción
        else:
            print("No se ha introducido ninguna ID")

    def modificar_bdd(self, id, nombre_contacto, numero_contacto, mail_contacto):

        """En este metodo se le solicita al modelo la modificacion de un contacto"""

        if self.modelo.modificar_contacto(
            nombre_contacto, numero_contacto, mail_contacto, id
        ):
            self.actualizar_contactos()
            # Se vacían los campos
            self.nombre.set("")
            self.numero.set("")
            self.mail.set("")
            print("Base de datos actualizada")
        else:
            messagebox.showerror(
                "Error",
                "Campos inválidos, verifique que estén bien escritos y no estés vacíos",
            )
