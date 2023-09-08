import sqlite3
import pandas as pd
sql_name = 'auto_gnn_j30_cpfeatures_True_reverseedges_False_data_list_long_exp.db'
connection = sqlite3.connect(sql_name)
cursor = connection.cursor()
 # Execute a query to retrieve the table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# Fetch all the table names
table_names = cursor.fetchall()
# Extract table names from the list of tuples and store them in a separate list
table_names_list = [table[0] for table in table_names]
# Print the table names to see what tables are available in the database
print(table_names_list)

query = "SELECT * FROM trial_intermediate_values"
df = pd.read_sql_query(query,connection)
sorted_df = df.sort_values(by="intermediate_value")
column_list = sorted_df.columns.tolist()
print(column_list)
selected_data = sorted_df.head(200)[["trial_id", "intermediate_value"]].drop_duplicates(subset=["trial_id"])
print(selected_data)
