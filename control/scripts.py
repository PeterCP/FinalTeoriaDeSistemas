#!/usr/bin/env python3

import sys
from random import randint
from . import config
from .guards import conn_guard, cur_guard

# Get the record count from the database.
def get_record_count(conn):
    count = None
    with cur_guard(conn) as cur:
        cur.execute('select count(*) from people;')
        row = cur.fetchone()
        count = row[0]
    assert count is not None, "Could not get record count from database."
    return count

# Get the setpoint from the user.
def ask_for_setpoint():
    setpoint = float(input("Please insert the setpoint (0 <= setpoint <= 1): "))
    while setpoint < 0 or setpoint > 1:
        setpoint = float(input(
            "Invalid setpoint value, try again (0 <= setpoint <= 1): "))
    return setpoint

# Function to test convergence. Returns a percentage (0 <= result <= 1).
def test_convergence(cache, record_count):
    hits = 0
    for i in range(0, config.TESTS):
        key = str(randint(1, record_count))
        if cache.get(key) is not None:
            hits += 1
    # Return convergence, cache_hits, db_hits
    return hits / config.TESTS, hits, config.TESTS - hits

def add_to_cache(db, cache, record_count):
    added = 0
    while added < config.BATCH_SIZE:
        key = str(randint(1, record_count))
        if cache.get(key) is None:
            with cur_guard(db, prepared=True) as cur:
                cur.execute("select * from people where id = %s", (key,))
                row = cur.fetchone()
                cache.set(key, "{1} {2} {3}".format(*row))
                added += 1

