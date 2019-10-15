import hashlib


def hash_folder(dirpath):
    """Finds the MD5 hash for each file in a directory tree.  Recursively walks a folder hierarchy."""
    for root, dirs, files in os.walk(dirpath):
        for filename in files:
            file_hexdigest = hash_file(filename)
            yield (os.path.join(root, filename), file_hexdigest)
    

def hash_file(fname):
    """Finds the MD5 hash for the file whose path is specified by fname."""
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
