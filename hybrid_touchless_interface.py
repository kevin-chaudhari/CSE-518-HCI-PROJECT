# # hybrid_touchless_interface.py
# import cv2
# import mediapipe as mp
# import pyautogui
# import time
# from GazeTracking.gaze_tracking import GazeTracking


# # Initialization
# gaze = GazeTracking()
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
# mp_draw = mp.solutions.drawing_utils
# screen_width, screen_height = pyautogui.size()

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# # Helper functions
# prev_x, prev_y = 0, 0
# smooth_factor = 0.2  # 0–1; higher = faster but shakier
# last_click_time = 0

# def smooth_cursor(x, y):
#     """Exponential smoothing to make motion stable."""
#     global prev_x, prev_y
#     smoothed_x = prev_x + (x - prev_x) * smooth_factor
#     smoothed_y = prev_y + (y - prev_y) * smooth_factor
#     prev_x, prev_y = smoothed_x, smoothed_y
#     return int(smoothed_x), int(smoothed_y)

# def distance(p1, p2):
#     """Euclidean distance between two Mediapipe landmarks."""
#     return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

# def get_palm_center(handLms):
#     """Approximate palm center using wrist and finger bases."""
#     ids = [0, 5, 9, 13, 17]
#     cx = sum(handLms.landmark[i].x for i in ids) / len(ids)
#     cy = sum(handLms.landmark[i].y for i in ids) / len(ids)
#     return cx, cy


# # Main loop
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # --- Eye Tracking ---
#     gaze.refresh(frame)
#     if gaze.is_left():
#         eye_text = "Looking Left"
#     elif gaze.is_right():
#         eye_text = "Looking Right"
#     elif gaze.is_center():
#         eye_text = "Looking Center"
#     else:
#         eye_text = "Blinking"

#     # --- Hand Tracking ---
#     results = hands.process(rgb_frame)
#     gesture_text = "No Hand Detected"

#     if results.multi_hand_landmarks:
#         handLms = results.multi_hand_landmarks[0]
#         mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

#         # --- Use palm center instead of fingertip ---
#         palm_x, palm_y = get_palm_center(handLms)
#         x = int(palm_x * screen_width)
#         y = int(palm_y * screen_height)

#         # Smooth cursor movement
#         cursor_x, cursor_y = smooth_cursor(x, y)
#         pyautogui.moveTo(cursor_x, cursor_y)

#         # --- Use pinch gesture (thumb + index) for click ---
#         index_tip = handLms.landmark[8]
#         thumb_tip = handLms.landmark[4]
#         pinch_dist = distance(index_tip, thumb_tip)
#         now = time.time()
#         click_cooldown = 0.6  # seconds between clicks

#         if pinch_dist < 0.04 and (now - last_click_time) > click_cooldown:
#             pyautogui.click()
#             last_click_time = now
#             gesture_text = "Click (Pinch)"
#         else:
#             gesture_text = f"Tracking palm ({int(pinch_dist * 100)} cm est.)"

#         # Draw palm center on frame
#         px, py = int(palm_x * frame.shape[1]), int(palm_y * frame.shape[0])
#         cv2.circle(frame, (px, py), 10, (0, 255, 255), -1)
    
#     # --- Display info on screen ---
#     cv2.putText(frame, f'Eye: {eye_text}', (30, 50),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.putText(frame, f'Gesture: {gesture_text}', (30, 100),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#     # Resize the frame to a smaller window (for recording as a side video)
#     display_scale = 0.4  # Adjust between 0.2–0.6 for smaller/larger window
#     small_frame = cv2.resize(frame, (0, 0), fx=display_scale, fy=display_scale)

#     # Create a flexible, movable window
#     cv2.namedWindow("Hybrid Touchless Interface (Palm Cursor)", cv2.WINDOW_NORMAL)
#     cv2.resizeWindow("Hybrid Touchless Interface (Palm Cursor)", 480, 320)  # default size
#     cv2.moveWindow("Hybrid Touchless Interface (Palm Cursor)", 50, 50)  # x, y position on screen

#     # Show the smaller frame
#     cv2.imshow("Hybrid Touchless Interface (Palm Cursor)", small_frame)

#     # Exit when pressing 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# cap.release()
# cv2.destroyAllWindows()



# import cv2
# import mediapipe as mp
# import pyautogui
# import time
# from GazeTracking.gaze_tracking import GazeTracking
# import ctypes

# # Initialization
# gaze = GazeTracking()
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
# mp_draw = mp.solutions.drawing_utils
# screen_width, screen_height = pyautogui.size()

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# # Helper functions
# prev_x, prev_y = 0, 0
# smooth_factor = 0.2
# last_click_time = 0

