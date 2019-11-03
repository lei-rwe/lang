print('conf.__init__.py')

mydata = None
mydb = None

def init():
    print('conf.init()')
    global mydata
    global mydb

    mydata = 'My Data'
    mydb = 'My DB'