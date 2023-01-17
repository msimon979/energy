drop_product_sql = "DROP TABLE IF EXISTS product"

create_product_sql = """
    CREATE TABLE product (
        id INT NOT NULL AUTO_INCREMENT primary key,
        product_symbol varchar(225),
        product_description varchar(225)
    );
"""

insert_product_sql = f"""
INSERT INTO product(product_symbol,product_description)
SELECT
    product_symbol,
    product_description
FROM nymex
WHERE CONCAT(product_symbol,product_description) not in (select CONCAT(product_symbol,product_description) from product)
"""
