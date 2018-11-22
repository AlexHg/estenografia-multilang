from PIL import Image

imagen = Image.open("salida1.png") # Aquí puedes cambiar el nombre de la imagen
pixeles = imagen.load()

tamaño = imagen.size
anchura = tamaño[0]
altura = tamaño[1]

for x in range(anchura):
	for y in range(altura):
		pixel = pixeles[x, y]

		rojo = pixel[0]
		verde = pixel[1]
		azul = pixel[2]

		print("Rojo: {}".format(rojo))
		print("Verde: {}".format(verde))
		print("Azul: {}".format(azul))