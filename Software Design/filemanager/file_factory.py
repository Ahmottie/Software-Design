from abc import ABC, abstractmethod

from file_formats import TextFile, ImageFile, AudioFile


class FileFactoryAbstraction(ABC):
    @staticmethod
    @abstractmethod
    def create_text_file(file_path):
        pass

    @staticmethod
    @abstractmethod
    def create_audio_file(file_path):
        pass    

    @staticmethod
    @abstractmethod
    def create_image_file(file_path):
        pass


class FileFactory(FileFactoryAbstraction):
    @staticmethod
    @abstractmethod
    def create_text_file(file_path):
        return TextFile(file_path)

    @staticmethod
    @abstractmethod
    def create_audio_file(file_path):
        return AudioFile(file_path)    

    @staticmethod
    @abstractmethod
    def create_image_file(file_path):
        return ImageFile(file_path)
