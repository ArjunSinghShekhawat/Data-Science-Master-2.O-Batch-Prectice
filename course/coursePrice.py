import os,sys
from os.path import abspath,join,dirname

sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from payment import coursePayment


def price():
    print("Course price 2000")

coursePayment.payment()