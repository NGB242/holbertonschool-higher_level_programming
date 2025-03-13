#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Retrieve MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the query to fetch all states, sorted by states.id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows of the query result
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
