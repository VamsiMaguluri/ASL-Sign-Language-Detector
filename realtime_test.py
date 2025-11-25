import cv2
import numpy as np
from tensorflow.keras.models import load_model

# --- 1. LOAD THE TRAINED MODEL ---
print("Loading model...")
try:
    model = load_model('sign_language_model_95.h5')
    print("Model loaded successfully!")
except:
    print("ERROR: Could not find 'sign_language_model.h5'. Make sure you are in the correct folder.")
    exit()

# --- 2. DEFINE THE LABELS ---
labels = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
    9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
    17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
    25: 'Z', 26: 'del', 27: 'nothing', 28: 'space'
}

# --- 3. START WEBCAM (WITH DIRECTSHOW FIX) ---
# We add cv2.CAP_DSHOW to fix the Windows error
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# If camera 0 doesn't work, try changing it to 1 in the line above
if not cap.isOpened():
    print("Could not open webcam. Trying index 1...")
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Still cannot read from webcam. Check privacy settings.")
        break

    # Flip frame for "mirror" effect
    frame = cv2.flip(frame, 1)

    # Draw the ROI (Region of Interest) Box
    # User puts hand inside this Blue Box
    cv2.rectangle(frame, (100, 100), (350, 350), (255, 0, 0), 2)
    
    # Crop the image to just the box
    roi = frame[100:350, 100:350]
    
    # Preprocessing
    try:
        img = cv2.resize(roi, (64, 64))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        # Prediction
        prediction = model.predict(img, verbose=0)
        index = np.argmax(prediction)
        confidence = prediction[0][index]
        
        predicted_char = labels[index]

        # Display Text
        if confidence > 0.5:
            display_text = f"Sign: {predicted_char} ({int(confidence*100)}%)"
            color = (0, 255, 0) 
        else:
            display_text = "Sign: ?"
            color = (0, 0, 255) 
            
        cv2.putText(frame, display_text, (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    except Exception as e:
        pass # Ignore errors if hand is out of frame

    cv2.imshow("ASL Translator (Press 'q' to quit)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()