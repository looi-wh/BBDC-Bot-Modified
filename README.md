# BBDC-Bot-Modified
a modified script based on https://github.com/rohit0718/BBDC-bot.
the original script was not made to run indifinitely, so i added my own codes into it

# Original script features
- auto logs into the bbdc webpage
- selects everything for month, session and day
- and books every slots for you
- was not designed to retry attempts

# Added features due to my modification
- selects user-specified month, session and day
- auto retry failed attempts
- random delays between each attempts [to prevent hammering on the server]
- auto restart script when an unexpected error occurs
- added more verbose


# Requirements
- python3
- a python module "selenium"
- google chrome
- chrome webdriver from http://chromedriver.chromium.org/downloads

# Editing the script
- edit the script with your favourite editor
- find a section
```
chromedriver_location = 'insert_chromedriver_location'
username = 'insert_username'
password = 'insert_password'
```
- edit the additional variables to select which slots to book
- it is a list variable, meaning you can always enter more than 1 slots at once

# Running it
```
python3 bbdc_bot.py
```

# Notice
PLEASE DO YOUR PART AND AVOID HAMMERING THEIR SERVER. IF THEY FOUND OUT WE ARE RUNNING BOTS, THIS SCRIPT WILL BE USELESS AND NOBODY WILL HAVE A LOVELY BOT ANYMORE
