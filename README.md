# File Renaming Script

This script is designed to scan a directory and rename files based on their MIME types. It can be useful for organizing files by type or correcting file extensions.

## Usage

1. **Clone the Repository:**
git clone https://github.com/imenemedjaoui/file_ext_recover.git


2. **Navigate to the Directory:**
cd your-repository


3. **Install Dependencies:**
pip install -r requirements.txt


4. **Run the Script:**
python rename_files.py


5. **Provide the Directory Path:**
Input the directory path containing the files you want to rename when prompted.


## Dependencies

- **Python 3.x**
- **python-magic:** 
- **python-magic-bin:** 


## When to Use

- **Organizing Files:** Use this script when you have a directory containing files with missing extensions and you want to organize them by type.
- **Standardizing File Extensions:** It's handy when you need to ensure all files have consistent extensions based on their MIME types.


## Notes

- The script uses the `magic` library to determine file MIME types, so it's essential to have it installed.
- If the `mimetypes.guess_extension()` function fails to guess the extension, it defaults to `.dat`. You can modify this behavior as needed in the script.
- The script is safe to run in any directory, as it will not rename files that already have an extension.


## Author

- **Imene Medjaoui**
- **Contact:** medjaoui.imene@gmail.com
