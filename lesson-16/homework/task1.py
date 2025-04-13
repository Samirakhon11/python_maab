import sqlite3
import pandas
import openpyxl
import csv

with sqlite3.connect('chinook.db') as connection:
    df_customers = pandas.read_sql(
        "SELECT * FROM customers", 
        con = connection
    ) 

print(df_customers.head(10)) 
print('* ' * 30)

df_iris = pandas.read_json('iris.json') 
print("The shape of the file: ", df_iris.shape)
print("Names of the columns: ", df_iris.columns.tolist())  
print('* ' * 30)

df_titanic = pandas.read_excel('titanic.xlsx')
print(df_titanic.head(5)) 
print('* ' * 30)

flights = pandas.read_parquet('flights')  
flights.info() 
print('* ' * 30)

df_movie = pandas.read_csv('movie.csv') 
sample = df_movie.sample(n = 10, random_state = 1)
print(sample)