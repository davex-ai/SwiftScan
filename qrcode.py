import pytesseract

text = pytesseract.image_to_string("scanned_final.png")
print("Detected text:", text)

barcodes = pyzbar.decode(orig)

for barcode in barcodes:
    data = barcode.data.decode("utf-8")
    barcode_type = barcode.type

    print(f"[QR] Type: {barcode_type}")
    print(f"[QR] Data: {data}")
