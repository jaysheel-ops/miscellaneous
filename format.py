from PIL import Image
import os

def convert_images_to_png():
    current_folder = os.getcwd()
    image_files = [f for f in os.listdir(current_folder) if os.path.isfile(os.path.join(current_folder, f)) and f.lower().endswith(('.jpg', '.jpeg', '.bmp', '.gif', '.tiff', 'jfif', 'webp'))]

    for image_file in image_files:
        # Open the image
        image_path = os.path.join(current_folder, image_file)
        img = Image.open(image_path)

        # Convert and save as PNG
        png_path = os.path.splitext(image_path)[0] + ".png"
        img.save(png_path, "PNG")

        # Optionally, you can delete the original image file if needed
        # os.remove(image_path)

def convert_png_to_jpg():
    current_folder = os.getcwd()
    png_files = [f for f in os.listdir(current_folder) if os.path.isfile(os.path.join(current_folder, f)) and f.lower().endswith('.png')]

    for png_file in png_files:
        # Open the PNG image
        png_path = os.path.join(current_folder, png_file)
        img = Image.open(png_path)

        # Convert and save as JPG
        jpg_path = os.path.splitext(png_path)[0] + ".jpg"
        img.convert("RGB").save(jpg_path, "JPEG")

        # Optionally, you can delete the original PNG image file if needed
        # os.remove(png_path)
