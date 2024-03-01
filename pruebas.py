import cv2
import mediapipe as mp

# Importar las clases necesarias
BaseOptions = mp.tasks.BaseOptions
DetectionResult = mp.tasks.vision.ObjectDetectorResult
ObjectDetector = mp.tasks.vision.ObjectDetector
ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Definir la función de callback para imprimir los resultados de la detección
def print_result(result: DetectionResult, output_image: mp.Image, timestamp_ms: int):
    print('Detection result:', result)

# Definir las opciones para el detector de objetos
options = ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path='modelo\efficientdet_lite0.tflite'),
    running_mode=VisionRunningMode.IMAGE,
    max_results=5,
)

# Crear el detector de objetos a partir de las opciones definidas


with ObjectDetector.create_from_options(options) as detector:
    # Inicializar la captura de video desde la cámara
    source = cv2.VideoCapture(0)
    
    while source.isOpened():
        # Leer un frame de la cámara
        ret, frame = source.read()
        if not ret:
            break
        
        # Convertir el frame de BGR a RGB (ya que MediaPipe espera imágenes en formato RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Procesar la detección de objetos en el frame actual
        
        results = detector.detect(mp.Image
                                  (image_format=mp.ImageFormat.SRGB, data=rgb_frame))
        
        
        # Mostrar el frame con los resultados de la detección
        cv2.imshow('Object Detection', frame)
        
        # Salir del bucle si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Liberar los recursos y cerrar las ventanas
    source.release()
    cv2.destroyAllWindows()
