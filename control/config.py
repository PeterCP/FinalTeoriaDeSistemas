#!/usr/bin/env python3

# MySQL connection configuration
MYSQL_CONFIG = {
    'user': 'finalguirao',
    'password': 'finalguirao',
    'host': '127.0.0.1',
    'database': 'finalguirao'
}

# Memcached connection configuration
MEMCACHED_HOST = '127.0.0.1'

# Row indices to be used with row tuples
ID = 0
NAME = 1
FIRST_SURNAME = 2
LAST_SURNAME = 3
BIRTH_DATE = 4

# Number of memcached keys to try.
TESTS = 100

# Number of records to add to cache upon failed convergence.
BATCH_SIZE = 500
