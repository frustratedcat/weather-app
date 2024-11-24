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

# Add uBlock Origin addon
driver.install_addon('uBlock0_1.61.3b0.firefox.signed.xpi')

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
    # Print locaiton, date, time
    location =  get_element(5, By.CLASS_NAME, 'header-loc')
    current_date = get_element(5, By.XPATH, '//div[contains(@class, "card-header")]/p')
    current_time = get_element(5, By.XPATH, '//p[contains(@class, "cur-con-weather-card__subtitle")]')
    print(f'{location.text} | {current_date.text} | {current_time.text}')

    # Print today and tonight forecast
    today_forecast = get_element(5, By.XPATH, '//div[contains(@class, "body-item")][1]')
    tonight_forecast = get_element(5, By.XPATH, '//div[contains(@class, "body-item")][2]')
    print(f'\nToday\'s Forecast: {today_forecast.text}\nTonight\'s Forecast: {tonight_forecast.text}')

    # Print current temp and real feel
    current_temp = get_element(5, By.XPATH, '//div[contains(@class, "temp-container")]/div[1]')
    real_feel = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[1]/span[2]')
    print(f'\nCurrent Temperature: {current_temp.text}\nReal Feel: {real_feel.text}F')

    # Print wind and wind gusts
    wind = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[2]/span[2]')
    wind_gusts = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[3]/span[2]')
    print(f'Wind: {wind.text}\nWind Gusts: {wind_gusts.text}')

    # Print air quality
    air_quality = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[4]/span[2]')
    print(f'Air Quality: {air_quality.text}')

    # Print hourly for the next 6 hours
    print('\nNext 6 Hours')
    for i in range(1, 7):
        hourly_list_time = get_element(5, By.XPATH, '//div[contains(@class, "hourly-list__list-wrapper")]/div/a[' + str(i) + ']/span[1]')
        hourly_list_temp = get_element(5, By.XPATH, '//div[contains(@class, "hourly-list__list-wrapper")]/div/a[' + str(i) + ']/span[2]')
        hourly_list_precip = get_element(5, By.XPATH, '//div[contains(@class, "hourly-list__list-wrapper")]/div/a[' + str(i) + ']/div/span')
        print(f'{hourly_list_time.text} | Temperature: {hourly_list_temp.text}F | Precipitation: {hourly_list_precip.text}')

    # Print 10-day

    # Print sun and moon info

    # Print allergy outlook

# List weather results
def list_results():
    for i in range(1, 11):
        result = get_element(5, By.XPATH, '//div[contains(@class, "locations-list")]/a[' +  str(i) + ']/p[2]')
        print(i, result.text)
    choose_item = input('\nPlease choose an item by typing 1 - 10:\n> ')
    get_element(5, By.XPATH, '//div[contains(@class, "locations-list")]/a[' + str(choose_item) + ']/p[2]').click()
          
def main():
    try:
        clear_screen()
        search_user_location()
        clear_screen()
        if driver.find_elements(By.CLASS_NAME, 'locations-list'):
            list_results()
            clear_screen()
            weather_result()
        else:
            weather_result()
    # except:
    #     print(f'\nThat is not in the range... Run the program again')
    finally:
        driver.close()

if __name__ == '__main__':
    main()