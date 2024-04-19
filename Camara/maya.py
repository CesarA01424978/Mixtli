import cv2
import numpy as np

# Crear una imagen en blanco
image = np.zeros((300, 300, 3), dtype=np.uint8)

# Definir las coordenadas de los puntos de la cuadrícula
# Horizontales
cv2.line(image, (0, 100), (300, 100), (255, 255, 255), 1)
cv2.line(image, (0, 200), (300, 200), (255, 255, 255), 1)

# Verticales
cv2.line(image, (100, 0), (100, 300), (255, 255, 255), 1)
cv2.line(image, (200, 0), (200, 300), (255, 255, 255), 1)

# Mostrar la imagen con la cuadrícula
cv2.imshow("Cuadrícula", image)
cv2.waitKey(0)
cv2.destroyAllWindows()