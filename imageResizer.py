from PIL import Image
import sys

allowed_formats = ["jpg", "png", "jpeg"]
image_fullname = sys.argv[1].split("/")[-1].split(".")
image_format = image_fullname[1]
image_name = image_fullname[0]
output_dir = sys.argv[2]

if image_format not in allowed_formats:
    raise TypeError("Image format invalid, only JPG and PNG allowed")

basewidth = 750
img = Image.open(sys.argv[1])
wpercent = basewidth / float(img.size[0])
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize))

img.save(f"{output_dir}/{image_name}.{image_format}", quality=80, optimize=True)
