from sqlite3 import connect

def gentable(cur):
    print('ctxtable.__enter__')
    cur.execute('create table points(x int, y int)')
    yield
    print('ctxtable.__exit__')
    cur.execute('drop table points')

class genctx:
    def __init__(self, gen):
        self.gen = gen
    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)
    def __exit__(self, exc_type, exc_val, exc_tb):
        next(self.gen_inst, None)

class ctxtable:
    def __init__(self, cur):
        self.cur = cur
    def __enter__(self):
        print('ctxtable.__enter__')
        cur.execute('create table points(x int, y int)')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('ctxtable.__exit__')
        cur.execute('drop table points')

with connect('test.db') as conn:
    cur = conn.cursor()
    with ctxtable(cur):
        cur.execute('insert into points (x, y) values (1, 1)')
        cur.execute('insert into points (x, y) values (1, 2)')
        cur.execute('insert into points (x, y) values (1, 5)')
        cur.execute('insert into points (x, y) values (3, 1)')
        for row in cur.execute('select * from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)
