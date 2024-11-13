from selenium_scraper import scrape_books
from utils import save_books_to_csv, save_books_to_db, init_driver

def main():
    # Initialize the web driver
    driver = init_driver()

    # URL of the website to scrape
    url = 'http://books.toscrape.com/catalogue/page-1.html'

    # Scrape data (scrape all pages)
    books = scrape_books(driver, url, pages=10)  # Scrape the first 10 pages

    # Save scraped books data into CSV
    save_books_to_csv(books)

    # Save books data into MySQL database
    save_books_to_db(books)

    # Close the Selenium driver after scraping
    driver.quit()

if __name__ == "__main__":
    main()
