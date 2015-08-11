'''
@author: F.Mariotti
'''
import imp

class pyml_dataread:
    
    filename = None

#-------------------------------------------------------------------------------
    def __init__(self, *pars):
        '''
        Set the default return code (irc) to 1=[no errors]
        '''
        self.irc=1
        try:
            imp.find_module('csv')
            self.has_m_csv = True
        except ImportError:
            self.has_m_csv = False

        if len(pars) == 1 and isinstance(pars[0], str):
            self.filename=pars[0]
            
#-------------------------------------------------------------------------------
    def set_filename(self, infilename):

        self.filename=infilename
    
#-------------------------------------------------------------------------------
    def get_filename(self):

        return self.filename
    
#-------------------------------------------------------------------------------
    def read_ascii_umrd(self):

        matdict = dict()
        tmpdict = dict()

        if self.filename == None:
            return None

        f = open(self.filename)
        #all_lines = f.readlines()

        for l in f:
            if (True):
                print "Line", l

            fields = l.split()
            if (True):
                print "Fileds: 1: ", fields[0], " - 2: ", fields[1], " - 3: ", fields[2], " - 4: ", fields[3]

            
            
        

