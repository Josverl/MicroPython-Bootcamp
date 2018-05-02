import upip 
upip.install('micropython-sqlite3')

import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("SELECT 1, 'foo', 3.14159 UNION SELECT 3, 3, 3")

while True:
    row = cur.fetchone()
    if row is None:
        break
    print(row)

import upip
upip.install("micropython-pystone_lowmem",'/flash')    