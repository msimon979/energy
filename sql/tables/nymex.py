drop_nymex_sql = "DROP TABLE IF EXISTS nymex"

create_nymex_sql = """
    CREATE TABLE nymex (
        product_symbol varchar(225),
        contract_month int,
        contract_year int,
        contract_day int,
        contract varchar(225) primary key,
        product_description varchar(225),
        open DECIMAL(4,3),
        high DECIMAL(4,3),
        high_ab_indicator varchar(225),
        low DECIMAL(4,3),
        low_ab_indicator varchar(225),
        last DECIMAL(4,3),
        last_ab_indicator varchar(225),
        settle varchar(225),
        pt_chg varchar(225),
        est_vol int,
        prior_settle varchar(225),
        prior_vol int,
        priot_int int,
        tradedate date
    );
"""

insert_nymex_sql = f"""
INSERT INTO nymex
SELECT
    product_symbol,
    contract_month,
    contract_year,
    case when contract_day = '' then 0 else contract_day end as contract_day,
    contract,
    product_description,
    case when open = '' then 0.0 else CAST(open AS DECIMAL(4,3)) end as open,
    case when high = '' then 0.0 else CAST(high AS DECIMAL(4,3)) end as high,
    high_ab_indicator,
    case when low = '' then 0.0 else CAST(low AS DECIMAL(4,3)) end as low,
    low_ab_indicator,
    case when last = '' then 0.0 else CAST(last AS DECIMAL(4,3)) end as last,
    last_ab_indicator,
    settle,
    pt_chg,
    case when est_vol = '' then 0 else est_vol end as est_vol,
    prior_settle,
    case when prior_vol = '' then 0 else prior_vol end as prior_vol,
    case when priot_int = '' then 0 else priot_int end as priot_int,
    STR_TO_DATE(tradedate,'%m/%d/%Y') as date
FROM nymex_raw
LIMIT 1000
"""