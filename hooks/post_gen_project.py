import os
import shutil


def remove_file(file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
    except OSError as e:
        print(f"Error deleting file {file_path}: {e}")


def remove_directory(directory_path):
    try:
        if os.path.isdir(directory_path):
            shutil.rmtree(directory_path)
    except OSError as e:
        print(f"Error deleting directory {directory_path}: {e}")


def main():
    web_pwa = "{{cookiecutter.web_pwa}}".lower()
    web_pwa_enabled = web_pwa not in ["y", "yes", "true", "1"]

    if web_pwa_enabled:
        base_dir = os.path.abspath("assets")

        files_to_remove = [
            os.path.join(base_dir, f) for f in os.listdir(base_dir) if f != "icon.png"
        ]

        for file_path in files_to_remove:
            if os.path.isdir(file_path):
                remove_directory(file_path)
            elif os.path.isfile(file_path):
                remove_file(file_path)


if __name__ == "__main__":
    main()
