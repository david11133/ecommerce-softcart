import mysql.connector
import snowflake.connector

# Snowflake connection details
snowflake_config = {
    'user': 'DAVID2342',
    'password': 'rQYDUxYdP8WFsWV',
    'account': 'um76382.eu-central-2.aws',
    'warehouse': 'TRANSFORMING',
    'database': 'SoftCart',
    'schema': 'PUBLIC'
}

# MySQL connection details
mysql_config = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'database': 'sales'
}

def get_snowflake_connection():
    return snowflake.connector.connect(
        user=snowflake_config['user'],
        password=snowflake_config['password'],
        account=snowflake_config['account'],
        warehouse=snowflake_config['warehouse'],
        database=snowflake_config['database'],
        schema=snowflake_config['schema']
    )

def get_mysql_connection():
    return mysql.connector.connect(
        user=mysql_config['user'],
        password=mysql_config['password'],
        host=mysql_config['host'],
        database=mysql_config['database']
    )

def get_last_rowid():
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(rowid) FROM sales_data;")
    last_rowid = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return last_rowid if last_rowid is not None else 0

def get_latest_records(last_rowid):
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, product_id, price FROM sales_data WHERE rowid > %s", (last_rowid,))
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

def insert_records(records):
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    insert_data_sql = "INSERT INTO sales_data (rowid, product_id, price) VALUES (%s, %s, %s)"
    cursor.executemany(insert_data_sql, records)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    last_rowid = get_last_rowid()
    latest_records = get_latest_records(last_rowid)
    if latest_records:
        insert_records(latest_records)
        print(f"Inserted {len(latest_records)} new records into Snowflake.")
    else:
        print("No new records to insert.")
