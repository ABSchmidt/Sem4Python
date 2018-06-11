from PIL import Image
import requests
from io import BytesIO
import os


def loadAndSaveImageFromWeb(url,filename):

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    path = os.path.join(os.getcwd(), filename + ".png")
    img.save(path)
    img.show()

loadImageFromWeb("https://www.rd.com/wp-content/uploads/2018/01/Burano_Amazing-Photos-of-Towns-with-Colorful-Houses-Around-the-World.jpg","colorful_houses")