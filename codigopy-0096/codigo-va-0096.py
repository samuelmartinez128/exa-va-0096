# Samuel Martinez NC 0096

import cv2
from pathlib import Path

# 1. Definir las rutas de trabajo (subiendo un solo nivel con .parent)
carpeta_script = Path(__file__).resolve().parent
carpeta_proyecto = carpeta_script.parent

ruta_original = (
    carpeta_proyecto
    / "img-original-0096"
    / "img-ventiladorr-0096.jpg"
)

carpeta_resultados = (
    carpeta_proyecto / "resultados-img-0096"
)

# Crear la carpeta de resultados si no existe
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original con imread
img0096 = cv2.imread(str(ruta_original))

# Comprobar que la imagen se haya leído correctamente
if img0096 is None:
    raise FileNotFoundError(
        f"No se pudo leer la imagen: {ruta_original}"
    )

# 3. Rotar la imagen 90 grados en sentido horario
img90_0096 = cv2.rotate(
    img0096, cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar la imagen 45 grados
alto, ancho = img0096.shape[:2]

centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_0096 = cv2.warpAffine(
    img0096,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Redimensionar a 600 píxeles de ancho y 500 píxeles de alto
img600x500_0096 = cv2.resize(
    img0096, (600, 500)
)

# 6. Dibujar un rectángulo rojo de 100 x 200 píxeles sobre una copia de la imagen original
img_rojo_0096 = img0096.copy()

x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200

cv2.rectangle(
    img_rojo_0096,
    (x1, y1),
    (x2, y2),
    (0, 0, 255),
    3
)

# 7. Mostrar las cinco imágenes con sus títulos
cv2.imshow("ventilador original 0096", img0096)

cv2.imshow("ventilador 90 0096", img90_0096)

cv2.imshow("ventilador 45 0096", img45_0096)

cv2.imshow(
    "ventilador 600x500 0096",
    img600x500_0096
)

cv2.imshow("ventilador rojo 0096", img_rojo_0096)

# 8. Guardar las cuatro imágenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "img-ventilador1-0096.jpg"),
    img90_0096
)

cv2.imwrite(
    str(carpeta_resultados / "img-ventilador2-0096.jpg"),
    img45_0096
)

cv2.imwrite(
    str(carpeta_resultados / "img-ventilador3-0096.jpg"),
    img600x500_0096
)

cv2.imwrite(
    str(carpeta_resultados / "img-ventilador4-0096.jpg"),
    img_rojo_0096
)

# 9. Esperar una tecla y cerrar las ventanas
print("Imágenes procesadas y guardadas.")
print("Presiona una tecla en las ventanas para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Samuel Martinez NC 0096")