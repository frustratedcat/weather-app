import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Clear Screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Connect to webdriver
clear_screen()
print('Starting Up. Please Wait...\n')
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.page_load_strategy = 'eager'
driver = webdriver.Firefox(options=options)
driver.get('https://www.accuweather.com/')

# Get HTML elements
def get_element(time, type, name):
    driver.implicitly_wait(time)
    return driver.find_element(type, name)

# Get location for search
def get_user_location():
    location = input('Type your full address here:\n> ')
    return location.strip()

# Search location and return list of locations or result
def search_user_location():
    get_element(5, By.CLASS_NAME, 'search-input').send_keys(get_user_location() + Keys.ENTER)

# Current weather result
def weather_result():
    current_date = get_element(5, By.XPATH, '//div[contains(@class, "card-header")]/p')
    current_time = get_element(5, By.XPATH, '//p[contains(@class, "cur-con-weather-card__subtitle")]')
    print(current_date.text, current_time.text)

    today_forecast = get_element(5, By.XPATH, '//div[contains(@class, "body-item")][1]')
    tonight_forecast = get_element(5, By.XPATH, '//div[contains(@class, "body-item")][2]')
    print(f'\nToday\'s Forecast: {today_forecast.text}\nTonight\'s Forecast: {tonight_forecast.text}')

    current_temp = get_element(5, By.XPATH, '//div[contains(@class, "temp-container")]/div[1]')
    real_feel = get_element(5, By.XPATH, '//div[contains(@class, "temp-container")]/div[2]')
    print(f'\nCurrent Temperature: {current_temp.text} {real_feel.text}')

def main():
    try:
        clear_screen()
        search_user_location()
        clear_screen()
        weather_result()
    except:
        clear_screen()
        print('You mistyped, run the application again...')
    finally:
        driver.close()

if __name__ == '__main__':
    main()