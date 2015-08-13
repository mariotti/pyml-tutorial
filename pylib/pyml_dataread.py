'''
@author: F.Mariotti
'''
import imp

class pyml_dataread:
    
    irc = 1
    pymldebug = False
    filename = None
    filenlines = None
    use_numpy = True

#-------------------------------------------------------------------------------
    def __init__(self, *pars):
        '''
        Set the default return code (irc) to 1=[no errors]
        '''
        self.irc = 1
        self.pymldebug = False
        self.filename = None
        self.filenlines = None
        self.has_m_csv = True

        self.use_numpy = True
        self.has_m_numpy = True
        self.has_m_scipy = True

        
        try:
            self.has_m_csv = True
            imp.find_module('csv')
        except ImportError:
            self.has_m_csv = False
            self.irc = -1

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

        if len(pars) == 1 and isinstance(pars[0], str):
            self.filename=pars[0]

#-------------------------------------------------------------------------------
    def set_filename(self, infilename):

        self.filename=infilename
    
#-------------------------------------------------------------------------------
    def get_filename(self):

        return self.filename
    
#-------------------------------------------------------------------------------
    def get_file_lines(self, *pars):

        if len(pars) == 1 and isinstance(pars[0], str):
            filenm = pars[0]
        else:
            filenm = self.filename

        with open(filenm) as f:
            for i, l in enumerate(f):
                pass

        f.close()
        
        self.filenlines = i+1
        return self.filenlines

#-------------------------------------------------------------------------------
    def dict2mat(self,matdict,utr,otr):
        
        #amat = [[0 for x in range(nu)] for x in range(no)] 

        nu = len(utr)
        no = len(otr)
        
        vmax = -1

        if (self.pymldebug):
            if (self.use_numpy):
                print "dict2mat using numpy"
            
        if (self.use_numpy):
            import numpy as np
            from scipy import sparse

            amat = sparse.lil_matrix((nu,no))
            
            for ik in utr.keys():
                i = utr[ik]
                for jk in otr.keys():
                    j = otr[jk]

                    val = 0
                    if matdict[ik].has_key(jk):
                        val = int(matdict[ik][jk])
                
                    amat[i,j] = val
                    
                    if (val > vmax):
                        vmax = val

                    if (self.pymldebug):
                        print '{0:5} {1:5} {2:5} {3:5}'.format(i,j,ik,jk)
                        print '{0:5} {1:5} {2:5} {3:5} {4:5}'.format(' ',' ',' ',' ',val)

        else:
            amat = [[0 for x in range(no)] for x in range(nu)] 

            for ik in utr.keys():
                i = utr[ik]
                for jk in otr.keys():
                    j = otr[jk]

                    val = 0
                    if matdict[ik].has_key(jk):
                        val = int(matdict[ik][jk])
                
                    amat[i][j] = val
                    
                    if (val > vmax):
                        vmax = val

                    if (self.pymldebug):
                        print '{0:5} {1:5} {2:5} {3:5}'.format(i,j,ik,jk)
                        print '{0:5} {1:5} {2:5} {3:5} {4:5}'.format(' ',' ',' ',' ',val)
                        
        if (self.pymldebug):
            print "Max in sub", vmax
        
        return amat
            
#-------------------------------------------------------------------------------
    def read_ascii_umrd(self):

        self.filenlines = self.get_file_lines()
        
        uidxdict = dict()
        midxdict = dict()
        matdict = dict(dict())
        movdict = dict()

        uidx = 0
        midx = 0

        if self.filename == None:
            self.irc = -4
            return None

        if self.filenlines == None:
            self.irc = -5
            return None

        f = open(self.filename)
                                # Alternative reading: # all_lines = f.readlines()

        for l in f:
            
            if (self.pymldebug):
                print "Line", l

            fields = l.split()
            
            if (self.pymldebug):
                print "Fileds: 1: ", fields[0], " - 2: ", fields[1], " - 3: ", fields[2], " - 4: ", fields[3]

            if matdict.has_key(fields[0]):

                if matdict[fields[0]].has_key(fields[1]):
                    print "ERROR _ duplicated vote"
                    exit()

            else:
                matdict[fields[0]] = dict()
                uidxdict[fields[0]] = uidx
                uidx += 1

            matdict[fields[0]][fields[1]] = fields[2]

            if not movdict.has_key(fields[1]):
                movdict[fields[1]] = dict()
                midxdict[fields[1]] = midx
                midx += 1

            if (self.pymldebug):
                print '{0:5} {1:5} {2:5} {3:5} {4:5} {5:5}'.format(fields[0],fields[1],fields[2],uidxdict[fields[0]],midxdict[fields[1]],matdict[fields[0]][fields[1]])
                

        amat = self.dict2mat(matdict,uidxdict,midxdict)

        return amat



#-------------------------------------------------------------------------------
    def read_csv_umrd(self):

        if (self.has_m_csv):
            import csv
        else:
            self.irc = -8
            return None
        
        self.filenlines = self.get_file_lines()
        
        uidxdict = dict()
        midxdict = dict()
        matdict = dict(dict())
        movdict = dict()

        uidx = 0
        midx = 0

        if self.filename == None:
            self.irc = -6
            return None

        if self.filenlines == None:
            self.irc = -7
            return None

        csvfile = open(self.filename, "rb")
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)

        #initiate reader
        csvreader = csv.reader(csvfile, dialect)
        
        for row in csvreader:
            
            if (self.pymldebug):
                print "Line", row

            if matdict.has_key(row[0]):

                if matdict[row[0]].has_key(row[1]):
                    print "ERROR _ duplicated vote"
                    exit()

            else:
                matdict[row[0]] = dict()
                uidxdict[row[0]] = uidx
                uidx += 1

            matdict[row[0]][row[1]] = row[2]

            if not movdict.has_key(row[1]):
                movdict[row[1]] = dict()
                midxdict[row[1]] = midx
                midx += 1

            if (self.pymldebug):
                print '{0:5} {1:5} {2:5} {3:5} {4:5} {5:5}'.format(row[0],row[1],row[2],uidxdict[row[0]],midxdict[row[1]],matdict[row[0]][row[1]])
                

        amat = self.dict2mat(matdict,uidxdict,midxdict)

        return amat
    
