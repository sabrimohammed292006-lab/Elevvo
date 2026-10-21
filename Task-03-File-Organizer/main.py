
import os
import shutil
from pathlib import Path

def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Error: The folder does not exist.")
        return

    for file_path in folder.iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()

            if extension:
                target_folder = folder / extension[1:].upper()
            else:
                target_folder = folder / "Others"

            target_folder.mkdir(exist_ok=True)

            destination = target_folder / file_path.name

            counter = 1
            while destination.exists():
                destination = target_folder / f"{file_path.stem}_{counter}{file_path.suffix}"
                counter += 1

            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name} -> {target_folder.name}/")

    print("File organization completed!")

def main():
    print("=== Automated File Organizer ===")
    folder_path = input("Enter the folder path to organize: ").strip().strip('"')
    organize_files(folder_path)

if __name__ == "__main__":
    main()
