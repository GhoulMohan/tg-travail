from file import *
from pile import *

def inverse(file):
    p = Pile()
    file_inversee = File()
    while not file.est_vide():
        pile.empile(file.defile())
    while not pile.est_vide():
        file_inversee.enfile(pile.depile())
    return file_inversee

def separe(file):
    file_pair = File()
    file_impair = File()
    while not file.est_vide():
        x = file.defile()
        if element % 2 == 0:
            file_pair.enfile(x)
        else :
            file_impair.enfile(x)
    return pair, impair

