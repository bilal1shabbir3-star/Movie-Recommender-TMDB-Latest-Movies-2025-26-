import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 1. Setup Headless Chrome Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background without a UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Initialize the Browser Driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), 
    options=chrome_options
)

# 3. Target URL (Replace with your actual Streamlit App URL)
APP_URL = "https://streamlit.app" 

try:
    print("Navigating to Streamlit App...")
    driver.get(APP_URL)
    time.sleep(10)  # Wait for the page elements to load completely

    # 4. Search for the "Wake Up" button by its visual text
    # Streamlit uses specific text triggers like "Wake up this app" or "Yes, get this app back up!"
    wake_up_button = driver.find_element(By.XPATH, "//button[contains(., 'Wake up') or contains(., 'back up')]")
    
    if wake_up_button:
        wake_up_button.click()
        print("Success: Clicked the 'Wake Up' button!")
        time.sleep(5)  # Wait for wake process to initiate
    else:
        print("App was already awake or button wasn't found.")

except Exception as e:
    print(f"Notice: Could not click button (the app might already be awake). Detail: {e}")

finally:
    driver.quit()
