import cv2
import mediapipe as mp

# Inicializar el estimador de posturas
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Definir la altura mínima para considerar que los brazos están levantados
MIN_ARM_HEIGHT = 100  # Ajusta este valor según tus necesidades

# Iniciar la captura de video desde la cámara
source = cv2.VideoCapture(0)

# Variable para controlar si la alarma está activa
alarm_active = False

# Función para verificar si los brazos están levantados y activar la alarma
def check_arms_and_alarm(landmarks):
    global alarm_active
    
    # Verificar si los brazos están levantados
    if are_arms_raised(landmarks):
        if not alarm_active:
            print("¡Alarma activada!")
            alarm_active = True
    else:
        alarm_active = False

# Función para verificar si las muñecas sobrepasan el límite definido
def are_arms_raised(landmarks):
    if not landmarks:
        return False
    
    # Convertir los landmarks a un formato más fácil de manejar
    landmarks_list = [lm for lm in landmarks]
    
    # Obtiene las coordenadas de los puntos clave de las muñecas
    left_wrist = landmarks_list[15]  # La posición de la muñeca izquierda
    right_wrist = landmarks_list[16]  # La posición de la muñeca derecha
    
    if left_wrist and right_wrist:
        # Calcula la posición vertical de las muñecas
        left_wrist_y = left_wrist.y * frame.shape[0]  # Convertir a píxeles
        right_wrist_y = right_wrist.y * frame.shape[0]  # Convertir a píxeles
        
        # Retorna True si alguna de las muñecas sobrepasa el límite definido
        return left_wrist_y > MIN_ARM_HEIGHT or right_wrist_y > MIN_ARM_HEIGHT
    
    return False

while source.isOpened():
    _, frame = source.read()
    
    try:
        # Dibujar la línea límite en el fotograma
        cv2.line(frame, (0, MIN_ARM_HEIGHT), (frame.shape[1], MIN_ARM_HEIGHT), (0, 0, 255), 2)
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Procesar el fotograma para detección de posturas
        pose_results = pose.process(frame_rgb)
        
        # Verificar si los brazos están levantados y activar la alarma
        if pose_results.pose_landmarks:
            check_arms_and_alarm(pose_results.pose_landmarks.landmark)
        
        # Dibujar el esqueleto en el fotograma
        mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        cv2.imshow('Salida', frame)
    
    except Exception as e:
        print("Error:", e)
        break
    
    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) == ord('q'):
        break

source.release()
cv2.destroyAllWindows()
