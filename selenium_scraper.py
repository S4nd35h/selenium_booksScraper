from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# Function to initialize WebDriver
def init_driver():
    options = Options()
    options.add_argument("--headless")  # Optional: run in headless mode
    driver = webdriver.Firefox(options=options)  # Use Firefox driver from PATH
    return driver

# Function to scrape books from a website
def scrape_books(driver, url, pages=5):
    books_data = []
    driver.get(url)

    for page in range(1, pages + 1):
        books = driver.find_elements(By.CLASS_NAME, "product_pod")
        for book in books:
            title = book.find_element(By.TAG_NAME, "h3").text
            price = book.find_element(By.CLASS_NAME, "price_color").text
            stock = book.find_element(By.CLASS_NAME, "instock.availability").text.strip()
            rating = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class").split()[-1]
            link = book.find_element(By.TAG_NAME, "a").get_attribute("href")
            
            books_data.append({
                "title": title,
                "price": price,
                "stock": stock,
                "rating": rating,
                "link": link
            })

        # Go to the next page
        try:
            next_button = driver.find_element(By.CLASS_NAME, "next")
            next_button.find_element(By.TAG_NAME, "a").click()
            time.sleep(2)  # Pause to load the next page
        except Exception as e:
            print(f"No more pages or error: {e}")
            break
    
    return books_data
