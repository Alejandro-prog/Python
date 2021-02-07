
from PIL import Image
import pandas as pd

def escala_de_grises(im):
    #ruta = (im)
    #im = Image.open(ruta)
    im.show()
    im2 = im
    i = 0
    while i < im2.size[0]:
        j = 0
        while j < im2.size[1]:
            r, g, b = im2.getpixel((i,j))
            g = (r + g + b) / 3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            im2.putpixel((i,j), pixel)
            j+=1
        i+=1
    im2.show()
    
    from __future__ import division   # impone aritmética no entera en la división
from PIL import Image             # funciones para cargar y manipular imágenes
import numpy as np                # funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   # funciones para representación gráfica


%matplotlib inline
I = Image.open("C:/Users/fgonzalez/Pictures/Firma.jpg")
I.show()
plt.imshow(np.asarray(I))
plt.show()


from google.colab import files
from IPython.display import Image

uploaded = files.upload()

print(uploaded)
Image('naruto.jpg', width = 500)

from PIL import Image

def escala_de_grises(im):
    ruta = ("/home/Desktop/" + im)
    im = Image.open(ruta)
    im.show()
    im2 = im
    i = 0
    while i < im2.size[0]:
        j = 0
        while j < im2.size[1]:
            r, g, b = im2.getpixel((i,j))
            g = (r + g + b) / 3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            im2.putpixel((i,j), pixel)
            j+=1
        i+=1
    im2.show()
    
pd.

escala_de_grises("naruto.jpg")

escala_de_grises(uploaded)
