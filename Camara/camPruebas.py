import cv2
import numpy as np

totalCuadrados = 0

def detect_shapes(image):
    
    global totalCuadrados
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar umbralización adaptativa
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Encontrar contornos en la imagen umbralizada
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detected_shapes = []
    for contour in contours:
        # Aproximar la forma del contorno a una forma más simple
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Determinar el tipo de forma
        sides = len(approx)
        shape = ""
        if sides == 4:
            # Calcular el rectángulo delimitador para verificar si es un cuadrado
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            if 0.95 <= aspect_ratio <= 1.05:
                shape = "Cuadrado"
                
        elif sides == 5:
            shape = "Pentágono"

        # Si se detecta una forma, dibujar su contorno en la imagen original
        if shape:
            detected_shapes.append((shape, contour))
            totalCuadrados += 1
            print("Cuadrado", totalCuadrados)

    # Dibujar contornos de formas detectadas en la imagen original
    for shape, contour in detected_shapes:
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        
    return image

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if ret:
        # Detectar formas en la imagen
        detected_frame = detect_shapes(frame)
        
        # Mostrar el fotograma con formas detectadas
        cv2.imshow("Detected Shapes", detected_frame)
    
    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()

