from .base import FileAbstraction


class TextFile(FileAbstraction):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def edit(self, new_content):
        self.new_content = new_content

    def write(self, output_path=None):
        if output_path:
            with open(self.output_path, 'w') as file:
                file.write(self.new_content)
        else:
            with open(self.file_path, 'w') as file:
                file.write(self.new_content)
