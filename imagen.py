from PIL import Image

basewidth = 300
img = Image.open('game/sources/sprites/salto.png')
#box = (10, 100, 500, 900)
#1920 / 96 = 20
#Escala a 20
#800 x 400

img = img.resize((120,108), Image.ANTIALIAS)
img.save('background1.png')
