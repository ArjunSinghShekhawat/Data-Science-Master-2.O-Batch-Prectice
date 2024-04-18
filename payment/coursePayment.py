import os,sys
from os.path import abspath,join,dirname

sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from course import coursePrice

def payment():
    print('Course Payment')

coursePrice.price()