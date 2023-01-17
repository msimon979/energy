import json
from sql.load.load_nymex_raw import load_nymex_raw_data
from sql.load.load_nymex import load_nymex_data
from sql.load.load_product import load_product_data
import time

def load_nymex(event, context):
    if file := event.get("file"):
        start = time.perf_counter()
        loaded_raw_rows = load_nymex_raw_data(file=file)
        load_nymex_data()
        load_product_data()

        end = time.perf_counter()
        total_time = f"{end - start:0.4f}"
        body = {
            "nymex_raw_rows": loaded_raw_rows,
            "run_time": total_time
        }

        response = {"statusCode": 200, "body": json.dumps(body)}
        return response

    return {"statusCode": 400, "body": "Could not find file"}
