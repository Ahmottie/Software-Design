from abc import abstractmethod, ABC

class FileAbstraction(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def edit(self, *args, **kwargs):
        pass

    @abstractmethod
    def write(self, output_path=None):
        pass
