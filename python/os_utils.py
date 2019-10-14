""" OS Utils """

import os
import shutil


def list_subfolder_names(path):
    """ Lists folders in path """
    return [o for o in os.listdir(path)
            if os.path.isdir(os.path.join(path, o))]


def create_folder(path):
    """ Creates a folder if it does not exist """
    if os.path.isdir(path):
        return
    try:
        os.mkdir(path)
    except OSError:
        print("Failed to create directory at path %s" % path)
        raise


def copy_directory_recursive(src, dest):
    """ Recursively copies a directory from src to dest """
    try:
        shutil.copytree(src, dest)
    except OSError as err:
        print('Directory not copied. Error: %s' % err)


def remove_directory_recursive(dir_path):
    """ Recursively removes directory at dir_path """
    if not os.path.isdir(dir_path):
        return
    try:
        shutil.rmtree(dir_path)
    except OSError as err:
        print('Directory not removed. Error: %s' % err)


def replace_directory_recursive(src, dest):
    """ Recursively removes dest, then copies src to dest """
    remove_directory_recursive(dest)
    copy_directory_recursive(src, dest)
