# Leer la imagen en escala de grises
img = cv2.imread('./imgs/lena_std.tif', cv2.IMREAD_GRAYSCALE)

# Definir el umbral
umbral = 128  # Puedes cambiar este valor según tus necesidades

# Binarizar la imagen
_, img_binarizada = cv2.threshold(img, umbral, 255, cv2.THRESH_BINARY)

# Visualizar la imagen original y la imagen binarizada
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Mostrar la imagen en escala de grises
ax[0].imshow(img, cmap='gray')
ax[0].set_title("Imagen Original")
ax[0].axis('off')

# Mostrar la imagen binarizada
ax[1].imshow(img_binarizada, cmap='gray')
ax[1].set_title(f"Imagen Binarizada (Umbral = {umbral})")
ax[1].axis('off')


