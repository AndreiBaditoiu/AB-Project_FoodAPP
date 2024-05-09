from PIL import Image


img=Image.open("Logo.webp")

img.save("Logo.jpg", "JPEG")


def convert_jpeg_to_ico(source_path, target_path, sizes=None):
    if sizes is None:
        sizes = [(32, 32)]
    with Image.open(source_path) as img:
        img.save(target_path, format='ICO', size=sizes)


source_jpeg_path = r'C:\\Users\Andrei Baditoiu\OneDrive\Desktop\Final Project\mysite\food\static\Images'
target_ico_path = r'C:\\Users\Andrei Baditoiu\OneDrive\Desktop\Final Project\mysite\food\static\Images\favicon'

convert_jpeg_to_ico(source_jpeg_path, target_ico_path)
