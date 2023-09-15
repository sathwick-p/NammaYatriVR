import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

# Set the URL of the website and the path to your ChromeDriver executable
website_url = "https://nammayatri.in/open/"
chromedriver_path = r"Z:\4Ls\Alpaca\chromedriver-win64\chromedriver.exe"  # Update with your actual path

# Define the CSS selector as a variable
# Define the updated CSS selector as a variable
button_selector = "body > astro-island > div > div > div:nth-child(3) > div.flex.flex-col.items-center.gap-9.xmd\\:gap-10.py-6.sm\\:py-7.lg\\:py-14.px-4.sm\\:px-14.lg\\:px-30.xl\\:px-40.w-full > div > div.flex.md\\:flex-row.flex-col.md\\:flex-wrap.gap-y-16.justify-left.rounded-xl.w-full > div.md\\:w-1\\/2.w-full.md\\:order-1.md\\:pr-2.lg\\:pr-6 > div > div.flex.flex-col.w-full > div.flex.justify-between.mt-4.md\\:mr-0 > div > button"


# Function to download data from the website
def download_data():
    try:
        # Create a ChromeService instance with the specified path to ChromeDriver
        chrome_service = ChromeService(executable_path=chromedriver_path)
        
        # Initialize Chrome WebDriver with the ChromeService
        driver = webdriver.Chrome(service=chrome_service)
        driver.get(website_url)
        
        # Wait for the button to be clickable
        wait = WebDriverWait(driver, 10)
        download_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))
        
        # Click the download button
        download_button.click()
        
        # Sleep to allow the download to complete (you may adjust this based on download speed)
        time.sleep(10)
        
        print("Data downloaded successfully.")
        
        # Close the browser
        driver.quit()
    except Exception as e:
        print(f"Error: {str(e)}")

# Call the download_data function to initiate the download
download_data()
