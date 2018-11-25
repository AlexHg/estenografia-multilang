# pip install Pillow
from PIL import Image

finishFlag = "11111111"

def lastBit(byte):
	return byte[-1]

def intToBin(numero):
	return bin(numero)[2:].zfill(8)

def binToInt(binario):
	return int(binario, 2)

def asciiToChar(numero):
	return chr(numero)

def showText(imageRoute):
	imagen = Image.open(imageRoute)
	pixeles = imagen.load()

	imageSize = imagen.size
	imageWidth = imageSize[0]
	imageHeight = imageSize[1]

	byte = ""
	mensaje = ""

	for x in range(imageWidth):
		for y in range(imageHeight):
			pixel = pixeles[x, y]

			red = pixel[0]
			green = pixel[1]
			blue = pixel[2]
            
			byte += lastBit(intToBin(red))
			if len(byte) >= 8:
				if byte == finishFlag:
					break
				mensaje += asciiToChar(binToInt(byte))
				byte = ""

			byte += lastBit(intToBin(green))
			if len(byte) >= 8:
				if byte == finishFlag:
					break
				mensaje += asciiToChar(binToInt(byte))
				byte = ""

			byte += lastBit(intToBin(blue))
			if len(byte) >= 8:
				if byte == finishFlag:
					break
				mensaje += asciiToChar(binToInt(byte))
				byte = ""

			print("RGB ({},{},{})".format(red,green,blue))
		else:
			continue
		break
	return mensaje

mensaje = showText("wall_himno.png")
print("El mensaje oculto es:")
print(mensaje)