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
    - `pip install -r requirements.txt`
6. You will need to download the .xpi file of a version of uBlock Origin, and update the code accordingly for the version you download. Please see [Raymond Hill's Github](https://github.com/gorhill/uBlock/releases). Note that you may need to open it in a different browser than Firefox as Firefox wants to install it when you click the file rather than download it. 
7. Create a file called "ublock_xpi.py" and set a variable called "xpi" to a string that includes the file path to the .xpi file you downloaded. You can call the file and varialbe whatever you want, but you'll need to change the main.py references to it accordingly.
8. You should now be able to run the application without any problems.

To deactivate the virtual environment, simply type `deactivate` in your terminal.

If an error occurs, please check that your version of Firefox supports the version of uBlock Origin that you have downloaded. The purpose of using uBlock Origin is to remove content blocking objects that may occur in the AccuWeather DOM.
