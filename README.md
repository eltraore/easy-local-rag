# Application de Chat Basée sur RAG avec Ollama

Ce projet est une démonstration d'une application de chat utilisant la technique **RAG (Retrieval-Augmented Generation)**, combinée à **Ollama** pour le traitement du langage naturel. Il intègre **AWS S3** pour la récupération de documents, extrait le texte des fichiers PDF téléchargés, et permet aux utilisateurs de poser des questions de manière interactive.

---

## Fonctionnalités

- **Intégration AWS S3** : Téléchargement automatique de fichiers PDF depuis un bucket S3.
- **Extraction de Texte des PDF** : Analyse et extraction du texte des fichiers PDF pour créer un contexte de réponse.
- **Intégration avec Ollama** : Utilisation du modèle `llama3.2` pour générer des réponses aux questions posées.
- **Chat Interactif** : Les utilisateurs peuvent poser plusieurs questions dans une même session.
- **Nettoyage Automatique** : Suppression des fichiers temporaires comme `__pycache__` après exécution.

---

## Prérequis

1. **Python 3.8 ou une version ultérieure+**
2. **Bucket AWS S3** Contenant des fichiers PDF.
3. **Ollama** Installez Ollama sur votre machine (https://ollama.com/download).
4. **Bibliothèques Python nécessaires** :
   - `boto3`
   - `PyPDF2`
   - `python-dotenv`

---

## Installation

1. **Clonez ce dépôt :**
  ```bash
  git clone https://github.com/eltraore/elijah-rag.git
  cd <dossier_du_projet>
  ```

2. **Installez les dépendances :**
  ```bash
  pip install -r requirements.txt
  ```

3. **Configurez un fichier .env avec vos informations AWS :**

  Exemple :
  ```.env
  AWS_ACCESS_KEY=AKIATBRPQSAWM4OI2X42
  AWS_SECRET_KEY=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
  AWS_REGION=eu-west-3  
  BUCKET_NAME=rag-docs-elijah 
  ```

---

## Structure du Projet

```Structure
.
├── download_from_s3.py      # Gestion du téléchargement des fichiers depuis S3
├── extract_pdf_text.py      # Extraction de texte des fichiers PDF
├── ollama_interface.py      # Interaction avec le modèle Ollama
├── main.py                  # Orchestration de l'application
├── gui.py                   # Orchestration de l'application (avec interface utilisateur (GUI))
├── requirements.txt         # Dépendances du projet
├── README.md                # Documentation du projet
├── .env                     # Variables d'environnement (non inclus dans le dépôt)
└── downloaded_files/        # Contient les fichiers PDF téléchargés depuis S3 (non inclus dans le dépôt, se rajoute automatiquement lorsque l'application se lance)
```

---

## Utilisation

1. **Lancez l'application :**
  ```bash
  python3 main.py
  ```

2. **Suivez les instructions :**
  - L'application télécharge automatiquement les fichiers PDF depuis votre bucket S3.
  - Elle extrait le texte des fichiers pour constituer un contexte.
  - Posez vos questions et recevez des réponses générées par Ollama.

3. **Quittez l'application en tapant "quit" ou en fermant la console.**

---

## Bonus : Utilisation avec Interface Graphique (GUI)

Dans ce bonus, nous ajoutons une interface graphique **(GUI)** à l'application de chat basée sur RAG, utilisant **Tkinter** pour une expérience utilisateur améliorée.

1. **Lancez l'application GUI :** Pour démarrer l'application avec l'interface graphique, exécutez le fichier `gui.py` :
  ```bash
  python3 gui.py
  ```
  Une interface graphique doit s'ouvrir.

2. **Posez une question :**
- Tapez votre question dans la zone "Posez une question".
- Cliquez sur le bouton "Poser la question" pour envoyer la question au modèle Ollama.

3. **Affiche la réponse :**
- La réponse générée par le modèle Ollama sera affichée dans le champ "Réponse" sous la zone de saisie de la question.

4. **Quittez l'application :**
- Pour fermer l'application, vous pouvez simplement fermer la fenêtre de l'interface graphique.

---

## Contributeur
Elijah TRAORE / elijah.traore9@gmail.com