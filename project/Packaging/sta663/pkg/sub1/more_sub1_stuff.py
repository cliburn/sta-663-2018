from pkg.sub1.sub1_stuff import g1, g2

def g3():
    return 'g3 uses %s, %s' % (g1(), g2())

