# Leer la imagen
img = cv2.imread('./imgs/lena_std.tif', cv2.IMREAD_GRAYSCALE)  # Leer en escala de grises directamente

# Calcular el histograma
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Visualizar la imagen y su histograma
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Mostrar la imagen en escala de grises
ax[0].imshow(img, cmap='gray')
ax[0].set_title("Imagen en Grises")
ax[0].axis('off')

# Mostrar el histograma
ax[1].plot(hist, color='black')
ax[1].set_title("Histograma")
ax[1].set_xlabel("Intensidad de Pixel")
ax[1].set_ylabel("Cantidad de Píxeles")
ax[1].grid(True)

plt.tight_layout()
plt.show()