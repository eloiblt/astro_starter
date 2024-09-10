import os

def add_header_to_markdown_files(folder_path):
    ## Parcourir tous les fichiers et sous-dossiers du dossier spécifié
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                add_header(file_path)

def add_header(file_path):
    ## Lire le contenu du fichier
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    ## Vérifier si la deuxième ligne commence par 'title:'
    if len(content) > 1 and content[1].lower().startswith('title:'):
        print(f"Le fichier {file_path} a déjà un titre à la deuxième ligne. Ignoré.")
        return

    ## Obtenir le nom du fichier sans extension
    file_name = os.path.basename(file_path).replace(".md", "")

    ## Préparer le nouvel en-tête à ajouter
    header = [
        "---\n",
        f'title: "{file_name}"\n',
        "---\n",
        "\n"  ## Ligne vide
    ]

    ## Ecrire l'en-tête suivi du contenu existant
    with open(file_path, "w", encoding="utf-8") as file:
        print(file_name + " done")
        file.writelines(header + content)

## Utiliser le dossier courant
current_folder = os.getcwd()
add_header_to_markdown_files(current_folder)
