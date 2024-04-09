from PIL import Image
import pytesseract  # type: ignore

# image_name = "plaque-immatriculation.png"
image_name = "dify__1.jpg"
image_path = f"C:\\Users\\Choaib ELMADI\\Downloads\\D.I.F.Y\\Web Development\\Web Dev\\9) Python\\Useful Python Scripts\\Assets\\{ image_name }"


def extract_text(image, lang):
    img = Image.open(image)

    tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    extracted_text = pytesseract.image_to_string(img, lang=lang)
    processed_text = " ".join(extracted_text.split())

    return processed_text


text = extract_text(image_path, lang="eng")
print(text)
