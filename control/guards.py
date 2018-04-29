from mysql.connector import connect
from memcache import Client

"""
Used to wrap native MySQL connection objects and safely wrap them
for usage inside `with` statements.
"""
class conn_guard:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    
    def __enter__(self):
        self.conn = connect(*self.args, **self.kwargs)
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.close()
        self.conn = None
        return False # Returning False means we don't catch any errors here.

"""
Used to wrap native MySQL cursor objects and safely wrap them
for usage inside `with` statements.
"""
class cur_guard:

    def __init__(self, conn, *args, **kwargs):
        self.conn = conn
        self.args = args
        self.kwargs = kwargs
        self.cur = None

    def __enter__(self):
        self.cur = self.conn.cursor(*self.args, **self.kwargs)
        return self.cur

    def __exit__(self, type, value, traceback):
        self.cur.close()
        return False # Returning False means we don't catch any errors here.

"""
Used to wrap native Memcached connection objects and safely wrap them
for usage inside `with` statements.
"""
class cache_guard:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __enter__(self):
        self.conn = Client(*self.args, **self.kwargs)
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.disconnect_all()
        return False # Returning False means we don't catch any errors here.
