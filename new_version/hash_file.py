import hashlib
import os

HASH_DICT = {
    "sha1": hashlib.sha1(),
    "sha256": hashlib.sha256(),
    "md5": hashlib.md5()
}

class HashFile:

    def __init__(self, hash_type) -> None:
        self.hash_type = hash_type

        if not self.is_valid_hash():
            raise ValueError("Hash type not found in the dictionary")

    def is_valid_hash(self):
        return bool(HASH_DICT.get(self.hash_type, 0))

    def hash_algorithm(self):
        return HASH_DICT.get(self.hash_type)

    def hash_file(self, file_path, file_name):
        algo = hashlib.sha1()
        file = file_path + '/' + file_name 

        with open(file, 'rb') as fh:
            chunk = 0
            while chunk != b'':
                chunk = fh.read(1024)
                algo.update(chunk)
        return algo.hexdigest()



