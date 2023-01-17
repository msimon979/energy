import mysql.connector


def get_cursor():
    mydb = mysql.connector.connect(host="localhost", user="root", password="password")

    cur = mydb.cursor()
    cur.execute("USE DB")

    return mydb, cur


def close_cursor(mydb, cur):
    cur.close()
    mydb.close()


def format_nymex_data(record):
    formatted_record = ""
    for k, v in record.items():
        formatted_record += f"'{v}'"
        if k != "TRADEDATE":
            formatted_record += ","

    return formatted_record
