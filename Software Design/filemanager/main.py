from file_factory import FileFactory


def main():
    image_file = FileFactory.create_image_file("")
    image_file.edit(operation="crop", box=())
    image_file.write(output_path="")

    audio_file = FileFactory.create_audio_file("")
    audio_file.edit()
    audio_file.write()

    text_file = FileFactory.create_text_file("")
    text_file.edit(new_content="...")
    text_file.write()


if __name__ == "__main__":
    main()
