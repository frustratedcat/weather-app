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

# Do all the stuff
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.page_load_strategy = 'eager'
driver = webdriver.Firefox(options=options)
driver.get('https://www.accuweather.com/')

# Add uBlock Origin addon
driver.install_addon('uBlock0_1.61.3b5.firefox.signed.xpi')

# Get HTML elements
def get_element(time, type, name):
    driver.implicitly_wait(time)
    return driver.find_element(type, name)

# Get location for search
def get_user_location():
    # Check if file exists
    if os.path.isfile('saved_location.txt'):

        # If file exists, open and check if empty
        with open('saved_location.txt') as saved_location:
            saved_string = str(saved_location.read())
            if len(saved_string) != 0:

                # If not empty, ask if user wants to use saved location
                use_saved_location = input(f'Would you like to use your prior location search?\n--------------------------------------------------\n{saved_string}\n--------------------------------------------------\n(Type "Yes" or "No")\n> ')

                try:
                    # If yes, return location 
                    if use_saved_location.lower() == 'yes':
                        location = saved_string
                        return location.strip()
                    # Else, ask for input
                    elif use_saved_location.lower() == 'no':
                        clear_screen()
                        with open('saved_location.txt', 'w') as saved_location:
                            location = input('Type your address here:\n> ')
                            saved_location.write(location)
                            return location.strip()
                except ValueError:
                    print('You were supposed to type "yes" or "no"...')

    else:
        with open('saved_location.txt', 'w') as saved_location:
            location = input('Type your address here:\n> ')
            saved_location.write(location)
            return location.strip()

# Search location and return list of locations or result
def search_user_location():
    get_element(5, By.CLASS_NAME, 'search-input').send_keys(get_user_location() + Keys.ENTER)

# Current weather result
def weather_result():
    clear_screen()
    # Print locaiton, date, time
    location =  get_element(5, By.CLASS_NAME, 'header-loc')
    current_date = get_element(5, By.XPATH, '//div[contains(@class, "card-header")]/p')
    current_time = get_element(5, By.XPATH, '//p[contains(@class, "cur-con-weather-card__subtitle")]')
    print(f'{location.text} | {current_date.text} | {current_time.text}')

    # Print today and tonight forecast
    today_forecast = get_element(5, By.XPATH, '//div[contains(@class, "body-item")][1]')
    tonight_forecast = get_element(5, By.XPATH, '//div[contains(@class, "body-item")][2]')
    print(f'\n{today_forecast.text}\n{tonight_forecast.text}')

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
    print('\nNext 5 Hours\n------------')
    for i in range(1, 6):
        hourly_list_time = get_element(5, By.XPATH, '//div[contains(@class, "hourly-list__list-wrapper")]/div/a[' + str(i) + ']/span[1]')
        hourly_list_temp = get_element(5, By.XPATH, '//div[contains(@class, "hourly-list__list-wrapper")]/div/a[' + str(i) + ']/span[2]')
        hourly_list_precip = get_element(5, By.XPATH, '//div[contains(@class, "hourly-list__list-wrapper")]/div/a[' + str(i) + ']/div/span')
        print(f'{hourly_list_time.text} | Temperature: {hourly_list_temp.text} | Precipitation: {hourly_list_precip.text}')

    # Print next 9 days
    print('\nNext 9 Days\n-----------')
    for i in range(2, 11):
        _9_day_day_of_week = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[1]/p[1]')
        _9_day_date = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[1]/p[2]')
        _9_day_high = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[2]/div/span[1]')
        _9_day_low = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[2]/div/span[2]')
        _9_day_outlook_day = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[3]/p')
        _9_day_outlook_night = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[3]/span/p')
        _9_day_precip = get_element(5, By.XPATH, '//a[contains(@class, "daily-list-item")][' + str(i) + ']/div[4]')
        print(f'{_9_day_day_of_week.text} - {_9_day_date.text} | High: {_9_day_high.text} | Low: {_9_day_low.text} | Day\'s Outlook: {_9_day_outlook_day.text} | Night\'s Outlook: {_9_day_outlook_night.text} | Precipitation: {_9_day_precip.text}')

    # Print sun and moon info
    print('\nSun and Moon\n------------')
    sunrise = get_element(5, By.XPATH, '//div[contains(@class, "sunrise-sunset__item")][1]/div/div[1]/span[2]')
    sunset = get_element(5, By.XPATH, '//div[contains(@class, "sunrise-sunset__item")][1]/div/div[2]/span[2]')
    moonrise = get_element(5, By.XPATH, '//div[contains(@class, "sunrise-sunset__item")][2]/div/div[1]/span[2]')
    moonset = get_element(5, By.XPATH, '//div[contains(@class, "sunrise-sunset__item")][2]/div/div[2]/span[2]')
    print(f'Sunrise: {sunrise.text} | Sunset: {sunset.text}\nMoonrise: {moonrise.text} | Moonset: {moonset.text}')

    # Print allergy outlook
    print('\nAllergy\n-------')
    tree_pollen = get_element(5, By.XPATH, '//a[contains(@class, "health-activities__item")][1]/span[2]')
    ragweed_pollen = get_element(5, By.XPATH, '//a[contains(@class, "health-activities__item")][2]/span[2]')
    mold = get_element(5, By.XPATH, '//a[contains(@class, "health-activities__item")][3]/span[2]')
    grass_pollen = get_element(5, By.XPATH, '//a[contains(@class, "health-activities__item")][4]/span[2]')
    dust_dander = get_element(5, By.XPATH, '//a[contains(@class, "health-activities__item")][5]/span[2]')
    print(f'Tree Pollen: {tree_pollen.text}\nRagweed Pollen: {ragweed_pollen.text}\nMold: {mold.text}\nGrass Pollen: {grass_pollen.text}\nDust & Dander: {dust_dander.text}\n')

# List weather results
def list_results():
    clear_screen()
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
        print('Retrieving data, please wait...')
        if driver.find_elements(By.CLASS_NAME, 'locations-list'):
            list_results()
            weather_result()
        else:
            weather_result()
    except:
        print('\nAn error has occurred... Run the program again')
    finally:
        driver.close()

if __name__ == '__main__':
    main()
