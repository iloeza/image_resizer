from PIL import Image
import sys

class Photo:
    
    allowed_formats = ["jpg", "png", "jpeg"]

    def __init__(self, image_path, output_dir, quality = 100,  basewidth = 750) -> None:
        self.__image_path = image_path
        self.__output_dir = output_dir
        self.__basewidth = basewidth
        self.__quality = quality
        self.__image_name = self.format_image_name()[0]
        self.__image_type = self.format_image_name()[1]
        self.__image = Image.open(self.__image_path)
    
    def format_image_name(self):
        return self.__image_path.split("/")[-1].split(".")

    def get_new_hight(self):
        # A little something borrowed from https://stackoverflow.com/a/451580
        basewidth = 750
        width_percent = basewidth / float(self.__image.size[0])
        return int((float(self.__image.size[1]) * float(width_percent)))

    def validate_image_type(self):
        if self.__image_type not in self.allowed_formats:
            raise TypeError("Invalid image format, only JPG and PNG allowed")            

    def resized_image(self):
        new_hight = self.get_new_hight()
        self.__image = self.__image.resize((self.__basewidth, new_hight))

    def save_image(self):
        output = f"{self.__output_dir}/{self.__image_name}.{self.__image_type}"
        self.__image.save(output, quality=self.__quality, optimize=True)


if __name__ == "__main__":

    image = Photo(sys.argv[1], sys.argv[2], 90, 750)
    image.validate_image_type()
    image.resized_image()
    image.save_image()
