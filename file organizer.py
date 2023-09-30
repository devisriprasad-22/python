import os
import shutil

# Define a dictionary mapping file extensions to directory names
file_extensions = {
    '.txt': 'TextFiles',
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.png': 'Images',
    '.docx': 'Documents',
    '.xlsx': 'Documents',
    '.mp3': 'Music',
}

def organize_files(source_dir):
    # Create directories for each file type if they don't exist
    for directory in file_extensions.values():
        if not os.path.exists(directory):
            os.mkdir(directory)

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)
        if os.path.isfile(src_path):
            # Get the file extension
            file_ext = os.path.splitext(filename)[1].lower()

            # Determine the destination directory based on the file extension
            dest_dir = file_extensions.get(file_ext, 'Other')
            dest_path = os.path.join(dest_dir, filename)

            # Move the file to the destination directory
            shutil.move(src_path, dest_path)
            print(f"Moved '{filename}' to '{dest_dir}' directory.")

if __name__ == "__main__":
    source_directory = input("Enter the source directory path: ")
    organize_files(source_directory)
    print("File organization complete.")
