import cv2
import matplotlib.pyplot as plt

# Cargar una imagen
image = cv2.imread('imagen.jpg')

# Definir nuevas dimensiones
nuevas_dimensiones = (400, 300)  # (ancho, alto)

# Redimensionar la imagen utilizando interpolación lineal
imagen_redimensionada_lineal = cv2.resize(image, nuevas_dimensiones, interpolation=cv2.INTER_LINEAR)

# Redimensionar la imagen utilizando interpolación cúbica
imagen_redimensionada_cubica = cv2.resize(image, nuevas_dimensiones, interpolation=cv2.INTER_CUBIC)

# Mostrar las imágenes utilizando matplotlib
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Imagen Original")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(imagen_redimensionada_lineal, cv2.COLOR_BGR2RGB))
plt.title("Imagen Redimensionada (Lineal)")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(imagen_redimensionada_cubica, cv2.COLOR_BGR2RGB))
plt.title("Imagen Redimensionada (Cúbica)")

plt.tight_layout()
plt.show()
