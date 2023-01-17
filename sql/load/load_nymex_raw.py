import csv
from helpers import get_cursor, close_cursor, format_nymex_data
from sql.tables.nymex_raw import drop_nymex_raw_sql, create_nymex_raw_sql, nymex_values

def load_nymex_raw_data(file):
    if file is None:
        return

    mydb, cur = get_cursor()

    cur.execute(drop_nymex_raw_sql)
    cur.execute(create_nymex_raw_sql)
    mydb.commit()

    data_file = file

    print("Loading file into memory")
    with open(data_file, "r") as f:
        csv_reader = csv.DictReader(f)
        records = list(csv_reader)

    print("Inserting rows into the nymex_raw")
    error_rows = []
    for idx, record in enumerate(records):
        formatted_record = format_nymex_data(record)
        sql_stmt = f"""
        INSERT INTO nymex_raw({nymex_values}) 
        VALUES({formatted_record})"""

        try:
            cur.execute(sql_stmt)
        except:
            error_rows = idx + 1
            continue

        mydb.commit()

        if idx % 500 == 0:
            print(f"Loaded {idx} rows")

    
    sql_stmt = "select count(*) from nymex_raw"
    cur.execute(sql_stmt)
    response = cur.fetchall()
    close_cursor(mydb, cur)

    return response[0][0]
