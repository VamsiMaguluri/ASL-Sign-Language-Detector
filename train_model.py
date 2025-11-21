import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import os

# --- CRITICAL FIX: POINT TO THE INNER FOLDER ---
# Your structure is: asl_alphabet_train -> asl_alphabet_train -> [A, B, C...]
DATA_DIR = 'asl_alphabet_train/asl_alphabet_train'

# Verification: Print what we find inside to be sure
if os.path.exists(DATA_DIR):
    contents = os.listdir(DATA_DIR)
    print(f"✅ Success! Found {len(contents)} items in folder.")
    print(f"First 5 items: {contents[:5]}")
else:
    print(f"❌ ERROR: Could not find folder: {DATA_DIR}")
    exit()

# --- CONFIGURATION ---
IMG_SIZE = 64
BATCH_SIZE = 32
NUM_CLASSES = 29

# --- DATA GENERATORS ---
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_generator = datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# --- BUILD MODEL ---
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    MaxPooling2D(2, 2),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(NUM_CLASSES, activation='softmax')
])

# --- TRAIN ---
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

print("\nStarting Training... (This will take 15-30 mins)")
model.fit(train_generator, epochs=5, validation_data=val_generator)

# --- SAVE ---
model.save('sign_language_model.h5')
print("\nSUCCESS! Model saved as 'sign_language_model.h5'")