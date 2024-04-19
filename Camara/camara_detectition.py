# El código detecta cículos en el centro de la pantalla (en la computadora)
# Hay un contador para los Circulos detectados (todos los que se ven al momento)

import cv2
import numpy as np

circulosDetectados = 0

# Función para detectar círculos en una región de interés (ROI) de la imagen
def detect_circles_in_roi(image, x_center, y_center, roi_width, roi_height):
    
    global circulosDetectados
    
    # Definir la región de interés (ROI) centrada en (x_center, y_center)
    x = int(x_center - roi_width/2)
    y = int(y_center - roi_height/2)
    roi = image[y:y+roi_height, x:x+roi_width]
    
    # Convertir la ROI a escala de grises
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    # Aplicar suavizado para reducir el ruido
    gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    
    # Detectar círculos utilizando la transformada de Hough
    circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=0, maxRadius=0)
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x_circle, y_circle, r) in circles:
            # Ajustar las coordenadas del círculo al fotograma original
            x_circle += x
            y_circle += y
            # Dibujar el círculo y su centro en el fotograma original
            cv2.circle(image, (x_circle, y_circle), r, (0, 255, 0), 4)
            cv2.rectangle(image, (x_circle - 5, y_circle - 5), (x_circle + 5, y_circle + 5), (0, 128, 255), -1)
        circulosDetectados += 1
        
    
    return image

# Tamaño de la región de interés (ROI) centrada en el centro de la pantalla
roi_width = 300
roi_height = 300

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if ret:
        # Obtener las dimensiones del fotograma
        height, width = frame.shape[:2]
        
        # Calcular las coordenadas del centro de la pantalla
        x_center = int(width / 2)
        y_center = int(height / 2)
        
        # Detectar círculos en el área central de la imagen
        detected_frame = detect_circles_in_roi(frame, x_center, y_center, roi_width, roi_height)
        print("Circulos detectados:", circulosDetectados)
        
        # Mostrar el fotograma con círculos detectados
        cv2.imshow("Detected Circles", detected_frame)
    
    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
