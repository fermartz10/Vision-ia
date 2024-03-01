import cv2
import mediapipe as mp

# Crea una instancia del detector de objetos
mp_objectron = mp.solutions.objectron
objectron = mp_objectron.Objectron(static_image_mode=False, max_num_objects=5, min_detection_confidence=0.5, min_tracking_confidence=0.99, model_name='Shoe')

# Crea un objeto de captura de video para la cámara.
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convierte la imagen a RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesa la imagen con el detector de objetos
    results = objectron.process(image_rgb)

    # Dibuja las anotaciones de los objetos detectados en la imagen
    if results.detected_objects:
        for detected_object in results.detected_objects:
            mp.solutions.drawing_utils.draw_landmarks(frame, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
    
    # Muestra la imagen
    cv2.imshow('Video en tiempo real', frame)

    # Sal del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando todo esté hecho, libera la captura
cap.release()
cv2.destroyAllWindows()
