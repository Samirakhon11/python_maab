import sqlite3

create = """
    Create table Books(Title TEXT, Author TEXT, Year_Published INT, Genre TEXT)
"""

insert = """
    INSERT into Books Values('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald',	1925, 'Classic') 
"""

with sqlite3.connect("library.db") as connection:
    cursor = connection.cursor()
    cursor.execute(create)
    cursor.execute(insert)

    cursor.execute("""
        UPDATE Books SET Year_Published = 1950 WHERE Year_Published = 1949
    """)

    cursor.execute("""
        SELECT Title, Author FROM Books WHERE Genre = 'Dystopian' 
    """)

    cursor.execute("""
        DELETE FROM Books WHERE Year_Published < 1950
    """)

    cursor.execute("""
        ALTER TABLE Books ADD COLUMN Rating TEXT
    """)

    cursor.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
    cursor.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
    cursor.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")

    cursor.execute("""
        SELECT * FROM Books ORDER BY Year_Published ASC
    """)

    results = cursor.fetchall()
    for row in results:
        print(row) 