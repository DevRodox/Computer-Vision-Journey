import numpy as np
import cv2
import matplotlib.pyplot as plt

# Cargar una imagen en escala de grises
image = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Definir el tamaño del kernel (ventana de filtro)
kernel_size = 3  # Tamaño 3x3

# Obtener las dimensiones de la imagen
height, width = image.shape

# Crear una matriz vacía para la imagen filtrada
filtered_image = np.zeros((height, width), dtype=np.uint8)

# Recorrer la imagen y aplicar el filtro de promedio
for y in range(1, height - 1):
    for x in range(1, width - 1):
        # Extraer el vecindario (submatriz) centrado en (x, y)
        neighborhood = image[y - 1:y + 2, x - 1:x + 2]
        
        # Calcular el promedio de los valores en el vecindario
        average = np.mean(neighborhood)
        
        # Asignar el valor promedio al píxel en la imagen filtrada
        filtered_image[y, x] = int(average)

# Mostrar la imagen original y la imagen filtrada utilizando matplotlib
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Imagen Filtrada')

plt.tight_layout()
plt.show()
