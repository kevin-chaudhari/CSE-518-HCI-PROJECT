# Gesture Control & Eye Tracking: A Hybrid Approach to Touchless Interfaces  
### CSE-518 Human–Computer Interaction Project

This project integrates **gesture recognition** and **eye-tracking** to create a unified, touchless interaction system.  
The hybrid design enables users to perform actions using hand movements while allowing precise control through gaze detection.

The system is built for:
- Accessibility and assistive technologies  
- Sterile medical environments  
- AR/VR interaction  
- Smart displays and kiosks  
- Next-generation UI/UX research  

---

## **Features**

### 1. Gesture Control  
The system supports multiple gesture types, including:
- Static hand gestures  
- Dynamic motion gestures  
- Swipe, pinch, grab, and directional gestures  
- Custom actions mapped to gesture events  

---

### 2. Eye Tracking  
Powered by the **GazeTracking** module, the system identifies:
- Eye position  
- Blink detection  
- Pupil location  
- Left, right, up, and down gaze direction  

---

### 3. Hybrid Interaction Model  
The fusion of hand gestures and eye tracking enables:
- Select with gaze, confirm with gesture  
- Navigate with eyes, interact with hands  
- Smooth cursor control via palm + eye ratios  
- Touchless control suitable for AR/VR or sterile environments  

---

## **Tech Stack**

- Python 3.x  
- OpenCV  
- MediaPipe (Hand Gesture Recognition)  
- GazeTracking Library  
- PyAutoGUI  
- NumPy  
- Custom hybrid logic (`hybrid_touchless_interface.py`)  

---

## **Project Structure**

```plaintext
CSE-518-HCI-PROJECT/
│
├── GazeTracking/                 # Eye-tracking module
├── __pycache__/                  # Auto-generated cache (ignored in Git)
│
├── hybrid_touchless_interface.py # Main interaction script
├── README.md                     # Project documentation
├── LICENSE                       # MIT License
├── requirements.txt              # Python dependencies
```

---

## **How It Works**

### **1. Camera Input**  
OpenCV captures real-time video from the webcam.

### **2. Hand Gesture Detection**  
MediaPipe processes frames to detect:
- 21 hand landmarks  
- Palm center  
- Pinch gesture → triggers click  
- Hand presence → switches to Hand Mode  

### **3. Eye Tracking**  
GazeTracking extracts:
- Horizontal and vertical eye ratios  
- Pupil position  
- Blink detection  
- Gaze direction (L/R/Up/Down)

### **4. Hybrid Fusion Engine**  
The system intelligently switches modes:
- **Hand Mode** when the hand is visible  
- **Eye Mode** when no hand is detected  

Hybrid actions include:
- Select with gaze, trigger with pinch  
- Move cursor with palm or eyes  
- Blink-based clicking  
- Dynamic calibration for each user  

---

## **Use Cases**

- Touchless public interfaces  
- Accessibility for users with motor impairments  
- Medical & laboratory sterile environments  
- Interactive museum installations  
- Gaming, AR/VR, robotics interfaces  

---

## **Installation**

```bash
git clone https://github.com/kevin-chaudhari/CSE-518-HCI-PROJECT.git
cd CSE-518-HCI-PROJECT
pip install -r requirements.txt
python hybrid_touchless_interface.py
```

If you need, I can create:
- `setup.sh`  
- Windows installer script  
- Conda environment file  
- Dockerfile  

---

## **Demo (Optional)**

Your 3-minute video demo can include:
1. Gesture detection examples  
2. Eye tracking overlay  
3. Combined hybrid usage  
4. System statistics  
5. Code walkthrough and architecture view  

I can also write a complete script for your video narration.

---

## **License**

This project is licensed under the **MIT License**.

---

## **Author**

**Kevinkumar Tusharbhai Chaudhari**  
Stony Brook University  
CSE-518 Human–Computer Interaction  

