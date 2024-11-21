import boto3
import os
from dotenv import load_dotenv

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupére les informations AWS depuis les variables d'environnement
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Initialise le client S3 avec les informations d'identification
def init_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )

# Fonction pour télécharger le pdf depuis S3
def download_files_from_s3():
    s3 = init_s3_client()

    # Liste les objets dans le bucket S3
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if "Contents" not in response:
        print("Aucun fichier trouvé dans le bucket.")
        return

    # Crée un dossier local pour les fichiers téléchargés
    download_dir = "downloaded_files"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Télécharge chaque fichier du bucket
    for obj in response["Contents"]:
        file_key = obj["Key"] 
        local_file_path = os.path.join(download_dir, os.path.basename(file_key)) 

        print(f"Téléchargement de {file_key} vers {local_file_path}...")
        s3.download_file(BUCKET_NAME, file_key, local_file_path)
        print(f"{file_key} téléchargé avec succès.")

if __name__ == "__main__":
    download_files_from_s3()
