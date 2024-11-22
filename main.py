import os
import shutil
from download_from_s3 import download_files_from_s3
from extract_pdf_text import extract_texts_from_folder
from ollama_interface import ask_question_with_ollama

def main():
    # Étape 1 : Télécharge les fichiers depuis S3
    print("Téléchargement des fichiers depuis S3...")
    download_files_from_s3()

    # Étape 2 : Extrait le texte des fichiers PDF téléchargés
    print("Extraction des textes des fichiers PDF...")
    pdf_folder = "downloaded_files"  
    texts = extract_texts_from_folder(pdf_folder)

    # Combine tous les textes extraits pour constituer un contexte
    context = " ".join(texts)

    # Étape 3 : Boucle pour poser des questions à Ollama
    while True:
        query = input("\nEntrez votre question (ou tapez 'quit' pour quitter) : ")
        
        # Condition pour quitter la boucle
        if query.lower() == 'quit':
            print("Merci d'avoir utilisé l'application. À bientôt !")
            break

        print("\nGénération de la réponse avec Ollama...")
        answer = ask_question_with_ollama(context, query)

        # Afficher la réponse générée
        print("\nRéponse générée :")
        print(answer)

    # Supprime le dossier __pycache__ s'il existe
    remove_pycache()

def remove_pycache():
    """Supprime le dossier __pycache__ s'il existe."""
    pycache_path = "__pycache__"
    try:
        if os.path.exists(pycache_path):
            shutil.rmtree(pycache_path)
    except Exception as e:
        print(f"Erreur lors de la suppression de '{pycache_path}': {e}")

if __name__ == "__main__":
    main()
