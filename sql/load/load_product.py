from helpers import get_cursor, close_cursor
from sql.tables.product import insert_product_sql

def load_product_data():
    mydb, cur = get_cursor()

    print("Inserting data into product")
    try:
        cur.execute(insert_product_sql)
    except:
        print('ERROR')
        return False
    mydb.commit()

    close_cursor(mydb, cur)
