from PIL import Image
import os






# Directorio donde están tus imágenes JFIF
directorio_entrada = '/Users/factu/Downloads/ProyectosT/Seguridad/modelo/data/images/train'

# Directorio donde quieres guardar las imágenes PNG
directorio_salida = '/Users/factu/Downloads/ProyectosT/Seguridad/modelo/data/images/train2'

# Obtén una lista de todas las imágenes JFIF en el directorio de entrada
imagenes = [f for f in os.listdir(directorio_entrada) if f.endswith('.jfif')]

# Convierte cada imagen JFIF a PNG
for imagen in imagenes:
    # Abre la imagen JFIF
    img = Image.open(os.path.join(directorio_entrada, imagen))
    
    # Crea el nombre del archivo PNG
    nombre_png = os.path.splitext(imagen)[0].replace(' ', '') + '.png'
    
    # Guarda la imagen en formato PNG
    img.save(os.path.join(directorio_salida, nombre_png))
    
