from tkinter import filedialog
import os


def choose_folder():
    return filedialog.askdirectory()

#-----------------------------------------------------------------------------------------------------------------#

def select_and_organize(chosen_folder):
    if os.path.isdir(chosen_folder): 
        organize_files(chosen_folder)
        
#-----------------------------------------------------------------------------------------------------------------#

def create_folders(Extensions, files, chosen_folder):
    for folder in Extensions.keys():
        if folder not in files: os.mkdir(f"{chosen_folder}/{folder}")

#-----------------------------------------------------------------------------------------------------------------#

def organize_files(chosen_folder):
    Extensions = {
    "Texts": (".txt", ".odt", ".docx", ".rtf", ".md"),
    "Images": (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".svg", ".webp"),
    "Excel": (".xlsx", ".xls", ".ods", ".csv"),
    "PDF": (".pdf",),
    "Powerpoint": (".pptx", ".odp", ".ppt"),
    "Applications": (".exe", ".msi"),
    "Videos": (".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"),
    "Audio": (".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"),
    "Compressed": (".zip", ".rar", ".7z", ".tar", ".gz"),
    "Scripts": (".py", ".js", ".java", ".c", ".cpp", ".sh", ".bat"),
    "Fonts": (".ttf", ".otf", ".woff", ".woff2")
}
        
    files = os.listdir(chosen_folder)
    create_folders(Extensions, files, chosen_folder)
    for file in files:
        for archive, extension in Extensions.items():
            if file.lower().endswith(extension):
                file_to_folder(chosen_folder, archive, file)

#-----------------------------------------------------------------------------------------------------------------#

def file_to_folder(chosen_folder, folder, file):
    origem = os.path.join(chosen_folder, file)
    destino = os.path.join(chosen_folder, folder, file)
    destino = check_existence(destino)
    os.rename(origem, destino)

#-----------------------------------------------------------------------------------------------------------------#

def check_existence(destino):
    if os.path.exists(destino):
        base, ext = os.path.splitext(destino)
        i=1
        while os.path.exists(f"{base}_{i}{ext}"):
            i += 1
        return f"{base}_{i}{ext}"
    return destino