#!/usr/bin/env python3

import os
import sys

import shlex

def unzip_file(filename):
    escaped_filename = shlex.quote(filename)
    extension = filename.split('.')[-1]
    folder_name = filename.split('.')[0] + "_unzipped"
    escaped_folder_name = shlex.quote(folder_name)
    multi_extension = '.'.join(filename.split('.')[-2:])

    if extension == 'zip':
        command = f"unzip {escaped_filename} -d {escaped_folder_name}"
    elif extension == 'tar':
        command = f"tar -xvf {escaped_filename} -C {escaped_folder_name}"
    elif extension == 'gz':
        command = f"gunzip {escaped_filename}"
    elif multi_extension == 'tar.bz2':
        command = f"tar -xjvf {escaped_filename} -C {escaped_folder_name}"
    else:
        print("Unsupported file type")
        return

    os.makedirs(folder_name, exist_ok=True)
    os.system(command)

    
if __name__ == "__main__":
    unzip_file(sys.argv[1])
