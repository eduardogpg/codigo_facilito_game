from PIL import Image

basewidth = 300
img = Image.open('coin.png')
#box = (10, 100, 500, 900)
#1920 / 96 = 20
#Escala a 20
#800 x 400

img = img.resize((340,200), Image.ANTIALIAS)
img.save('coin1.png')
