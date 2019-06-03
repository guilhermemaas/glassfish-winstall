import os.path
import pytest
from os import walk

#http://download.oracle.com/glassfish/4.0/release/glassfish-4.0.zip

def test_directory_exists(directory):
    exists = os.path.isdir(directory)
    assert exists == True

def test_directory_empty(directory):
    empty = os.listdir(directory)
    assert empty == 0

def test_link_glassfish4(link)
