from helpers import get_cursor, close_cursor
from sql.tables.nymex import drop_nymex_sql, create_nymex_sql, insert_nymex_sql

def load_nymex_data():
    mydb, cur = get_cursor()

    cur.execute(drop_nymex_sql)
    cur.execute(create_nymex_sql)
    mydb.commit()

    print("Inserting data into nymex")
    try:
        cur.execute(insert_nymex_sql)
    except:
        print('ERROR')
        return False
    mydb.commit()

    close_cursor(mydb, cur)
