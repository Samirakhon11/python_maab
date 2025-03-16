import sqlite3

create = """
    Create table Roster(name TEXT, species TEXT, age INT)
"""

insert = """
    Insert into Roster Values('Benjamin Sisko', 'human', 40),
    ('Jadzia Dax', 'Trill', 300), 
    ('Kira Nerys', 'Bajoran', 29)
"""

with sqlite3.connect("roster.db") as connection:
    cursor = connection.cursor()
    cursor.execute(create)
    cursor.execute(insert)

    cursor.execute("""
        UPDATE Roster SET name = 'Ezri Dax' WHERE name = 'Jadzia Dax'
    """)
    connection.commit() 

    cursor.execute("""
        SELECT name, age FROM Roster WHERE species = 'Bajoran' 
    """)

    cursor.execute("""
        DELETE FROM Roster WHERE age > 100
    """)
    connection.commit()

    cursor.execute("""
        ALTER TABLE Roster ADD COLUMN rank TEXT
    """) 

    cursor.execute("UPDATE Roster SET rank = 'Captain' WHERE name = 'Benjamin Sisko'")
    cursor.execute("UPDATE Roster SET rank = 'Lieutenant' WHERE name = 'Ezri Dax'")
    cursor.execute("UPDATE Roster SET rank = 'Major' WHERE name = 'Kira Nerys'")

    cursor.execute("""
        SELECT * FROM Roster ORDER BY age DESC;
    """)

    results = cursor.fetchall()
    for row in results:
        print(row)