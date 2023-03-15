class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.model.__init__(self)


