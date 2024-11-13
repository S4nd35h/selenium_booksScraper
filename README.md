
# Web Scraping Books with Selenium

This project is a Python-based web scraping solution that extracts book data from "Books to Scrape" using Selenium and BeautifulSoup. It stores the scraped data in a MySQL database and a CSV file. Additionally, a PHP-based frontend is used to display the data with basic search functionality and sorting options by price and rating.

## Features

- Scrapes book title, price, stock status, rating, and link from the website.
- Supports pagination to scrape multiple pages.
- Saves the data in both a MySQL database and a CSV file for further analysis.
- Frontend in PHP that displays the scraped data with sorting and search capabilities.
- Option to filter books by price and rating.

## Project Structure

```
/books-scraping
│
├── books_data.csv          # CSV file containing the scraped book data
│
│   ├── index.php               # PHP file for displaying books with search and sorting
│  
│   ├── main.py                 # Main script to execute the scraping process
│   ├── selenium_scraper.py     # Selenium scraper file for scraping data
│   └── utils.py                # Utility functions for saving data to CSV and DB
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Requirements

### Python Dependencies

- selenium
- beautifulsoup4
- requests
- mysql-connector-python (used for MySQL database connection)

You can install the required Python dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### XAMPP for MySQL Database

This project uses XAMPP to run a MySQL server locally. Make sure to have XAMPP installed and MySQL running on your local machine.

### Web Browser Driver

Ensure you have Firefox installed, and the geckodriver executable is in your system PATH. You can download the latest version of geckodriver from here.

## Setup and Configuration

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up XAMPP and MySQL

- Start XAMPP and launch MySQL.
- Create a new database `books_db`:

```sql
CREATE DATABASE books_db;
```

- Create a table `books`:

```sql
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    price VARCHAR(50),
    stock VARCHAR(50),
    rating VARCHAR(50),
    link VARCHAR(255),
    
);
```

### 3. Running the Scraper

- Make sure geckodriver is in your system PATH.
- Run the `main.py` script to start the scraping process:

```bash
python main.py
```

This will:

- Scrape data from the website (http://books.toscrape.com).
- Save the scraped data to a CSV file (`data/books_data.csv`).
- Insert the data into the MySQL database (`bookstore.books`).

### 4. Frontend (PHP)

To view the scraped data:

- Make a folder in the `htdocs` directory of your XAMPP installation and move index.php inside that folder
- Start the Apache server and MySQL using XAMPP.
- Visit `http://localhost/YOURFOLDERNAME/index.php` in your web browser.
- Use the search bar to filter books by title, price, and rating.
- You can sort the books by price or rating.

### 5. Search and Sorting Features in Frontend

- **Search**: Allows searching for books by title.
- **Sort by Price**: Sorts books by price in ascending or descending order.
- **Sort by Rating**: Sorts books by rating in ascending or descending order.

## Python Scripts Breakdown

### selenium_scraper.py

Handles the web scraping using Selenium. It loads pages, scrapes book data (title, price, stock, rating, and link), and handles pagination.

### utils.py

Contains utility functions for saving data:

- `save_books_to_csv()` - Saves the scraped data into a CSV file.
- `save_books_to_db()` - Saves the scraped data into the MySQL database.

### main.py

This script is the entry point for the scraping process. It initializes the web driver, scrapes the data, saves it to CSV and MySQL, and then closes the web driver.

## Frontend (PHP)

- `index.php` - This PHP file connects to the MySQL database, retrieves the book data, and displays it in a table format. It includes features like search and sorting by price and rating.

**Note**: There is no `config.php` file in this project. Database connection settings have been directly placed in the `index.php` file.

## Troubleshooting

- Ensure that XAMPP's MySQL service is running before scraping.
- If the scraping doesn't work, check that geckodriver is installed correctly and is accessible in your PATH.
- Verify the database connection settings in `index.php` for MySQL.
- If you encounter issues with sorting in the frontend, ensure the proper SQL queries are being executed.

## Further Enhancements

- Add more book details (e.g., author, description) by inspecting the website more closely.
- Implement a more advanced search with multiple filters (e.g., filter by category, author).
- Add pagination to the frontend to navigate through more records.
- Schedule periodic scraping using a task scheduler (e.g., cron jobs).
