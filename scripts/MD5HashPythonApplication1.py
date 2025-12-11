import hashlib
import os

def md5_hash_file(file_path: str) -> str:
    """
    Generate the MD5 hash of a file's contents.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            # Read file in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                md5.update(chunk)
    except Exception as e:
        raise IOError(f"Error reading file: {e}")

    return md5.hexdigest()

if __name__ == "__main__":
    while True:
        path = input("Enter file path: ")
        try:
            print("MD5 Hash:", md5_hash_file(path))
        except Exception as e:
            print("Error:", e)

        choice = input("Try again? (y/n): ")
        if choice.lower() == 'n':
            break
