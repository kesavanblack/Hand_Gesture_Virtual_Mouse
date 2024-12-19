import cv2
import mediapipe as mp
import pyautogui
from utils.gesture_recognition import detect_gesture
from utils.mouse_control import perform_mouse_action

# Initialize MediaPipe and webcam
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

# Screen size
screen_width, screen_height = pyautogui.size()

while True:
    success, frame = cap.read()
    if not success:
        break

    # Convert to RGB and downscale for faster processing
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_small = cv2.resize(frame_rgb, (0, 0), fx=0.5, fy=0.5)

    # Process the downscaled frame
    results = hands.process(frame_small)

    # Check for hand landmarks and draw them on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Detect gesture and perform corresponding mouse action
            gesture = detect_gesture(hand_landmarks)
            perform_mouse_action(gesture, hand_landmarks, screen_width, screen_height)

    # Display the output frame
    cv2.imshow("Hand Gesture Virtual Mouse", frame)

    # Control frame rate and allow 'q' key to exit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
