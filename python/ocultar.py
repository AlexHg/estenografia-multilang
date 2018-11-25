# pip install Pillow 
from PIL import Image
import math 

finishFlag = "11111111"

def getBitList(texto):
	lista = []
	for letra in texto:
		asciiChar = charToAscii(letra)
		binChar = intToBin(asciiChar)
		for bit in binChar:
			lista.append(bit)
	for bit in finishFlag:
		lista.append(bit)
	return lista

def charToAscii(caracter):
	return ord(caracter)

def intToBin(numero):
	return bin(numero)[2:].zfill(8)

def binToInt(binario):
	return int(binario, 2)

def lastBitChange(byte, nuevo_bit):
	return byte[:-1] + str(nuevo_bit)

def colorChange(originColor, bit):
	binColor = intToBin(originColor)
	modColor = lastBitChange(binColor, bit)
	return binToInt(modColor)

def hideText(mensaje, imageRouteIn, imageRouteOut="salida.png"):
	print("Ocultando mensaje: '{}'".format(mensaje))
	imagen = Image.open(imageRouteIn)
	pixeles = imagen.load()

	imageSize = imagen.size
	imageWidth = imageSize[0]
	imageHeight = imageSize[1]

	lista = getBitList(mensaje) #Crea una lista de bit a partir del mensaje ingresado 
	contador = 0
	longitud = len(lista)

	#Recorre los pixeles en la imagen
	for x in range(imageWidth):
		for y in range(imageHeight):
			if contador < longitud:
				pixel = pixeles[x, y]
				
				#obtiene valores RGB
				red = pixel[0]
				green = pixel[1]
				blue = pixel[2]

				if contador < longitud:
					modRed = colorChange(red, lista[contador])
					contador += 1
				else:
					modRed = red

				if contador < longitud:
					modGreen = colorChange(green, lista[contador])
					contador += 1
				else:
					modGreen = green

				if contador < longitud:
					modBlue = colorChange(blue, lista[contador])
					contador += 1
				else:
					modBlue = blue

				pixeles[x, y] = (modRed, modGreen, modBlue)

				print("RGB ({},{},{}) -> mRGB ({},{},{}) ".format(red,green,blue,modRed,modGreen,modBlue))
			else:
				break
		else:
			continue
		break

	if contador >= longitud:
		print("Mensaje escrito correctamente")
	else:
		print("Advertencia: no se pudo escribir todo el mensaje, sobraron {} caracteres".format( math.floor((longitud - contador) / 8) ))

	imagen.save(imageRouteOut)

hideText(
	"@--El Himno Nacional Mexicano es uno de los tres símbolos patrios establecidos por la ley en dicho país junto con el escudo y la bandera. Pese a conocerse y usarse como tal desde 1854, solo se hizo oficial desde 1943, a partir de un decreto expedido por Manuel Ávila Camacho, quien fungió como presidente de México de 1940 a 1946. Y desde febrero de 1984 su uso es regulado por la Secretaría de Gobernación con base en la Ley sobre el escudo, la bandera y el himno nacional La letra del himno alude a victorias mexicanas en batallas, trata sobre la defensa de la patria, las virtudes del pueblo que la ejerce y el sacrificio que conlleva. Sus estrofas y estribillo fueron compuestas por el poeta potosino Francisco González Bocanegra en 1853, mientras que su música, obra del músico español Jaime Nunó, fue compuesta al año siguiente. En su versión original, el himno está compuesto por diez estrofas, pero en los noventa años que pasó para su oficialización pasó por varias modificaciones o intentos de modificación, y quedó reducido solo a cuatro estrofas y el estribillo a partir de 1943, cuando se oficializó.", 
	"wall.png",
	"wall_himno.png"
)