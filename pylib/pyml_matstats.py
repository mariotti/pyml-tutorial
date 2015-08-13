'''
@author: F.Mariotti
'''
import imp

class pyml_matstats:
    
    irc = 1
    pymldebug = False
    use_numpy = True

    amat = None

#-------------------------------------------------------------------------------
    def __init__(self, *pars):
        '''
        Set the default return code (irc) to 1=[no errors]
        '''
        self.irc = 1
        self.pymldebug = False

        self.amat = None

        self.use_numpy = True
        self.has_m_numpy = True
        self.has_m_scipy = True

        try:
            self.has_m_numpy = True
            imp.find_module('numpy')
        except ImportError:
            self.has_m_numpy = False
            self.irc = -2

        try:
            self.has_m_scipy = True
            imp.find_module('scipy')
        except ImportError:
            self.has_m_numpy = False
            self.has_m_scipy = False
            self.irc = -3

        if (self.has_m_numpy and self.has_m_scipy):
            self.use_numpy = True
        else:
            self.use_numpy = False
            
        if (self.pymldebug):
            if (self.use_numpy):
                print "Class init setting up numpy"
            else:
                print "Class init cannot load numpy"

        if len(pars) == 1 and isinstance(pars[0], list):
            self.amat = pars[0]
            if (self.use_numpy):
                self.use_numpy = False
                if (self.pymldebug):
                    print "Class input matrix is a list: restoring to NOT usenumpy"

        if (self.use_numpy):
            import numpy as np
            import scipy as sp
            if len(pars) == 1 and sp.sparse.isspmatrix(pars[0]):
                self.amat = pars[0]

    
        if len(pars) == 1 and (self.amat == None):
            print "Something went wrong in the amat assignment"
            raise

#-------------------------------------------------------------------------------
    def print_basicstats(self):
        
        if (self.use_numpy):
            print "Mat Shape: ",self.amat.shape
        else:
            print "Mat Shape:  ", len(self.amat),',',len(self.amat[0])

        if (self.use_numpy):
            mnnz = self.amat.nnz
        else:
            mnnz = sum(sum(1 for i in row if i) for row in self.amat)
            
        print "Mat Non Zeros: ", mnnz

        if (self.use_numpy):
            aar = self.amat.toarray()
            
            for rt in xrange(1,6):
                mrt = ( aar == rt)
                nrt = sum(sum(mrt))
                print "Number of ", rt, "s ratings", nrt, float(nrt)/float(mnnz)

        else:
            for rt in xrange(1,6):
                nrt = sum(sum(1 for i in row if (i==rt)) for row in self.amat)
                print "Number of ", rt, "s ratings", nrt, float(nrt)/float(mnnz)
