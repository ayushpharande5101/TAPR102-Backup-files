from PIL import Image
import os

def execute_image(image_path):
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the image
    image_full_path = os.path.join(current_directory, image_path)

    # Check if the image file exists
    if not os.path.isfile(image_full_path):
        print(f"Image file '{image_path}' not found.")
        return

    # Open and display the image
    img = Image.open(image_full_path)
    img.show()

# Replace "your_image.jpg" with the actual filename of your image
execute_image("CTPL2.png")

