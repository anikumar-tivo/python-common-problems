__doc__ = 'Problem statement:\
    1. I wanted to list the content of a directory.\
    2. How to list the content of directory and subb-directories?\
    3. Python program to list the content of the directory and sub-directories.'
__author__ = 'Anil Kumar'
__email__ = 'anilkumar.jan28@gmail.com'
__version__ = '1.0'
__date__ = 'Apr 26, 2020'


import os


def is_exists(path):
    return os.path.exists(path);


def is_directory(path):
    return os.path.isdir(path)


def get_dir_contents(directory):
    return os.listdir(directory)


def ldir(directory, subdirectories=False):
    if (not is_exists(directory)):
        raise IOError("Directory does not exists: (%s)" %(directory))
    if (not is_directory(directory)):
        raise IOError("Not a directory: (%s)" %(directory))
    
    result = []
    if (not subdirectories):
        contents = get_dir_contents(directory)
        for content in contents:
            compelete_path = "%s/%s" %(directory, content)
            result.append(compelete_path)
        return result
    
    result = []
    contents = get_dir_contents(directory)
    for content in contents:
        compelete_path = "%s/%s" %(directory, content)
        if (is_directory(compelete_path)):
            result += ldir(compelete_path, subdirectories=True)
            continue
        result.append(compelete_path)
    return result


def print_content(contents):
    count = 0
    for item in contents:
        count += 1
        print "%06d # %s" %(count, item)
    print


if __name__ == "__main__":
    # Normal listing
    dir_contents = ldir("/Users/anikumar/workplace/python-common-problems")
    print_content(dir_contents)

    # Listing content including sub-dircteories
    dir_content_with_subdir = ldir(
        "/Users/anikumar/workplace/python-common-problems",
         subdirectories=True
    )
    print_content(dir_content_with_subdir)
