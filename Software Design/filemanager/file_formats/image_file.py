from PIL import Image

from .base import FileAbstraction

class ImageFile(FileAbstraction):
    def read(self):
        self.image = Image.open(self.file_path)
        return self.image

    def edit(self, operation="crop", **kwargs):
        if operation == "crop":
            box = kwargs["size"]
            self.edited_image = self.image.crop(box)  # box should be a tuple (left, upper, right, lower)
    
    def write(self, output_path=None):
        if output_path:
            self.edited_image.save(self.output_path)
        else:
            self.edited_image.save(self.file_path)
