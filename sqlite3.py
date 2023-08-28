import sqlite3

def calculate_total_revenue():
    # Connect to the database
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # Execute SQL query to calculate total revenue
    cursor.execute('SELECT SUM(quantity * price) FROM orders')
    total_revenue = cursor.fetchone()[0]

    # Close the database connection
    connection.close()
    return total_revenue

print(calculate_total_revenue())
