from tkinter import Tk
from lib.functions import set_window_center
from controller.homeController import HomeController
from model.homeModel import HomeModel
from view.homeView import HomeView


class App(Tk):
    def __init__(self):
        super().__init__()

        self.controller = None
        self.view = None
        self.config()

        self.mainloop()

    def config(self):
        self.title('Hardwalien')
        set_window_center(self, 800, 480)
        self.resizable(False, False)
        self.init_home()

    def set_page(self):
        pass

    def init_home(self):
        self.view = HomeView(self)
        self.controller = HomeController(HomeModel, self.view)
        self.view.set_controller(self.controller)
        self.view.place(x=0, y=0, relwidth=1, relheight=1)


if __name__ == '__main__':
    app = App()
