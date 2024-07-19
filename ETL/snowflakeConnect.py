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

# Establish the Snowflake connection
conn = snowflake.connector.connect(
    user=snowflake_config['user'],
    password=snowflake_config['password'],
    account=snowflake_config['account'],
    warehouse=snowflake_config['warehouse'],
    database=snowflake_config['database'],
    schema=snowflake_config['schema']
)

print("Connected to Snowflake database: ", snowflake_config['database'])

# Create table
create_table_sql = """
CREATE TABLE IF NOT EXISTS products (
    rowid INTEGER PRIMARY KEY,
    product VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);
"""

conn.cursor().execute(create_table_sql)
print("Table created")

# Insert data
insert_data_sql = """
INSERT INTO products (rowid, product, category) VALUES (%s, %s, %s)
"""

data = [
    (1, 'Television', 'Electronics'),
    (2, 'Laptop', 'Electronics'),
    (3, 'Mobile', 'Electronics')
]

cursor = conn.cursor()
cursor.executemany(insert_data_sql, data)
conn.commit()
print("Data inserted")

# Query data
query_data_sql = "SELECT * FROM products"
cursor.execute(query_data_sql)

rows = cursor.fetchall()
for row in rows:
    print(row)

# Export data to CSV
# import csv

# export_query = "SELECT * FROM products"
# cursor.execute(export_query)
# rows = cursor.fetchall()
# field_names = [i[0] for i in cursor.description]

# with open('products_data.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(field_names)
#     writer.writerows(rows)

# print("Data exported to products_data.csv")

# Close connection
conn.close()
