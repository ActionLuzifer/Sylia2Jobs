'''
Created on 13.06.2012

@author: duncanmcleod
'''

import os
import sys

def getListOfSyliaFiles(path):
    files = os.listdir(path)
    files=[filename for filename in files if filename.endswith("syl")]
    files.sort()
    return files

if __name__ == '__main__':
    if len(sys.argv)>1:
        pass
        print(sys.argv[0])
        print(sys.argv[1])
    # Sylia-Dateien suchen
    # Inhalte der Sylia-Dateien in einen Text (Jobs) einfügen
        # Header und Footer drumherum legen
    # Header und Footer an Jobs anlegen
    # Jobs-Datei speichern
    pass


