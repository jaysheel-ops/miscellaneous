from PIL import Image
import os

def convert_and_rename_images(input_dir, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all files in the input directory
    files = os.listdir(input_dir)

    # Counter for renaming images
    counter = 1

    # Iterate through each file in the directory
    for file_name in files:
        if file_name == "main.py" or file_name == "./main.py":
            continue
        # Construct the full path of the input file
        input_path = os.path.join(input_dir, file_name)

        # Check if the file is an image (you may want to add more file format checks)
        if os.path.isfile(input_path) and not file_name.lower().endswith('.png'):
            # Open the image using Pillow
            img = Image.open(input_path)

            # Construct the full path of the output file with a new name and .png extension
            output_name = f"image_{counter}.png"
            output_path = os.path.join(output_dir, output_name)

            # Save the image in PNG format
            img.save(output_path, format='PNG')

            # Increment the counter for the next image
            counter += 1

            # Optional: Close the image file
            img.close()

            # Remove the original file (optional, comment out if you want to keep the original files)
            os.remove(input_path)

    print(f"Conversion and renaming complete. {counter - 1} images processed.")

# Specify the input and output directories
input_directory = "./"
output_directory = "./"

# Call the function to convert and rename images
convert_and_rename_images(input_directory, output_directory)