"""TC-13: complete booking flow (FR-01). Run on your laptop: pip install selenium; start the booking page; set BASE_URL."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:5000"
driver = webdriver.Chrome()
try:
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL + "/book")
    wait.until(EC.visibility_of_element_located((By.ID, "party-size"))).send_keys("4")
    driver.find_element(By.ID, "submit").click()
    msg = wait.until(EC.visibility_of_element_located((By.ID, "confirmation")))
    assert "Booking confirmed" in msg.text
    driver.save_screenshot("tc13_booking.png")
    print("TC-13 PASSED")
finally:
    driver.quit()
