import os

import hash_file

MODES = {
    0: "Recursive in a single directory",
    1: "Comparision between dir1 & dir2",
    2: "Comparision between dir1 & dir2 with recursion",
}

class FindDuplicateFiles:

    def __init__(self, dir1, dir2=None, recursive=False) -> None:
        self.dir1 = dir1
        self.dir2 = dir2
        self.recursive = recursive

        if not self.is_valid_path(self.dir1):
            self.raise_dir_error(self.dir1)

        self.mode = self.find_mode()
    
    def files(self):
        if self.mode == 0:
            return os.walk(self.dir1)
        elif self.mode == 1:
            return [os.listdir(self.dir1), os.listdir(self.dir2)]
        else:
            return [os.walk(self.dir1), os.walk(self.dir2)]

    def find_duplicates(self):
        if self.mode == 0:
            return self.duplicates_mode0() 

    def duplicates_mode0(self):
        hash_digest = {}
        dup_dict = {}

        for root_dir, _, file_names in self.files():
            for file_name in file_names:
                hash_obj = hash_file.HashFile("sha1")
                hashDigest = hash_obj.hash_file(root_dir, file_name)
                if hash_digest.get(hashDigest, False):
                    dup_dict.setdefault(hashDigest, [])
                    dup_dict[hashDigest].append(root_dir + '/' + file_name)
                    dup_dict[hashDigest].append(hash_digest.get(hashDigest))
                    continue
                hash_digest[hashDigest] = root_dir + '/' + file_name
        return hash_digest, dup_dict  

    def find_mode(self):
        mode = 0
        if self.dir2:
            if self.recursive:
                mode = 2
            else:
                mode = 1
        return mode

    def raise_dir_error(self, dir):
        raise ValueError("Not a Valid Path - %s", dir)

    def is_valid_file(self, file):
        return os.path.isfile(file)

    def is_valid_path(self, file_path):
        return os.path.isdir(file_path)


if __name__ == "__main__":
    dir1 = input("Enter the directory - dir1: ")
    obj = FindDuplicateFiles(dir1)
    hash, duplicate_files = obj.find_duplicates()
    

    if duplicate_files:
        for _, v in duplicate_files.items():
            print(v[0] + "|" + v[1])
            if v[2:]:
                for file in v[2:]:
                    print(" " * len(v[0]) + "|" + file)
            print()
