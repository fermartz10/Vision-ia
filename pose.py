import cv2
import mediapipe as mp

## inicializar el estimador de posturas
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

source = cv2.VideoCapture(0)
while source.isOpened():
    # leer el fotograma
    _, frame = source.read()
    try:
         # redimensionar el fotograma para video en vertical
         # frame = cv2.resize(frame, (350, 600))
         # convertir a RGB
         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
         
         # procesar el fotograma para detección de posturas
         pose_results = pose.process(frame_rgb)
         # print(pose_results.pose_landmarks)
         
         # dibujar el esqueleto en el fotograma
         mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
         # mostrar el fotograma
         cv2.imshow('Salida', frame)
    except:
         break
    
    if cv2.waitKey(1) == ord('q'):
          break
          
source.release()
cv2.destroyAllWindows()