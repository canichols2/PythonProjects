import pypyodbc as odbc
from contextlib import contextmanager


# This is the perfered method to create a context manager.
# # There is already a module created to be used 
# # you just have to know how to use it.
# # # Much simpler syntax.
@contextmanager
def open_file(file, mode):
    print("opening file")
    try:
        myFile = open(file,mode)
        yield myFile
    finally:
        print("closing file")
        myFile.close()

def select(cur, statement):
    pass

@contextmanager
def transaction(connStr):
    with odbc.connect(connStr, autocommit=False) as con:
        try:
            yield con
        except:
            con.rollback()


def read_row(cur,selectStatement):
    cur.execute(selectStatement)
    row = cur.fetchone()
    while True:
        if not row:
            break 
        print("yielding next row")
        yield row;
        row = cur.fetchone()
    pass


connStr1 = 'DSN=MySQL Localhost'
with transaction(connStr1) as conn:
    cur = conn.cursor()
    if 'records' not in cur.execute('show tables'):
        cur.execute('create table points(x int, y int);')
    for i in range(100):
        cur.execute('insert into points (x, y) values({}, 1);'.format(i%80))
        cur.execute('insert into points (x, y) values(2, {});'.format(i*45))
        cur.execute('insert into points (x, y) values(?, 2);',i)

with transaction(connStr1) as conn:
    cur = conn.cursor()
    selectStatement = 'select * from points'
    for row in read_row(cur,selectStatement):
        print(row)


