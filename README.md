# 📄 SwiftScan — Python Mobile Document Scanner

SwiftScan is a **Python-based mobile document scanner** built with **Kivy + OpenCV**.  
It captures documents using a camera, automatically detects page edges, corrects perspective, enhances readability, exports to PDF, and supports OCR and QR code scanning.

This project is inspired by apps like **CamScanner** and **Adobe Scan**, but built entirely in Python for learning and experimentation.

---

## ✨ Features

- 📸 Camera capture (Kivy)
- ✂️ Automatic document edge detection
- 📐 Perspective correction (scan-like flattening)
- 🎨 Image enhancement (adaptive thresholding)
- 📄 Export scanned documents to PDF
- 🔍 OCR (text extraction using Tesseract)
- 📦 QR / Barcode scanning support
- 🧪 Modular computer vision pipeline

---

## 🧠 How It Works (High-Level)
```commandline
Camera
↓
Image Capture
↓
Edge Detection (OpenCV)
↓
Contour Detection (find document)
↓
Perspective Transform (flatten page)
↓
Image Enhancement
↓
PDF Export / OCR / QR Scan
```


---

## 🛠 Tech Stack

| Component | Technology |
|--------|------------|
UI | Kivy |
Image Processing | OpenCV |
Math / Arrays | NumPy |
PDF Export | FPDF |
OCR | Tesseract + pytesseract |
QR / Barcode | pyzbar |
Language | Python 3 |

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/davex-ai/SwiftScan.git
cd SwiftScan

```
---

## 🛠 Tech Stack

| Component | Technology |
|--------|------------|
UI | Kivy |
Image Processing | OpenCV |
Math / Arrays | NumPy |
PDF Export | FPDF |
OCR | Tesseract + pytesseract |
QR / Barcode | pyzbar |
Language | Python 3 |

---

### 2️⃣ Create virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate   # Windows
### 3️⃣ Install Python dependencies
pip install -r requirements.txt
### 🔤 Install Tesseract OCR (Required for OCR)
Windows
Download from:
https://github.com/UB-Mannheim/tesseract/wiki

Install and check “Add to PATH”

Default path:
```commandline

C:\Program Files\Tesseract-OCR\tesseract.exe
Verify installation
tesseract --version
⚙️ Configure Tesseract Path (Important)
Add this to your Python file:

import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
```
### ▶️ Running the App
python scannerApp.py
Click Capture

Document is detected and scanned

Output files:

scanned_final.png

document.pdf

OCR text printed to console

### 📷 QR / Barcode Scanning
QR codes are detected using pyzbar:
```python

from pyzbar import pyzbar

barcodes = pyzbar.decode(image)
for barcode in barcodes:
    print(barcode.data.decode("utf-8"))
```
⚠️ Notes

Python 3.10–3.11 is recommended for best compatibility

OCR requires Tesseract installed system-wide

Mobile packaging requires Linux (Buildozer)

📜 License

MIT License — free to use, modify, and learn from.

👤 Author

Built by [Dave](https://github.com/davex-ai)
Learning computer vision, mobile development, and systems-level debugging the hard (real) way.
