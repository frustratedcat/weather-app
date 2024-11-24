# Weather CLI

This is a weather application was built using python and selenium, and utilizes AccuWeather for data.

To install the application: 
1. Download the source code or copy the repo
2. Ensure you have Python and venv installed
3. Create a virtual environment using the following: 
    - `<python-version> -m venv <dir-name>`
    - Ex. `python3.10 -m venv py310`
4. After creating the virtual environment, activate it with the following:
    - `source <dir-name>/bin/activate`
    - Ex. `source py310/bin/activate`
5. At this point, you need to install the requirements from the requirements.txt file with the following: 
    - `pip freeze -r requirements.txt`
6. You should now be able to run the application without any problems.

To deactivate the virtual environment, simply type `deactivate` in your terminal.

If an error occurs, please check that your version of Firefox supports the version of uBlock Origin used here and download the correct uBlock .xpi file from [Raymond Hill's Github](https://github.com/gorhill/uBlock/releases).
The purpose of using uBlock Origin is to remove content blocking objects that may occur in the AccuWeather DOM. 