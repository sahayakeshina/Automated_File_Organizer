import os
import shutil

source_folder = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        moved = False

        for folder_name, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                destination = os.path.join(source_folder, folder_name)

                if not os.path.exists(destination):
                    os.makedirs(destination)

                shutil.move(file_path, os.path.join(destination, filename))
                moved = True
                break

        if not moved:
            others = os.path.join(source_folder, "Others")

            if not os.path.exists(others):
                os.makedirs(others)

            shutil.move(file_path, os.path.join(others, filename))
print("Files organized successfully!")