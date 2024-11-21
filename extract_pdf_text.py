import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    """
    Extrait le texte d'un fichier PDF donné.
    :param pdf_path: Chemin du fichier PDF.
    :return: Le texte extrait du PDF.
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Erreur lors de l'extraction du texte du PDF {pdf_path}: {e}")
        return ""

def extract_texts_from_folder(folder_path):
    """
    Extrait le texte de tous les fichiers PDF dans un dossier.
    :param folder_path: Chemin du dossier contenant les fichiers PDF.
    :return: Liste de textes extraits des fichiers PDF.
    """
    texts = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, file_name)
            print(f"Extraction du texte de {pdf_path}...")
            text = extract_text_from_pdf(pdf_path)
            texts.append(text)
    return texts
