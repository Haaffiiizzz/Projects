import json
import psycopg2
file = open("countries.json", "r")
data = json.load(file)





# Convert the dictionary to JSON strings for storage
# data = {country: json.dumps(prices[1]) for country, prices in data.items()}

all_items = set()
for prices_list in data.values():
    prices = prices_list[1]
    all_items.update(prices.keys())

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="ItemsAPI",
    user="postgres",
    password="Jss3ajdssk06.",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Create the table dynamically with the unique item names
create_table_query = "CREATE TABLE IF NOT EXISTS countries_items (name VARCHAR(255) PRIMARY KEY, "
create_table_query += ", ".join([f'"{item}" NUMERIC' for item in all_items])
create_table_query += ");"


cur.execute(create_table_query)

# Insert data into the table dynamically
for country, prices_list in data.items():
    prices = prices_list[1]
    columns = ', '.join(['"' + item + '"' for item in prices.keys()])
    values = ', '.join(['%s'] * len(prices))
    insert_query = f"INSERT INTO countries_items (name, {columns}) VALUES (%s, {values}) ON CONFLICT (name) DO NOTHING"
    cur.execute(insert_query, [country] + list(prices.values()))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Data inserted successfully.")