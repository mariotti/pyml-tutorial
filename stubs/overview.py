#! /usr/bin/python
#
import sys
sys.path.append("../pylib/")

from pyml_dataread import pyml_dataread

def overview_run():
    pm_reader = pyml_dataread()
    pm_reader.set_filename("../data/u.data")
    amat = pm_reader.read_ascii_umrd()

    if (pm_reader.has_m_numpy):
        print 'Number of users', amat.shape[0]
        print 'Number of movies', amat.shape[1]
        print 'Number of ratings', amat.nnz
        print 'Max rating', amat.tocoo().data.max()
    else:
        print 'Number of users', len(amat)
        print 'Number of movies', len(amat[0])
        print 'Number of ratings', sum(sum(1 for i in row if i) for row in amat)
        # Equivament: print 'Number of ratings', sum(1  for row in amat for i in row if i)
        print 'Max rating', max(map(max,zip(*amat)))
        # To check:  [(min(a), max(a)) for a in zip(*calib)] / http://stackoverflow.com/questions/21639010/python-2-7-find-min-max-on-list-of-lists

#==============================================================================

if __name__ == '__main__':

    #Load Some utility functions

    #Start the test
    overview_run()

