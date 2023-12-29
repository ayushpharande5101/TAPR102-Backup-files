import requests
from PIL import Image
from io import BytesIO

def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def display_image(img):
    img.show()

url = 'https://github.com/ayushpharande5101/GUI/blob/main/CTPL2.png'
image = load_image_from_url(url)
display_image(image)