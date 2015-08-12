#! /usr/local/bin/python

class myClass:
    theint = 0

    def __init__(self, *pars):
        if len(pars) == 1 and isinstance(pars[0], int):
            self.theint = pars[0]
            
    def set_theint(self,ival):
        self.theint = ival

    def print_theint(self):
        print "Within the class", self.theint

    def set_theint(self,vint):
        self.theint = vint

    def get_theint(self):
        return self.theint

print "define instances... a,b plain; c,d with init"
a = myClass()
b = myClass()
c = myClass(3)
d = myClass(4)

print "print property directly a,b,c,d,Class"
print a.theint, 0
print b.theint, 0
print c.theint, 3
print d.theint, 4
print myClass.theint, 0

print "print property with get_theint a,b,c,d"
print a.get_theint(), 0
print b.get_theint(), 0
print c.get_theint(), 3
print d.get_theint(), 4
# ERROR: print myClass.get_theint()

print "print property with CLASS get_theint giving instances a,b,c,d"
print myClass.get_theint(a), 0
print myClass.get_theint(b), 0
print myClass.get_theint(c), 3
print myClass.get_theint(d), 4

print "print property using print_theint(): res as above"
a.print_theint()
b.print_theint()
c.print_theint()
d.print_theint()

print "print property with CLASS print_theint giving instances a,b,c,d: res as above"
myClass.print_theint(a)
myClass.print_theint(b)
myClass.print_theint(c)
myClass.print_theint(d)


print "Set class 'static' theint to 10 .. see local name space for c and d."
myClass.theint = 10

print "print property directly a,b,c,d,Class"
print a.theint, 0, "Warning! Calling 'myClass.theint = 10' changed the a instance value!"
print b.theint, 0, "Warning! Calling 'myClass.theint = 10' changed the b instance value!"
print c.theint, 3
print d.theint, 4
print myClass.theint, 10
print "=========================================="
print "Note the Warning above. If you do not set the value in your instance, python namespace searches 'above'."
print "Technically it means that if you do not set all the values on instance generation, a direct call to the class might"
print "change the value 'on the fly'"
print "I think my old solution was to 're'-assign all values in __init__, but not sure now..."
print "Note also that the CLASS value now is 10 and not the default 0"
print "=========================================="
print "proove (e instance generate):"
e = myClass()
print "e theint", e.theint, 10
print " CLASS theint to 666"
myClass.theint = 666
print "e theint", e.theint, 10, "Warning! Calling 'myClass.theint = 666' changed the e instance value!"
print "Restoring CLASS to 10"
myClass.theint = 10

print "=========================================="
print "print property with get_theint a,b,c,d: res: WAIT see above: 10, 10, 3, 4"
a.print_theint()
b.print_theint()
c.print_theint()
d.print_theint()
myClass.print_theint(a)
myClass.print_theint(b)
myClass.print_theint(c)
myClass.print_theint(d)

print "setting local for a and b."
a.theint = 1
b.theint = 2

print a.theint, 1
print b.theint, 2
print c.theint, 3
print d.theint, 4
print myClass.theint, 10

print "Using print_theint() res: 1, 2, 3, 4"
a.print_theint()
b.print_theint()
c.print_theint()
d.print_theint()
myClass.print_theint(a)
myClass.print_theint(b)
myClass.print_theint(c)
myClass.print_theint(d)

#Adding random namespace...
print "Addind random namespace..."
a.otherint = 666
print "...Done"
# ERROR: myClass.set_theint(331)
print "=========================================="
print "Call: instance Set_TheInt" 
print "=========================================="
a.set_theint(21)
b.set_theint(22)
c.set_theint(23)
d.set_theint(24)

print a.theint, 21
print b.theint, 22
print c.theint, 23
print d.theint, 24
print myClass.theint, 10
a.print_theint()
b.print_theint()
c.print_theint()
d.print_theint()
myClass.print_theint(a)
myClass.print_theint(b)
myClass.print_theint(c)
myClass.print_theint(d)

print "=========================================="
print "test new instance"
print "=========================================="
e = myClass()
print "class value", myClass.theint
print "e instance value", e.theint
print "call e.set_theint() to 333"
e.set_theint(333)
print "class value", myClass.theint
print "e instance value", e.theint

print "Set class 'static' theint to 10 .. see local name space for c and d."
myClass.theint = 10

print a.theint
print b.theint
print c.theint
print d.theint
print myClass.theint
a.print_theint()
b.print_theint()
c.print_theint()
d.print_theint()
myClass.print_theint(a)
myClass.print_theint(b)
myClass.print_theint(c)
myClass.print_theint(d)

print "setting local for a and b."
a.theint = 1
b.theint = 2

print a.theint
print b.theint
print c.theint
print d.theint
print myClass.theint
a.print_theint()
b.print_theint()
c.print_theint()
d.print_theint()
myClass.print_theint(a)
myClass.print_theint(b)
myClass.print_theint(c)
myClass.print_theint(d)


print "=========================================="
