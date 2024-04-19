# Filtro para quitarle un rango de colores a una imagen

import cv2 #procesamiento de imágenes
import numpy as np

# Leer la imagen
image = cv2.imread('perrito.jpg')

# Redimensionar la imagen a un tamaño más grande
new_width = 800  # Cambiar el ancho deseado
new_height = 600
image_resized = cv2.resize(image, (new_width, new_height))

# Convertir la imagen de BGR a HSV
hsv_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2HSV)

# Definir el rango del color en HSV 0-255
lower_color = np.array([10, 0, 0])
upper_color = np.array([80, 255, 255])

# Crear una máscara para los píxeles del color
mask = cv2.inRange(hsv_image, lower_color, upper_color)

# Aplicar la máscara a la imagen original
color_pixels = cv2.bitwise_and(image_resized, image_resized, mask=mask)

# Mostrar la imagen con solo nuestros píxeles de color resaltados
cv2.imshow('Blue Pixels', color_pixels)
cv2.waitKey(0)
cv2.destroyAllWindows()
