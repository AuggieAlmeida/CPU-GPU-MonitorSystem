from model import cpuModel, gpuModel, ramModel


class HomeModel:
    def __init__(self):
        self.gpu = gpuModel.show()
