from PIL import Image
import sys
import argparse

class Photo:
    
    allowed_formats = ["jpg", "png", "jpeg"]

    def __init__(self, image_path, output_dir, *args, **kwargs) -> None:
        self.__image_path = image_path
        self.__output_dir = output_dir
        self.__basewidth = kwargs['basewidth']
        self.__quality = kwargs['quality']
        self.__image_name = self.format_image_name()[0]
        self.__image_type = self.format_image_name()[1]
        self.__image = Image.open(self.__image_path)
    
    def format_image_name(self):
        return self.__image_path.split("/")[-1].split(".")

    def get_new_hight(self):
        # A little something borrowed from https://stackoverflow.com/a/451580
        width_percent = self.__basewidth / float(self.__image.size[0])
        return int((float(self.__image.size[1]) * float(width_percent)))

    def validate_image_type(self):
        if self.__image_type not in self.allowed_formats:
            raise TypeError("Invalid image format, only JPG and PNG allowed")            

    def resize_image(self):
        new_hight = self.get_new_hight()
        self.__image = self.__image.resize((self.__basewidth, new_hight))

    def save_image(self):
        output = f"{self.__output_dir}/{self.__image_name}.{self.__image_type}"
        self.__image.save(output, quality=self.__quality, optimize=True)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Resize an image in size and quality"
    )
    parser.add_argument('image_path')
    parser.add_argument('output_directory')
    parser.add_argument('--quality', type=int, default=85, help="Define image's quality. Defaults to 85.")
    parser.add_argument('--basewidth', type=int, default=750, help="Define image's basewidth. Defaults to 750px.")
    args = parser.parse_args()

    image = Photo(args.image_path, args.output_directory, quality=args.quality, basewidth=args.basewidth)
    image.validate_image_type()
    image.resize_image()
    image.save_image()
