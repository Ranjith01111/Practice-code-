import opencv2
import mediapipe as mp
import numpy as np
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to calculate Euclidean distance
def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)*2 + (y2 - y1)*2)

# Function to control the mouse
def control_mouse(hand_landmarks, frame_width, frame_height):
    if hand_landmarks:
        # Get index finger and thumb landmarks
        index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

        # Convert landmarks to pixel coordinates
        ix, iy = int(index_finger.x * frame_width), int(index_finger.y * frame_height)
        tx, ty = int(thumb.x * frame_width), int(thumb.y * frame_height)

        # Move the mouse
        pyautogui.moveTo(ix, iy)

        # Check if thumb is close to index finger
        if calculate_distance(ix, iy, tx, ty) < 30:
            pyautogui.click()

# Open webcam
cap = opencv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = opencv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # Convert BGR to RGB
    rgb_frame = opencv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Control mouse
            control_mouse(hand_landmarks, frame_width, frame_height)

    opencv2.imshow('Virtual Mouse', frame)

    if opencv2.waitKey(10) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the VideoCapture object and close all windows
cap.release()
opencv2.destroyAllWindows()
