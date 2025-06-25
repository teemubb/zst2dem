import sys
from pathlib import Path
import zstandard as zstd

class ProgressReader:
    """
    File-like wrapper to track and display decompression progress by showing how much of the input file stream has been read.

    Attributes:
        f (file object): The original file being wrapped.
        total_size (int): Total size of the file in bytes.
        read_bytes (int): Number of bytes read so far.
    
    """
    def __init__(self, f, total_size):
        self.f = f
        self.total_size = total_size
        self.read_bytes = 0

    def read(self, size=-1):
        chunk = self.f.read(size)
        if chunk:
            self.read_bytes += len(chunk)
            self.show_progress()
        return chunk

    def show_progress(self):
        percent = self.read_bytes / self.total_size * 100
        bar_len = 30

        filled_len = int(bar_len * self.read_bytes // self.total_size)
        bar = '#' * filled_len + '-' * (bar_len - filled_len)
        print(f'\rProgress: [{bar}] {percent:6.2f}%', end='', flush=True) # Update the progress bar displayed in console


def decompress_zst_file(input_path, output_name):
    """
    Decompresses the input .zst file and gives the output as a .dem file by default.

    Args:
        input_path (str or Path): Path to the .zst input file.
        output_name (str): Filename to use for the output file.

    Returns:
        None
    """
    path = Path(input_path)
    output_path = path.parent / f"{output_name}.dem" #User input with .dem extension as default for output file, can be changed
    total_size = path.stat().st_size # Input file size for progress

    with open(path, 'rb') as compressed, open(output_path, 'wb') as destination:
        progress_reader = ProgressReader(compressed, total_size) # Wrap to ProgressReader for progress display...
        dctx = zstd.ZstdDecompressor()
        dctx.copy_stream(progress_reader, destination)

    print(f'\nDone! File unpacked to:\n{output_path.resolve()}')


if __name__ == "__main__":
    """
    Entry point for the script. Checks arguments and runs decompression logic.
    """
    if len(sys.argv) != 2:
        print("Drag a .zst file onto this script or .exe")
        input("Press Enter to exit...")
        sys.exit(1)

    input_path = sys.argv[1]
    output_name = input("Enter new filename (without extension): ").strip()

    if not output_name:
        print("No filename entered. Exiting.")
        sys.exit(1)

    decompress_zst_file(input_path, output_name)
    input("Press Enter to exit...")




