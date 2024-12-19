import math
import mediapipe as mp

def calculate_distance(landmark1, landmark2):
    return math.sqrt((landmark1.x - landmark2.x)**2 + (landmark1.y - landmark2.y)**2)

def detect_gesture(hand_landmarks):
    # Extract landmarks
    index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    middle_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]

    # Check if thumb and index finger are close (left click)
    if calculate_distance(index_tip, thumb_tip) < 0.05:
        return 'left_click'
    
    # Check if index and middle fingers are extended (right click)
    if calculate_distance(index_tip, middle_tip) < 0.1:
        return 'right_click'
    
    # Default gesture to move the cursor
    return 'move_cursor'
