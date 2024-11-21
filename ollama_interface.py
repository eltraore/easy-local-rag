import subprocess

def ask_question_with_ollama(question, context, model="llama3.2"):
    """
    Pose une question au modèle Ollama avec un contexte donné.

    Args:
        question (str): La question à poser.
        context (str): Le contexte textuel fourni au modèle.
        model (str): Le modèle Ollama à utiliser (par défaut: llama3.2).

    Returns:
        str: La réponse générée par le modèle.
    """
    prompt = f"Context: {context}\n\nQuestion: {question}"

    # Commande pour exécuter Ollama sans --temperature
    command = ["ollama", "run", model]

    try:
        # Exécution de la commande avec le texte en entrée via stdin
        process = subprocess.run(
            command,
            input=prompt,
            text=True,  # Permet d'envoyer du texte à l'entrée standard
            capture_output=True  # Capture la sortie de la commande
        )

        # Vérification des erreurs d'exécution
        if process.stderr:
            print(f"[DEBUG] Erreur Ollama : {process.stderr.strip()}")

        # Retourner la sortie générée par le modèle, ou un message si aucune réponse
        return process.stdout.strip() if process.stdout else "Pas de réponse du modèle."

    except Exception as e:
        # Gestion des exceptions générales
        return f"Erreur lors de l'exécution du modèle : {e}"
