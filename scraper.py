from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sqlite3
import os
import time

# Headless Chrome Setup
def setup_browser():
    options = Options()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)
    return driver

def scrape_instagram(username):
    driver = setup_browser()
    url = f"https://www.instagram.com/{username}/"
    driver.get(url)
    time.sleep(5)  # Adjust delay based on internet speed

    # Find video elements and download
    videos = driver.find_elements(By.TAG_NAME, 'video')
    download_path = f"downloads/{username}/"
    os.makedirs(download_path, exist_ok=True)

    for index, video in enumerate(videos):
        src = video.get_attribute("src")
        if src:
            file_path = f"{download_path}video_{index}.mp4"
            with open(file_path, "wb") as f:
                f.write(requests.get(src).content)

            # Save metadata to database
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO videos (username, file_path) VALUES (?, ?)", (username, file_path))
            conn.commit()
            conn.close()

    driver.quit()
