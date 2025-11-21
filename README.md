# Real-Time Sign Language Detector (ASL)

## 📌 Project Overview
This capstone project implements a real-time Computer Vision system capable of translating American Sign Language (ASL) finger spelling into text.

The system utilizes a **Convolutional Neural Network (CNN)** trained on the ASL Alphabet dataset (87,000 images). It captures video frames via OpenCV, processes them for feature extraction, and performs real-time inference to classify hand gestures into 29 distinct classes (A-Z, Space, Delete, Nothing).

## 👥 Project Team & Phases
This project was executed in five distinct phases, with team members leading specific components of the pipeline:

* **Phase 1: Environment Setup**
    * **Lead:** Phavan Phani Meka (Setup Lead)
    * *Focus: Configuration of Python 3.10 environments, Anaconda, and library dependencies.*

* **Phase 2: Data Collection**
    * **Lead:** Rohini Mandepula (Data Collector)
    * *Focus: Acquisition and verification of the ASL Alphabet dataset.*

* **Phase 3: Data Labeling & Preparation**
    * **Lead:** Vamsi Maguluri (Labeler/Prep)
    * *Focus: Image preprocessing, resizing (64x64), and categorical label encoding.*

* **Phase 4: Azure & Model Training**
    * **Lead:** Anusha Venkatesh (Training Lead)
    * *Focus: CNN architecture design and training execution.*

* **Phase 5: Deployment & Integration**
    * **Lead:** Mounika Mercharapu (Deployment Lead)
    * *Focus: Real-time inference script and webcam integration.*

## 🛠️ Technical Architecture
* **Deep Learning:** TensorFlow / Keras (Sequential CNN Model)
* **Computer Vision:** OpenCV (cv2) for frame capture and preprocessing
* **Language:** Python 3.10
* **Data:** Trained on 64x64 RGB images normalized to [0,1] range.

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/VamsiMaguluri/ASL-Sign-Language-Detector.git