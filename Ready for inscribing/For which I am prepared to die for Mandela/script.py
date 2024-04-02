import fitz  # PyMuPDF
import pytesseract
import re

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(pdf_file) as pdf_document:
        num_pages = pdf_document.page_count
        for page_num in range(num_pages):
            page = pdf_document[page_num]
            text += page.get_text()
    return text


def ocr_extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(pdf_file) as pdf_document:
        num_pages = pdf_document.page_count
        for page_num in range(num_pages):
            page = pdf_document[page_num]
            image = page.get_pixmap()
            image_text = pytesseract.image_to_string(image.rgb, lang='eng')
            text += image_text + "\n\n"
    return text


def fix_text_formatting(text):
    # Split text into paragraphs
    paragraphs = re.split(r'\n\s*\n', text.strip())

    # Wrap each paragraph with <p></p> tags
    formatted_paragraphs = [f"<p>{para.strip()}</p>" for para in paragraphs if para.strip()]

    # Combine paragraphs into a single string
    formatted_text = "\n".join(formatted_paragraphs)
    return formatted_text


def save_as_html(output_file, formatted_text):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'<!DOCTYPE html><html><body>{formatted_text}</body></html>')


if __name__ == "__main__":
    input_pdf_file = "/Users/akyriacou/VisualCode/Project Alexandria/Mandela/1278_mandelaIdeal.pdf"
    output_html_file = "/Users/akyriacou/VisualCode/Project Alexandria/Mandela/mandela.html"

    try:
        text_from_pdf = extract_text_from_pdf(input_pdf_file)
    except RuntimeError:
        print("Text extraction using PyMuPDF failed. Attempting OCR.")
        text_from_pdf = ocr_extract_text_from_pdf(input_pdf_file)

    formatted_text = fix_text_formatting(text_from_pdf)
    save_as_html(output_html_file, formatted_text)
    print("Text formatting is fixed and saved to 'mandela.html'")
