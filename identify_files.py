import os
import magic
import shutil
import mimetypes

def identify_file_type(file_path):
    try:
        file_type = magic.from_file(file_path, mime=True)
    except Exception as e:
        print(f"Error identifying file type for {file_path}: {e}")
        return None
    return file_type

def identify_files_in_directory(directory_path):
    print("\n")
    print("#" * 85)  # Separator line
    print("📂 Scanning directory:", directory_path)
    print("-" * 85)  # Separator line
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_type = identify_file_type(file_path)
            
            # Get the current file extension
            file_base_name, file_current_ext = os.path.splitext(file)
            
            # Check if the current extension matches the identified extension
            if file_current_ext:
                print(f'📄 File: {file}\n   🗂️ Type: {file_type}\n   ✅ Already has an extension: {file_current_ext}\n')
            else:
                # Guess the file extension based on the MIME type
                file_ext = mimetypes.guess_extension(file_type)
                
                # If guess_extension returns None, fallback to '.dat' extension
                if not file_ext:
                    file_ext = '.dat'
                
                new_file_name = f"{file_base_name}{file_ext}"
                new_file_path = os.path.join(root, new_file_name)
                
                # Rename the file only if the new name is different from the current name
                if new_file_path != file_path:
                    shutil.move(file_path, new_file_path)  # Use shutil.move for renaming
                    print(f'📄 File: {file}\n   🗂️ Type: {file_type}\n   ❌ Missing extension!\n   ✅ Renamed to: {new_file_name}\n')
    
    print("=" * 85)  # Separator line
    print("✅ Scan and correction complete.")

directory_path = 'C:\\Users\\Your\\Path\\Here'
identify_files_in_directory(directory_path)
