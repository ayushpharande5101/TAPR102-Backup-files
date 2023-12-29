import os

# Get the current script's directory
script_dir = os.path.dirname(__file__)

# Specify the relative path to the image
image_path = os.path.join(script_dir, 'CTPL', 'CTPL2.png')

print(image_path)

# Now you can use 'image_path' to reference the image in your code
