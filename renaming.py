import os

def rename_files_sequentially(folder_path=".", prefix="file_", extension=".txt"):
    """
    Renames files in a specified folder using a sequential naming pattern.

    Args:
        folder_path (str): The path to the folder containing the files.
                           Defaults to "." (the current directory).
        prefix (str): The prefix for the new file names (e.g., "file_").
        extension (str): The desired extension for the renamed files.
                         Only files with the NEW extension will be considered 
                         for renaming if they are already in the folder, 
                         to avoid renaming the renamed files infinitely.
    """
    try:
        # Get a list of all items in the folder
        items = os.listdir(folder_path)
        
        # Filter for files (not directories) and optionally by the NEW extension
        # We only consider files that DON'T match the prefix to avoid infinite renaming
        files_to_rename = [
            item for item in items 
            if os.path.isfile(os.path.join(folder_path, item)) 
            # Check if the file name does NOT start with the new prefix
            and not item.startswith(prefix) 
        ]
        
        # Sort the files to ensure a consistent, predictable renaming order
        files_to_rename.sort()

        print(f"--- Found {len(files_to_rename)} files to rename in '{folder_path}' ---")

        # Iterate through the files and rename them
        for index, old_name in enumerate(files_to_rename, start=1):
            # 1. Create the new file name (e.g., "file_1.txt", "file_2.txt")
            new_name = f"{prefix}{index}{extension}"

            # 2. Construct the full old and new paths
            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)

            # 3. Perform the renaming operation
            os.rename(old_path, new_path)
            
            print(f"Renamed: '{old_name}' -> '{new_name}'")

        print("--- Renaming complete ---")

    except FileNotFoundError:
        print(f"Error: Folder not found at path: {folder_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Execution ---

# ⚠️ IMPORTANT: 
# 1. Create a test folder with some dummy files (e.g., "report.pdf", "image.jpg", "document.doc")
# 2. Change the folder_to_work_on variable to the path of your test folder, 
#    or keep it as "." to run in the current directory.
folder_to_work_on =  "file_1.txt"

# Create the test directory if it doesn't exist (for easy testing)
if not os.path.exists(folder_to_work_on):
    os.makedirs(folder_to_work_on)
    print(f"Created directory: {folder_to_work_on}")
    # Create some dummy files for testing
    with open(os.path.join(folder_to_work_on, "file_1.txt"), "w") as f: f.write("a")
    with open(os.path.join(folder_to_work_on, "file_2.txt"), "w") as f: f.write("b")
    with open(os.path.join(folder_to_work_on, "file_3.txt"), "w") as f: f.write("c")
    print("Created 3 dummy files for testing.")


# Call the function to perform the renaming
# The files will be renamed to "file_1.txt", "file_2.txt", "file_3.txt", etc.
rename_files_sequentially(
    folder_path=folder_to_work_on, 
    prefix="asset_",      # New prefix
    extension=".md"       # New extension (optional change)
)