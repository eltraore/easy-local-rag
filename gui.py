import tkinter as tk
from tkinter import messagebox
from download_from_s3 import download_files_from_s3
from extract_pdf_text import extract_texts_from_folder
from ollama_interface import ask_question_with_ollama
import shutil
import os

class RAGChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat RAG Simplifié")

        # Télécharger les fichiers et extraire automatiquement le contexte au démarrage
        self.context = ""
        self.download_and_extract_context()

        # Zone d'entrée pour poser une question
        self.question_label = tk.Label(root, text="Posez une question :")
        self.question_label.pack()
        self.question_entry = tk.Entry(root, width=80)
        self.question_entry.pack()

        # Bouton pour poser une question
        self.ask_button = tk.Button(root, text="Poser la question", command=self.ask_question)
        self.ask_button.pack()

        # Zone de texte pour afficher la réponse
        self.answer_label = tk.Label(root, text="Réponse :")
        self.answer_label.pack()
        self.answer_text = tk.Text(root, height=5, width=80)
        self.answer_text.pack()

    def download_and_extract_context(self):
        try:
            # Téléchargement des fichiers PDF depuis S3
            print("Téléchargement des fichiers depuis S3...")
            download_files_from_s3()

            # Extraction de texte des fichiers téléchargés
            print("Extraction des textes...")
            pdf_folder = "downloaded_files"
            texts = extract_texts_from_folder(pdf_folder)

            # Stockage du contexte
            self.context = " ".join(texts)
            if not self.context:
                messagebox.showwarning("Attention", "Aucun texte extrait des fichiers téléchargés.")
            else:
                print("Contexte extrait avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
        finally:
            # Nettoyage du dossier __pycache__
            self.cleanup_pycache()

    def ask_question(self):
        try:
            # Vérifier que le contexte existe
            if not self.context:
                messagebox.showwarning("Attention", "Le contexte n'a pas été chargé.")
                return

            # Récupérer la question posée
            question = self.question_entry.get().strip()
            if not question:
                messagebox.showwarning("Attention", "Veuillez entrer une question.")
                return

            # Appel au modèle Ollama pour générer une réponse
            print("Génération de la réponse avec Ollama...")
            answer = ask_question_with_ollama(question, self.context)
            self.answer_text.delete("1.0", tk.END)
            self.answer_text.insert(tk.END, answer)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

    def cleanup_pycache(self):
        """Supprime le dossier __pycache__ s'il existe."""
        try:
            pycache_path = "__pycache__"
            if os.path.exists(pycache_path):
                shutil.rmtree(pycache_path)
        except Exception as e:
            print(f"Erreur lors de la suppression de __pycache__ : {e}")

# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = RAGChatApp(root)
    root.mainloop()
