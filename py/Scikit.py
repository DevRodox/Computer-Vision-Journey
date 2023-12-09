import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import disk, rectangle, ellipse, polygon
from skimage import measure, io
import matplotlib.patches as mpatches

# Crear una imagen en negro
image_shape = (400, 400)
binary_image = np.zeros(image_shape, dtype=np.uint8)

# Dibujar un círculo
rr, cc = disk((100, 100), 50)
binary_image[rr, cc] = 1

# Dibujar un rectángulo
rr, cc = rectangle(start=(50, 250), extent=(100, 50))
binary_image[rr, cc] = 1

# Dibujar una elipse
rr, cc = ellipse(300, 100, 60, 30)
binary_image[rr, cc] = 1

# Dibujar un triángulo
rr_triangle = np.array([300, 350, 350])
cc_triangle = np.array([300, 275, 325])
rr, cc = polygon(rr_triangle, cc_triangle)
binary_image[rr, cc] = 1

# Etiquetar los objetos en la imagen
label_image = measure.label(binary_image)

# Calcular propiedades de los objetos etiquetados
props = measure.regionprops(label_image)

# Crear una figura para mostrar los resultados
fig, ax = plt.subplots()
ax.imshow(binary_image, cmap='gray')

# Mostrar las propiedades de cada objeto
for prop in props:
    print(f'Label: {prop.label}')
    print(f'Area: {prop.area}')
    print(f'Perimeter: {prop.perimeter}')
    print(f'Centroid: {prop.centroid}')
    print(f'BoundingBox: {prop.bbox}')
    print(f'Orientation: {prop.orientation}')
    # Dibujar un rectángulo alrededor del objeto
    minr, minc, maxr, maxc = prop.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(rect)

# Configurar ejes
ax.set_axis_off()
plt.tight_layout()
plt.show()
