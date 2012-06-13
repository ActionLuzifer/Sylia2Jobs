#!/usr/bin/python3

'''
Created on 13.06.2012

@author: ActionLuzifer
'''

import sys

from SyliaToJobs.SyliaToJobs import SyliaToJobs

if __name__ == '__main__':
    stj = SyliaToJobs(sys.argv)
    stj.run()


