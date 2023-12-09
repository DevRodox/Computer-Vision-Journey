# Leer la imagen y convertirla a RGB
img = cv2.imread('./imgs/lena_std.tif')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Crear copias de la imagen para aislar cada canal
img_R = img_rgb.copy()
img_G = img_rgb.copy()
img_B = img_rgb.copy()

# Aislar el canal R
img_R[:, :, 1] = 0  # G
img_R[:, :, 2] = 0  # B

# Aislar el canal G
img_G[:, :, 0] = 0  # R
img_G[:, :, 2] = 0  # B

# Aislar el canal B
img_B[:, :, 0] = 0  # R
img_B[:, :, 1] = 0  # G

# Visualizar las imágenes
fig, ax = plt.subplots(1, 4, figsize=(20, 5))

ax[0].imshow(img_rgb)
ax[0].set_title("Imagen original")
ax[0].axis('off')

ax[1].imshow(img_R)
ax[1].set_title("Canal Rojo")
ax[1].axis('off')

ax[2].imshow(img_G)
ax[2].set_title("Canal Verde")
ax[2].axis('of')

ax[3].imshow(img_B)
ax[3].set_title("Canal Azul")
ax[3].axis('off')

plt.show()