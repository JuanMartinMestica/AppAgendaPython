from tkinter import Tk
from vista import Vista


class Controlador:

    """ Clase del controlador, activa la vista y pone a andar la app"""

    def __init__(self, root):

        """'root' debe ser la ventana madre Tk() de Tkinter, se instancia el controlador
        y se activa la vista"""

        self.root_controler = root
        self.activar_vista()

    def activar_vista(self):
        """ Se envía a la vista la ventana principal"""
        Vista(self.root_controler)


if __name__ == "__main__":
    root_tk = Tk()
    aplicacion = Controlador(root_tk)
    root_tk.mainloop()
