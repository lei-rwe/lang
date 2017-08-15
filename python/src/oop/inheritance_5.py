'''
super: worse or better?
'''
class B(object):
    def __init__(self): print('B.__init__'); super(B, self).__init__()
class C(object):
    def __init__(self): print('C.__init__'); super(C, self).__init__()
class D(B, C): pass

x = D()
