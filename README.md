<div align="center">
  <img src="https://img.icons8.com/color/96/000000/traffic-jam.png" alt="Logo">
  
  # 🚗 Pakistan ANPR System
  **Production-Grade Automatic Number Plate Recognition**
  
  *🎓 6th Semester Digital Image Processing (DIP) Project | Automated Monitoring & Enforcement*

  [![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
  [![Next.js](https://img.shields.io/badge/Next.js_15-000000?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
  [![YOLOv8](https://img.shields.io/badge/YOLOv8-FF1493?style=for-the-badge&logo=ultralytics&logoColor=white)](https://ultralytics.com/)
  [![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
</div>

<br />

> A comprehensive, highly-localized **Automatic Number Plate Recognition (ANPR)** system engineered specifically for the Pakistani context. This project fuses state-of-the-art Computer Vision (YOLOv8) and Deep Learning OCR (EasyOCR) to provide a robust, real-time vehicle monitoring solution backed by a beautiful full-stack dashboard.

---

## 🏛️ System Architecture

Our system follows a modular, service-oriented architecture designed for high throughput, strict security, and zero-latency video processing.

```mermaid
graph TD
    subgraph Frontend [Next.js Analytics Dashboard]
        UI[Live Camera Feed]
        D[Metrics & History Charts]
    end

    subgraph Backend [FastAPI Server]
        direction TB
        WS[WebSocket Manager]
        YOLO[YOLOv8 Character-Level Detector]
        TRACK[Vehicle Tracker & Temporal Smoothing]
        OCR[Multi-Variant OCR Engine]
        NORM[Pakistan Format Normalizer]
    end

    subgraph Storage [Persistence Layer]
        DB[(SQLite Database)]
        DISK[Evidence Storage System]
    end

    UI -- Base64 Frame --> WS
    WS --> YOLO
    YOLO --> TRACK
    TRACK --> OCR
    OCR --> NORM
    NORM --> DB
    NORM --> DISK
    NORM -- JSON Response --> WS
    WS -- Real-time Sync --> D
    
    classDef frontend fill:#000000,stroke:#333,stroke-width:2px,color:#fff;
    classDef backend fill:#009688,stroke:#333,stroke-width:2px,color:#fff;
    classDef storage fill:#3776AB,stroke:#333,stroke-width:2px,color:#fff;
    
    class UI,D frontend;
    class WS,YOLO,TRACK,OCR,NORM backend;
    class DB,DISK storage;
```

---

## 🔍 The ANPR Pipeline (Under the Hood)

We didn't just use a basic model; we built an entire image enhancement pipeline to ensure plates are readable even in terrible conditions (nighttime, motion blur, fog).

```mermaid
sequenceDiagram
    participant I as Image Input
    participant D as Smart Diagnosis
    participant E as Pre-Detection Enhancer
    participant Y as YOLOv8 (37 Classes)
    participant C as Plate Cropper
    participant O as EasyOCR
    
    I->>D: 1. Evaluate Blur & Light
    D->>E: 2. Apply LIME/CLAHE & Deblur
    E->>Y: 3. Detect Bounding Boxes
    Y->>C: 4. Extract Plate Region
    C->>O: 5. Multi-Variant OCR Scoring
    O-->>I: 6. Cleaned Pakistani Plate Text
```

---

## ✨ Key Features & Localized Context

Unlike generic ANPR systems, this project is fine-tuned for the unique rules and aesthetics of Pakistani license plates:

*   🎯 **Character-Level YOLOv8 Model:** Our model detects 37 unique classes (A-Z, 0-9, and the plate boundary). By understanding characters rather than just a blurry rectangle, we ensure high precision in low lighting.
*   🇵🇰 **Universal Smart Card Support:** Built-in regex parsing for the latest Punjab/Sindh Universal Series (e.g., `AAA-123`, `AZ-123-456`) alongside legacy city codes (`LEA-1234`).
*   ⚖️ **Temporal Smoothing (Stability Fix):** Built a custom `VehicleTracker` that uses a majority-voting algorithm over a 7-frame window. This ensures the "Live" text feed remains rock-solid and flicker-free, even on fast-moving cars.
*   📸 **Cryptographic Evidence Storage:** Automatically saves high-resolution crops of every detected plate in `uploads/evidence/` for legal verification.
*   🚀 **Graceful Degradation:** Smart CPU/GPU detection limits aggressive enhancements on live video streams to maintain high FPS while employing maximum AI power on static image uploads.

---

## 💾 Database Schema (Entity Relationship)

```mermaid
erDiagram
    DETECTION {
        uuid id PK
        string plate_text
        float confidence
        json bbox
        string crop_path "Evidence Image"
        datetime detected_at
    }
    UNAUTHORIZED_LOG {
        int id PK
        string plate_number
        string location
        datetime detected_at
    }
    AUTHORIZED_VEHICLE {
        int id PK
        string plate_number
        string owner_name
    }
    
    DETECTION ||--o| UNAUTHORIZED_LOG : "triggers (if unfound)"
    DETECTION }|--o| AUTHORIZED_VEHICLE : "fuzzy matches"
```

---

## 📈 Analytics & Academic Evaluation

The system includes a dedicated **Evaluation Service** designed to prove algorithmic efficiency for academic grading:

- **mAP (Mean Average Precision):** Evaluated against the Roboflow ANPR dataset.
- **F1-Score Proxy:** Uses high-confidence reads vs low-confidence reads to estimate real-world Precision/Recall.
- **Throughput:** Real-time FPS monitoring and per-stage latency tracking (Diagnosis -> Lighting -> Deblur -> Detection -> OCR).

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- **Python 3.13** (Windows/Linux/Mac)
- **Node.js 20+**
- **Git**

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/rayyan123571/Automated-Number-plate-Recognition.git
cd Automated-Number-plate-Recognition

# Backend Setup
cd backend
python -m venv .venv
# Activate (Windows)
.\.venv\Scripts\activate
# Activate (Linux/Mac)
source .venv/bin/activate
pip install -r requirements.txt

# Frontend Setup
cd ../frontend
npm install
```

### 3. Execution
- **Run Backend:** `start_backend.bat` (API on Port 8000)
- **Run Frontend:** `start_frontend.bat` (Dashboard on Port 3000)

---

## 🛠️ Engineering Standards

- **Backend:** Clean Architecture with Dependency Injection (FastAPI).
- **Frontend:** Glassmorphism UI using Tailwind CSS v4 and Framer Motion.
- **State Management:** TanStack Query for high-performance WebSocket data syncing.
- **Database:** SQLite with SQLAlchemy 2.x for lightweight but powerful persistence.

---

## 👥 Meet the Developers

This project was architected, trained, and developed by:

*   💻 **[@DanishButt586](https://github.com/DanishButt586)** — Full-Stack Integration & System Architecture
*   🧠 **[@rayyan123571](https://github.com/rayyan123571)** — Computer Vision, YOLOv8 Training, & OCR Optimization

*For any inquiries regarding the dataset, model weights, or system architecture, please reach out via GitHub issues.*

---

## 📄 License & Academic Integrity
This project is for academic purposes as part of the 6th Semester Digital Image Processing (DIP) curriculum. Distributed under the MIT License.
