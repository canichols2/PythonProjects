import pypyodbc as odbc

# Manually built context manager
class contextmanager:
    def __init__(self, gen):
        self.gen = gen
    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):
        self.gen_instance = self.gen(*self.args, **self.kwargs)
        next(self.gen_instance)
    def __exit__(self, *args):
        next(self.gen_instance, None)


@contextmanager
def temptable(cursor):
    cursor.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cursor.execute('drop table points')


with odbc.connect('DSN=MySQL Localhost') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1);')
        cur.execute('insert into points (x, y) values(2, 1);')
        cur.execute('insert into points (x, y) values(1, 2);')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x + y) from points'):
            print(row)





# conn.close();

# <iframe width="480" height="269" src="https://www.youtube.com/embed/7lmCu8wz8ro" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>