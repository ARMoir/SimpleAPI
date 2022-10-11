import os
import sqlite3

def get(conn, sql):

    try:
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchall()
        cur.close()
    except Exception as error:
        print(str(error))
        output = None

    return output

def set(conn, sql):

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        commit = True
    except Exception as error:
        print(str(error))
        conn.rollback()
        commit = False

    return commit

def create(config):
    
    create = 'CREATE TABLE IF NOT EXISTS "{0}" (time text, key text, value text, PRIMARY KEY (time))'.format('values')  
    status = set(config.database, create)

    return status

def sanitize(items):

    for item in items:
            if "'" in item:
                items[items.index(item)] = item.replace("'", "''")

    return items
        
