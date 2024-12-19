import pyautogui
import mediapipe as mp  # Import mediapipe to access hand landmarks

def perform_mouse_action(gesture, hand_landmarks, screen_width, screen_height):
    # Index finger tip coordinates
    index_finger_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    cursor_x = int(index_finger_tip.x * screen_width)
    cursor_y = int(index_finger_tip.y * screen_height)
    
    if gesture == 'move_cursor':
        pyautogui.moveTo(cursor_x, cursor_y)
    elif gesture == 'left_click':
        pyautogui.click()
    elif gesture == 'right_click':
        pyautogui.click(button='right')
