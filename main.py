import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Clear Screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Connect to webdriver
clear_screen()
driver = webdriver.Firefox()
driver.get('https://www.accuweather.com/')

# Get HTML elements
def get_element(time, type, name):
    driver.implicitly_wait(time)
    return driver.find_element(type, name)

# Get location for search
def get_user_location():
    location = input('Type your address here:\n> ')
    return location.strip()

# Search location and return list of locations or result
def search_user_location():
    get_element(20, By.CLASS_NAME, 'search-input').send_keys(get_user_location() + Keys.ENTER)

def main():
    search_user_location()

if __name__ == '__main__':
    main()