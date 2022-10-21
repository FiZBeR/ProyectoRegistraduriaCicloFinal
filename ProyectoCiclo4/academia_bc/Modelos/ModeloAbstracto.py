from abc import ABCMeta

class ModeloAbstracto(metaclass=ABCMeta):

    def __int__(self,data):
        for key, value in data.items():
            setattr(self, key, value)

            '''Se esta definiendo un modelo generico y un modelo de iniciacion '''