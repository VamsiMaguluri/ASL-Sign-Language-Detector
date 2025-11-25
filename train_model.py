import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# --- SMART PATH DETECTION ---
# Checks if the data is inside 'asl_alphabet_train/asl_alphabet_train' or just 'asl_alphabet_train'
base_dir = 'asl_alphabet_train'
inner_dir = os.path.join(base_dir, 'asl_alphabet_train')

if os.path.exists(inner_dir):
    DATA_DIR = inner_dir
    print(f"Detected double-folder structure. Using path: {DATA_DIR}")
else:
    DATA_DIR = base_dir
    print(f"Detected standard structure. Using path: {DATA_DIR}")

# --- CONFIGURATION ---
IMG_SIZE = 64
BATCH_SIZE = 32
NUM_CLASSES = 29
EPOCHS = 12  # We increased this to 12 for better learning

# --- 1. DATA GENERATORS (The Secret Sauce) ---
# This "Data Augmentation" creates fake variations of your images
# (rotates them, zooms them) so the AI learns to handle messy backgrounds.
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=10,      # Rotate hand slightly (10 degrees)
    zoom_range=0.1,         # Zoom in/out (10%)
    width_shift_range=0.1,  # Move hand left/right
    height_shift_range=0.1, # Move hand up/down
    horizontal_flip=True,   # Mirror image (Left hand vs Right hand)
    validation_split=0.2
)

print(f"Loading data from: {DATA_DIR}")

train_generator = train_datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

val_generator = train_datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# --- 2. BUILD THE MODEL ---
model = Sequential([
    # Layer 1: Detects simple lines
    Conv2D(64, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    MaxPooling2D(2, 2),
    
    # Layer 2: Detects shapes (curves, fingers)
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    
    # Layer 3: Detects complex hand parts (thumb vs pinky)
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    
    # Classifier: Decides which letter it is
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5), # Forgets 50% of info to prevent memorizing
    Dense(NUM_CLASSES, activation='softmax')
])

# --- 3. COMPILE AND TRAIN ---
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# This stops training early if the AI stops getting smarter (saves time)
callback = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

print(f"\nStarting Training for {EPOCHS} Epochs (Target: 95% Accuracy)...")
model.fit(train_generator, epochs=EPOCHS, validation_data=val_generator, callbacks=[callback])

# --- 4. SAVE WITH NEW NAME ---
model.save('sign_language_model_95.h5')
print("\nSUCCESS! Model saved as 'sign_language_model_95.h5'")