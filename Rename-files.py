import os

def rename_images(folder_path):
    file_extension = ".jpg"  # Change to ".jpeg" if necessary
    counter = 1

    for filename in os.listdir(folder_path):
        if filename.endswith(file_extension):
            old_name = os.path.join(folder_path, filename)
            new_name = os.path.join(folder_path, str(counter) + file_extension)

            os.rename(old_name, new_name)
            counter += 1

    print("Images renamed successfully!")

# Folrder Path
#folder_path = "path/to/folder"  # Replace with your folder path
rename_images(folder_path)
