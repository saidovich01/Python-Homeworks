import sqlite3

with sqlite3.Connection("Sample_Database.db") as connection:
    cursor = connection.cursor()
    query = "Create Table Roster (Name varchar(20), Species varchar(20), age int)"
    cursor.execute(query)

    query = """
    Insert into Roster values ("Benjamin Sisko", "Human", 40);
    Insert into Roster values ("Jadzia Dax", "Trill", 300);
    Insert into Roster values ("Kira Nerys", "Bajoran", 29)
    """
    cursor.executescript(query)

    query = """Update Roster
    Set Name = "Ezri Dax"
    where name = "Jadzia Dax"
    """
    cursor.execute(query)

    query = "Select * from Roster"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

