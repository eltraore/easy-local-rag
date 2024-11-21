import shutil
import os
from download_from_s3 import download_files_from_s3
from extract_pdf_text import extract_texts_from_folder
from ollama_interface import ask_question_with_ollama

def main():
    # Étape 1 : Télécharger les fichiers depuis S3
    print("Téléchargement des fichiers depuis S3...")
    download_files_from_s3()

    # Étape 2 : Extraire le texte des fichiers PDF téléchargés
    print("Extraction des textes des fichiers PDF...")
    pdf_folder = "downloaded_files"  # Le dossier où les PDF sont téléchargés
    texts = extract_texts_from_folder(pdf_folder)

    # Combiner tous les textes extraits pour constituer un contexte
    context = " ".join(texts)

    # Étape 3 : Poser une question à Ollama
    query = input("Entrez votre question : ")

    print("\nGénération de la réponse ...")
    answer = ask_question_with_ollama(context, query)

    # Afficher la réponse générée
    print("\nRéponse générée :")
    print(answer)

    # Supprimer le dossier __pycache__ s'il existe
    remove_pycache()

def remove_pycache():
    pycache_path = "__pycache__"
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)

if __name__ == "__main__":
    main()
