#! /usr/bin/python
#
import sys
sys.path.append("../pylib/")

from pyml_dataread import pyml_dataread

def overview_run():
    pm_reader = pyml_dataread()
    pm_reader.set_filename("../data/u.data")
    pm_reader.read_ascii_umrd()


#==============================================================================

if __name__ == '__main__':

    #Load Some utility functions

    #Start the test
    overview_run()

