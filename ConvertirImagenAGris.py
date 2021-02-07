from PIL import Image

def escala_de_grises(im):
    ruta = ("C:/Users/aleja/OneDrive/Escritorio/PH/" + im)
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
    


escala_de_grises("imagen.jpg")

---------------------------------------------------------------------------------- 2 ----------------------------------------------------------------------------------------