# def smooth_cursor(x, y):
#     global prev_x, prev_y
#     smoothed_x = prev_x + (x - prev_x) * smooth_factor
#     smoothed_y = prev_y + (y - prev_y) * smooth_factor
#     prev_x, prev_y = smoothed_x, smoothed_y
#     return int(smoothed_x), int(smoothed_y)

# def distance(p1, p2):
#     return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

# def get_palm_center(handLms):
#     ids = [0, 5, 9, 13, 17]
#     cx = sum(handLms.landmark[i].x for i in ids) / len(ids)
#     cy = sum(handLms.landmark[i].y for i in ids) / len(ids)
#     return cx, cy


# # Create a fixed OpenCV window once (bottom-right corner)
# window_name = "Hybrid Touchless Interface (Palm Cursor)"
# cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
# cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)  # keep always on top
# cv2.resizeWindow(window_name, 400, 280)  # fixed small window
# cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

# # Calculate position for bottom-right placement
# window_width, window_height = 400, 280
# x_pos = screen_width - window_width - 20
# y_pos = screen_height - window_height - 80
# cv2.moveWindow(window_name, x_pos, y_pos)

# # Keep window always on top using Win32 (Windows only)
# def always_on_top():
#     hwnd = ctypes.windll.user32.FindWindowW(None, window_name)
#     if hwnd:
#         ctypes.windll.user32.SetWindowPos(hwnd, -1, x_pos, y_pos, window_width, window_height, 0x0001)

# # Main loop
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # --- Eye Tracking ---
#     gaze.refresh(frame)
#     if gaze.is_left():
#         eye_text = "Looking Left"
#     elif gaze.is_right():
#         eye_text = "Looking Right"
#     elif gaze.is_center():
#         eye_text = "Looking Center"
#     else:
#         eye_text = "Blinking"

#     # --- Hand Tracking ---
#     results = hands.process(rgb_frame)
#     gesture_text = "No Hand Detected"

#     if results.multi_hand_landmarks:
#         handLms = results.multi_hand_landmarks[0]
#         mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

#         palm_x, palm_y = get_palm_center(handLms)
#         x = int(palm_x * screen_width)
#         y = int(palm_y * screen_height)

#         cursor_x, cursor_y = smooth_cursor(x, y)
#         pyautogui.moveTo(cursor_x, cursor_y)

#         index_tip = handLms.landmark[8]
#         thumb_tip = handLms.landmark[4]
#         pinch_dist = distance(index_tip, thumb_tip)
#         now = time.time()
#         click_cooldown = 0.6

#         if pinch_dist < 0.04 and (now - last_click_time) > click_cooldown:
#             pyautogui.click()
#             last_click_time = now
#             gesture_text = "Click (Pinch)"
#         else:
#             gesture_text = f"Tracking palm ({int(pinch_dist * 100)} cm est.)"

#         px, py = int(palm_x * frame.shape[1]), int(palm_y * frame.shape[0])
#         cv2.circle(frame, (px, py), 10, (0, 255, 255), -1)

#     cv2.putText(frame, f'Eye: {eye_text}', (30, 50),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.putText(frame, f'Gesture: {gesture_text}', (30, 100),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#     # Resize frame for fixed display
#     small_frame = cv2.resize(frame, (window_width, window_height))
#     always_on_top()  # ensure window stays on top
#     cv2.imshow(window_name, small_frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



import cv2
import mediapipe as mp
import pyautogui
import time
from GazeTracking.gaze_tracking import GazeTracking
import ctypes

# --- Configuration ---
pyautogui.FAILSAFE = False  # Prevent crash if cursor hits corner
SMOOTH_FACTOR_HAND = 0.2    # Responsive for hands
SMOOTH_FACTOR_EYE = 0.08    # Smooth for eyes

# Initialization
gaze = GazeTracking()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# State Variables
prev_x, prev_y = 0, 0
last_click_time = 0

# --- Eye Calibration Variables ---
eye_h_min, eye_h_max = 1.0, 0.0 
eye_v_min, eye_v_max = 1.0, 0.0
calibration_margin = 0.02 

# Blink Variables
blink_start_time = 0
blink_detected = False
last_blink_end_time = 0
double_blink_interval = 0.4

def smooth_cursor(target_x, target_y, factor):
    global prev_x, prev_y
    # Linear interpolation for smoothing
    smoothed_x = prev_x + (target_x - prev_x) * factor
    smoothed_y = prev_y + (target_y - prev_y) * factor
    prev_x, prev_y = smoothed_x, smoothed_y
    return int(smoothed_x), int(smoothed_y)

def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

def get_palm_center(handLms):
    # Calculates center using Wrist(0) and Knuckles(5,9,13,17)
    ids = [0, 5, 9, 13, 17]
    cx = sum(handLms.landmark[i].x for i in ids) / len(ids)
    cy = sum(handLms.landmark[i].y for i in ids) / len(ids)
    return cx, cy

