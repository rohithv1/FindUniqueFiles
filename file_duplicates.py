# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 09:55:48 2021

@author: Rohith_Vemulapally
"""

import hashlib
import os
import shutil

def hash_file(file):
    
    h = hashlib.sha1()
    
    with open(file, 'rb') as fh:
        chunk = 0
        while chunk != b'':
            chunk = fh.read(1024)
            h.update(chunk)
    return h.hexdigest()


def find_duplicates(path):
    files = os.walk(path)
    hash_digest = {}
    for root_dir, directory, file_names in files:
        for file_name in file_names:
            hashDigest = hash_file(root_dir + '/' + file_name)
            if hash_digest.get(hashDigest, False):
                continue
            hash_digest[hashDigest] = root_dir + '/' + file_name
    return hash_digest

def copy_unique(path,hash_digest):
    # unique_path = path + '/' + "unique"
    os.mkdir(unique_path)
    for k, v in hash_digest.items():
        filename = os.path.basename(v)
        shutil.copyfile(v, path + '/' +filename)
        
if __name__ == "__main__":
    path = input("Enter the Path where duplicates reside: ")
    unique_path = input("Enter the Path where Unique files should be placed: ")
    unique_dict = find_duplicates(path)
    copy_unique(unique_path, unique_dict)
        
    
    
    
    