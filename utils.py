import mysql.connector
from mysql.connector import Error
import csv

# Function to save books to a MySQL database
def save_books_to_db(books):
    try:
        # Establishing the MySQL connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # default XAMPP user
            password='',  # default XAMPP password
            database='books_db'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to insert books into the table
            query = """INSERT INTO books (title, price, stock, rating, link)
                       VALUES (%s, %s, %s, %s, %s)"""
            
            # Batch insert
            cursor.executemany(query, [(book['title'], book['price'], book['stock'], book['rating'], book['link']) for book in books])
            connection.commit()
            print(f"{cursor.rowcount} books inserted into the database.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to save books to CSV
def save_books_to_csv(books):
    keys = books[0].keys()  # Get column headers from first dictionary
    with open('books_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(books)
    print("Data saved to 'books_data.csv'.")

# Function to establish a driver for selenium scraping
def init_driver():
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options

    options = Options()
    options.add_argument("--headless")  # Optional: run in headless mode
    driver = webdriver.Firefox(options=options)  # Use Firefox driver from PATH
    return driver