# Window Setup (Bottom-Right Corner)
window_name = "Hybrid Interface (Palm + Eye)"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
cv2.resizeWindow(window_name, 400, 280)

window_width, window_height = 400, 280
x_pos = screen_width - window_width - 20
y_pos = screen_height - window_height - 80
cv2.moveWindow(window_name, x_pos, y_pos)

def keep_always_on_top():
    hwnd = ctypes.windll.user32.FindWindowW(None, window_name)
    if hwnd:
        ctypes.windll.user32.SetWindowPos(hwnd, -1, x_pos, y_pos, window_width, window_height, 0x0001)

print("System Started.")
print("1. Hand Mode: Show palm to move cursor. Pinch to click.")
print("2. Eye Mode: Hide hand to use eyes. Look at corners to calibrate.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame for mirror effect
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 1. Analyze Gaze (Always run this to keep calibration active)
    gaze.refresh(frame)
    frame = gaze.annotated_frame()

    # 2. Analyze Hands
    results = hands.process(rgb_frame)
    
    status_text = "Idle"
    mode_text = "Waiting..."

    # MODE 1: HAND TRACKING (Priority - from your requested code)
    if results.multi_hand_landmarks:
        mode_text = "HAND MODE"
        handLms = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

        # A. Calculate Palm Center
        palm_x, palm_y = get_palm_center(handLms)
        
        # B. Map to Screen
        screen_x = int(palm_x * screen_width)
        screen_y = int(palm_y * screen_height)
        
        # C. Smooth and Move
        cx, cy = smooth_cursor(screen_x, screen_y, SMOOTH_FACTOR_HAND)
        pyautogui.moveTo(cx, cy)

        # D. Pinch Click Logic
        index_tip = handLms.landmark[8]
        thumb_tip = handLms.landmark[4]
        pinch_dist = distance(index_tip, thumb_tip)
        
        if pinch_dist < 0.04: # Threshold for pinch
            if (time.time() - last_click_time) > 0.6: # Debounce time
                pyautogui.click()
                last_click_time = time.time()
                status_text = "CLICK (Pinch)"
        else:
            status_text = "Tracking Palm"

        # E. Visual Feedback (Yellow Circle on Palm)
        # We must convert normalized palm_x/y back to frame pixels for drawing
        px, py = int(palm_x * frame.shape[1]), int(palm_y * frame.shape[0])
        cv2.circle(frame, (px, py), 10, (0, 255, 255), -1)

    # MODE 2: EYE TRACKING (Fallback)
    else:
        mode_text = "EYE MODE"
        
        # Get raw ratios
        h_ratio = gaze.horizontal_ratio()
        v_ratio = gaze.vertical_ratio()

        if h_ratio is not None and v_ratio is not None:
            # Dynamic Calibration logic
            if h_ratio < eye_h_min: eye_h_min = h_ratio
            if h_ratio > eye_h_max: eye_h_max = h_ratio
            if v_ratio < eye_v_min: eye_v_min = v_ratio
            if v_ratio > eye_v_max: eye_v_max = v_ratio

            h_diff = (eye_h_max - eye_h_min) if (eye_h_max - eye_h_min) > 0 else 0.01
            v_diff = (eye_v_max - eye_v_min) if (eye_v_max - eye_v_min) > 0 else 0.01

            norm_x = (h_ratio - eye_h_min) / h_diff
            norm_y = (v_ratio - eye_v_min) / v_diff

            target_x = int(norm_x * screen_width)
            target_y = int(norm_y * screen_height)

            cx, cy = smooth_cursor(target_x, target_y, SMOOTH_FACTOR_EYE)
            pyautogui.moveTo(cx, cy)

            status_text = f"Gaze: {norm_x:.2f}, {norm_y:.2f}"
        
        # Blink Logic
        is_blinking = gaze.is_blinking()
        if is_blinking:
            if not blink_detected:
                blink_detected = True
                blink_start_time = time.time()
        else:
            if blink_detected:
                blink_detected = False
                blink_duration = time.time() - blink_start_time
                if 0.1 < blink_duration < 0.6:
                    time_since_last = time.time() - last_blink_end_time
                    if time_since_last < double_blink_interval:
                        pyautogui.click()
                        status_text = "DOUBLE BLINK CLICK!"
                        last_blink_end_time = 0
                    else:
                        status_text = "Single Blink..."
                        last_blink_end_time = time.time()

    # --- UI Overlays ---
    cv2.putText(frame, mode_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(frame, status_text, (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Display
    small_frame = cv2.resize(frame, (window_width, window_height))
    keep_always_on_top()
    cv2.imshow(window_name, small_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()