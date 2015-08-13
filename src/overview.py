#! /usr/bin/python
#
import sys
sys.path.append("../pylib/")

from pyml_dataread import pyml_dataread
from pyml_matstats import pyml_matstats

def overview_run():
    pm_reader = pyml_dataread()

    #pm_reader.use_numpy = False
    pm_reader.use_numpy = True
    
    if (pm_reader.use_numpy):
        print "Using Numpy/Scipy"
    else:
        print "NOT Using Numpy/Scipy"
        
    pm_reader.set_filename("../data/u.data")
    amat = pm_reader.read_ascii_umrd()

    if (pm_reader.use_numpy):
        print 'Number of users', amat.shape[0]
        print 'Number of movies', amat.shape[1]
        print 'Number of ratings', amat.nnz
        print 'Max rating', amat.tocoo().data.max()
        print 'Min rating', amat.tocoo().data.min()
    else:
        print 'Number of users', len(amat)
        print 'Number of movies', len(amat[0])
        print 'Number of ratings', sum(sum(1 for i in row if i) for row in amat)
        # Equivament: print 'Number of ratings', sum(1  for row in amat for i in row if i)
        print 'Max rating', max(map(max,zip(*amat)))
        # To check:  [(min(a), max(a)) for a in zip(*calib)] / http://stackoverflow.com/questions/21639010/python-2-7-find-min-max-on-list-of-lists
        print 'Min rating', min(map(min,zip(*amat))), '  - Please note here we have 0 as minimum!'


    pm_csv_reader = pyml_dataread()

    pm_csv_reader.use_numpy = False
    #pm_csv_reader.use_numpy = True
    
    if (pm_csv_reader.use_numpy):
        print "Using Numpy/Scipy"
    else:
        print "NOT Using Numpy/Scipy"
        
    pm_csv_reader.set_filename("./u.csv")
    cmat = pm_csv_reader.read_csv_umrd()

    if (pm_csv_reader.use_numpy):
        print 'Number of users', cmat.shape[0]
        print 'Number of movies', cmat.shape[1]
        print 'Number of ratings', cmat.nnz
        print 'Max rating', cmat.tocoo().data.max()
        print 'Min rating', cmat.tocoo().data.min()
    else:
        print 'Number of users', len(cmat)
        print 'Number of movies', len(cmat[0])
        print 'Number of ratings', sum(sum(1 for i in row if i) for row in cmat)
        # Equivament: print 'Number of ratings', sum(1  for row in cmat for i in row if i)
        print 'Max rating', max(map(max,zip(*cmat)))
        # To check:  [(min(a), max(a)) for a in zip(*calib)] / http://stackoverflow.com/questions/21639010/python-2-7-find-min-max-on-list-of-lists
        print 'Min rating', min(map(min,zip(*cmat))), '  - Please note here we have 0 as minimum!'




    pm_amat = pyml_matstats(amat)
    pm_cmat = pyml_matstats(cmat)
    pm_amat.print_basicstats()
    pm_cmat.print_basicstats()
    
#==============================================================================

if __name__ == '__main__':

    #Load Some utility functions

    #Start the test
    overview_run()

