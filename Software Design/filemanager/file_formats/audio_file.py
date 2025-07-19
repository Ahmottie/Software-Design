import pydub

from .base import FileAbstraction

class AudioFile(FileAbstraction):
    def read(self):
        self.audio = pydub.AudioSegment.from_file(self.file_path)
        return self.audio

    def edit(self, operation, *args):
        if operation == "change_speed":
            speed = args[0]
            self.edited_audio = self.audio.speedup(playback_speed=speed)

    def write(self, output_path=None):
        if output_path:
            self.edited_audio.export(output_path, format="wav")
        else:
            self.edited_audio.export(self.file_path, format="wav")
