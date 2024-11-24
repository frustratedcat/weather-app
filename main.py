import os
from datetime import datetime
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
    location = input('Type your address here:\n> ')
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
    print(f'\nCurrent Temperature: {current_temp.text}')
    
    # Check time
    now = datetime.now()
    sunset = get_element(5, By.XPATH, '//div[contains(@class, "sunrise-sunset__item")][1]/div/div[2]/span[2]')
    sunset_time = datetime.strptime(str(sunset.text), '%I:%M %p')

    # Compare and return result
    if (now.hour + now.minute / 60) < (sunset_time.hour + sunset_time.minute / 60):
        # Real feel
        real_feel = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[1]/span[2]')
        print(f'\nReal Feel: {real_feel.text}')

        # Print wind and wind gusts
        wind = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[2]/span[2]')
        wind_gusts = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[3]/span[2]')
        print(f'Wind: {wind.text}\nWind Gusts: {wind_gusts.text}')

        # Print air quality
        air_quality = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[4]/span[2]')
        print(f'Air Quality: {air_quality.text}')
    else:
        # Print wind and wind gusts
        wind = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[1]/span[2]')
        wind_gusts = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[2]/span[2]')
        print(f'Wind: {wind.text}\nWind Gusts: {wind_gusts.text}')

        # Print air quality
        air_quality = get_element(5, By.XPATH, '//div[contains(@class, "cur-con-weather-card__panel")][2]/div[3]/span[2]')
        print(f'Air Quality: {air_quality.text}')

    # Print hourly for the next 6 hours
    print('\nNext 6 Hours')
    for i in range(1, 7):
        hourly_list_time = get_element(5, By.XPATH, '//div[contains(@class, "hourly-list__list-wrapper")]/div/a[' + str(i) + ']/span[1]')
        hourly_list_temp = get_element(5, By.XPATH, '//div[contains(@class, "hourly-list__list-wrapper")]/div/a[' + str(i) + ']/span[2]')
        hourly_list_precip = get_element(5, By.XPATH, '//div[contains(@class, "hourly-list__list-wrapper")]/div/a[' + str(i) + ']/div/span')
        print(f'{hourly_list_time.text} | Temperature: {hourly_list_temp.text} | Precipitation: {hourly_list_precip.text}')

    # Print 10-day
    print('\n10-Day Forecast')
    for i in range(1, 11):
        _10_day_day_of_week = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[1]/p[1]')
        _10_day_date = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[1]/p[2]')
        _10_day_high = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[2]/div/span[1]')
        _10_day_low = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[2]/div/span[2]')
        _10_day_outlook_day = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[3]/p')
        _10_day_outlook_night = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[3]/span/p')
        _10_day_precip = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[4]')
        print(f'{_10_day_day_of_week.text} - {_10_day_date.text} | High: {_10_day_high.text} | Low: {_10_day_low.text} | Day\'s Outlook: {_10_day_outlook_day.text} | Night\'s Outlook: {_10_day_outlook_night.text} | Precipitation: {_10_day_precip.text}')

    # Print sun and moon info
    print('\nSun and Moon')
    sunrise = get_element(5, By.XPATH, '//div[contains(@class, "sunrise-sunset__item")][1]/div/div[1]/span[2]')
    sunset = get_element(5, By.XPATH, '//div[contains(@class, "sunrise-sunset__item")][1]/div/div[2]/span[2]')
    moonrise = get_element(5, By.XPATH, '//div[contains(@class, "sunrise-sunset__item")][2]/div/div[1]/span[2]')
    moonset = get_element(5, By.XPATH, '//div[contains(@class, "sunrise-sunset__item")][2]/div/div[2]/span[2]')
    print(f'Sunrise: {sunrise.text} | Sunset: {sunset.text}\nMoonrise: {moonrise.text} | Moonset: {moonset.text}')

    # Print allergy outlook
    print('\nAllergy')
    tree_pollen = get_element(5, By.XPATH, '//a[contains(@class, "health-activities__item")][1]/span[2]')
    ragweed_pollen = get_element(5, By.XPATH, '//a[contains(@class, "health-activities__item")][2]/span[2]')
    mold = get_element(5, By.XPATH, '//a[contains(@class, "health-activities__item")][3]/span[2]')
    grass_pollen = get_element(5, By.XPATH, '//a[contains(@class, "health-activities__item")][4]/span[2]')
    dust_dander = get_element(5, By.XPATH, '//a[contains(@class, "health-activities__item")][5]/span[2]')
    print(f'Tree Pollen: {tree_pollen.text}\nRagweed Pollen: {ragweed_pollen.text}\nMold: {mold.text}\nGrass Pollen: {grass_pollen.text}\nDust & Dander: {dust_dander.text}\n')

# List weather results
def list_results():
    print('Location Results:')
    result_len = driver.find_elements(By.XPATH, '//div[contains(@class, "locations-list")]/a')
    for i in range(1, len(result_len) + 1):
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
    except:
        print('\nAn error has occurred... Run the program again')
    finally:
        driver.close()

if __name__ == '__main__':
    main()