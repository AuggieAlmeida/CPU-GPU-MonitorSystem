from tkinter import ttk


class HomeView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = None
        self.controller = None

        self.create_label("Teste", 20, 20, 200, 100)
        self.create_label("Teste 2", 20, 120, 200, 100)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def create_label(self, text, x, y, w, h):
        """

        :param text:
        :param x:
        :param y:
        :param w:
        :param h:
        :return:
        """
        self.label = ttk.Label(self, text=text)
        self.label.place(x=x, y=y, width=w, height=h)
