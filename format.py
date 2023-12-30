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

if __name__ == "__main__":
    convert_images_to_png()
