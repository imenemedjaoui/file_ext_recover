# File Renaming Script

This script is designed to scan a directory and rename files based on their MIME types. It can be useful for organizing files by type or recovering file extensions.

## Usage

1. **Clone the Repository:**
```bash
git clone https://github.com/imenemedjaoui/file_ext_recover.git
```

2. **Navigate to the Directory:**
```bash
cd your-repository
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Put the Files in the same Directory:**
- Make sure to put the files you want to rename in the same directory as the script.

6. **Run the Script:**
```bash
python rename_files.py
```


## Dependencies

- **Python 3.x**
- **python-magic** 
- **python-magic-bin:** This is a Windows-compatible version of the `python-magic` library.


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
