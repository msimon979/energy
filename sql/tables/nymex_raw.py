drop_nymex_raw_sql = "DROP TABLE IF EXISTS nymex_raw"
create_nymex_raw_sql = """
    CREATE TABLE nymex_raw (
        product_symbol varchar(225),
        contract_month varchar(225),
        contract_year varchar(225),
        contract_day varchar(225),
        contract varchar(225),
        product_description varchar(225),
        open varchar(225),
        high varchar(225),
        high_ab_indicator varchar(225),
        low varchar(225),
        low_ab_indicator varchar(225),
        last varchar(225),
        last_ab_indicator varchar(225),
        settle varchar(225),
        pt_chg varchar(225),
        est_vol varchar(225),
        prior_settle varchar(225),
        prior_vol varchar(225),
        priot_int varchar(225),
        tradedate varchar(225)
    );
"""

nymex_values = "product_symbol,contract_month,contract_year,contract_day,contract,product_description,open,high,high_ab_indicator,low,low_ab_indicator,last,last_ab_indicator,settle,pt_chg,est_vol,prior_settle,prior_vol,priot_int,tradedate"
