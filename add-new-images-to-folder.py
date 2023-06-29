import os
# use this code if you have already numbered your images in ascending order
# and now wants to add new images to the folder 
def rename_images(folder_path):
    file_extension = ".jpeg"  # Change to ".jpeg" if necessary

    # Find the highest number used so far
    counter = 1
    existing_numbers = set()

    for filename in os.listdir(folder_path):
        if filename.endswith(file_extension):
            try:
                file_number = int(os.path.splitext(filename)[-0])
                existing_numbers.add(file_number)
                counter = max(counter, file_number)
            except ValueError:
                pass

    # Assign numbers to newly added images
    for filename in os.listdir(folder_path):
        if filename.endswith(file_extension):
            continue  # Skip existing files

        new_name = os.path.join(folder_path, str(counter) + file_extension)

        # Make sure the number is not already used
        while counter in existing_numbers:
            counter += 1

        os.rename(os.path.join(folder_path, filename), new_name)
        counter += 1
        existing_numbers.add(counter - 1)

    print("Images renamed successfully!")

# Folder Path
folder_path = "path/to/folder"  # Replace with your folder path
rename_images(folder_path)
