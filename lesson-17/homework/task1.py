import pandas as pd
import sqlite3

connection = sqlite3.connect('chinook.db') 

df1 = pd.read_sql_query(
    "SELECT * FROM customers", connection
)

df2 = pd.read_sql_query(
    "SELECT * FROM invoices", connection
)

merged_df = pd.merge(df1, df2, on = 'CustomerId', how = 'inner')

invoice_counts = merged_df.groupby('CustomerId')['InvoiceId'].count().reset_index() 
invoice_counts.columns = ['CustomerId', 'TotalInvoices'] 

print(invoice_counts)
print('\n', '* ' * 50, '\n') 

connection.close() 


df_movie = pd.read_csv('movie.csv') 

df_name_color = df_movie[['color', 'director_name']]
df_name_review = df_movie[['director_name', 'num_critic_for_reviews']] 

merged_left = pd.merge(df_name_color, df_name_review, on = 'director_name', how = 'left') 
print("Merged left:\n", merged_left)
print(f"Number of rows: {merged_left.shape[0]}, \n") 

merged_outer = pd.merge(df_name_color, df_name_review, on = 'director_name', how = 'outer')
print("Merged outer:\n", merged_outer)  
print(f"Number of rows: {merged_outer.shape[0]}, \n") 
print('* ' *50, '\n') 