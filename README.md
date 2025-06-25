# zst2dem-script
A simple Python script to decompress `.zst` files.


## Features
- Decompress `.zst` files to `.dem` by default.
- User input filename with option to change the extension.
- Progress bar to track progress in the console


## Requirements
#### Required 
To **run the script directly with Python**, you need:
- Python
- zstandard library (`pip install zstandard`)


#### Optional
To **build a .exe** for easier drag & drop use, you need:
- PyInstaller (`pip install pyinstaller`)


## Usage
1. Run the script by dragging a `.zst` file onto the `.exe` (if compiled) or by command line: `python unpac_zst.py path/to/file.zst`
2. Enter desired output name.
> [!NOTE]  
> If you don't provide an extension, the output file will be `.dem` by default


## Building the .exe
In order to make an executable .exe file for easier drag & drop support:
1. Make sure **pyinstaller** is installed (see requirements).
2. Open a terminal in the project's directory.
3. run `pyinstaller --onefile unpack_zst.py`


